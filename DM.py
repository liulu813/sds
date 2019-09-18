import DB
import numpy as np

class Dm:
    def __init__(self, database, graph, init_question):
        self.database = database
        self.graph = graph
        self.order_entry = DB.Entry(graph.partial_state)
        self.contact_entry = DB.Entry(graph.contact_state)
        self.confirmation, self.check = False, False
        self.question = init_question
        self.fav = False
        self.query = False
        self.fav_comfirm = False
    def execute(self, entity, value):
        # Cannot parse the response, repeat the question
        if not entity:
            return ['repeat', self.keys_order[self.question_idx]], None, self.order_entry, self.contact_entry
        e, v = entity[0], value[0]
        # Universals
        if e == 'cancel' or e == 'start-over':
            self.order_entry.clear()
            self.contact_entry.clear()
            self.question_idx = 0
            self.fav = False
            self.query = False
            return [e], None, self.order_entry, self.contact_entry
        if e == 'repeat':
            return [self.keys_order[self.question_idx]], None, self.order_entry, self.contact_entry

        if e == 'favorite':
            self.fav = True
            self.order_entry.fill_dummy()

        if e == 'query':
            self.query = True
            self.order_entry.fill_dummy()
        if self.fav:
            if e == 'phone_number':
                self.contact_entry.add(e, v)
            #if self.contact_entry.get_by_key('phone_number'):
                fav_order, fav_contact  = self.database.get_fav_order(self.contact_entry.get_by_key('phone_number'))
                if fav_order:
                    self.contact_entry = fav_contact
                    self.order_entry = fav_order
                    self.fav = False
                    self.fav_comfirm = True
                    #return ['confirmation'], None, self.order_entry, self.contact_entry
                else:
                    self.order_entry.clear()
                    self.fav = False
                    return ['no_fav'], None, self.order_entry, self.contact_entry

        # Request info in given order
        if not self.query and not self.fav:
            for e, v in zip(entity, value):
                if e in self.order_entry.get_keys():
                    self.order_entry.add(e, v.lower())
                elif e in self.contact_entry.get_keys():
                    self.contact_entry.add(e, v.lower())
            order_candidate = self.order_entry.return_candidate_state()
            contact_candidate = self.contact_entry.return_candidate_state()
        else:
            order_candidate = []
            contact_candidate = ['phone_number']
        if order_candidate:
            res = [order_candidate[
                       np.random.randint(0, len(order_candidate))]]
            if np.random.rand(1)[0] < 0.7:
                res = ['confirm_action'] + res
            return res, None, self.order_entry, self.contact_entry
        elif contact_candidate:
            res = [contact_candidate[
                       np.random.randint(0, len(contact_candidate))]]
            if np.random.rand(1)[0] < 0.7:
                res = ['confirm_action'] + res
                #if 'phone_number' in entity and 'location' not in entity and self.database.get_entry(value[entity.index['phone_number']]):
                #    self.contact_entry.add('location', self.database.get_entry(value[entity.index['phone_number']])[0][1].get_by_key('location'))
                #    return ['phone_contact'], None, self.order_entry, self.contact_entry
            return res, None, self.order_entry, self.contact_entry
        else:
            if self.fav:
                self.order_entry = self.database.get_fav_order(self.contact_entry.get_by_key('phone_number'))[0]
                return ['fav'], None, self.order_entry, self.contact_entry
            if self.query:
                self.order_entry = self.database.get_entry(self.contact_entry.get_by_key('phone_number'))[-1][0]
                return ['query'], None, self.order_entry, self.contact_entry

            self.database.add(self.contact_entry.get_by_key('phone_number'), self.order_entry, self.contact_entry, False)

            if not self.confirmation:
                self.confirmation = True
                if not self.fav_comfirm:
                    return ['confirmation'], None, self.order_entry, self.contact_entry
                else:
                    return ['fav_confirmation'], None, self.order_entry, self.contact_entry
            else:
                price = self.get_price()
                if self.order_entry.get_by_key('delivery_type') == 'pick-up':
                    return ['check_pick_up'], price, self.order_entry, self.contact_entry
                else:
                    return ['check_deliver'], price, self.order_entry, self.contact_entry

    def get_price(self):
        res = 0
        for toppings in self.graph.pizza_topping_table[self.order_entry.get_by_key('pizza_type')]:
            res += self.graph.price_table[self.graph.topping_type[toppings]]
        res += self.graph.price_table[self.order_entry.get_by_key('crust_type')][self.order_entry.get_by_key('pizza_size')]
        res += self.graph.price_table[self.order_entry.get_by_key('delivery_type')]
        return res
