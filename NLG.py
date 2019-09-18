import numpy as np

class NLGer:
    def __init__(self):
        self.corpus = {
            'start':['Welcome to the pizza ordering system. '],
            'pizza_type':['What pizza do you want? We have Hawaiian, Meat Lovers, 4 Cheese, Pepperoni, Veggie Supreme and vegan.',
                          'Which specialty do you want?',
                          'What pizza would like to order?',
                          'What pizza do you want to order?',
                          'What would you like?'],
            'pizza_size':['What size?',
                          'Size? Can be large, medium or small.',
                          'What size do you like? We have large, medium and small.'],
            'crust_type':['What crust type? We have thin, regular, deep dish, gluten free.',
                          'Crust?'],
            'delivery_type':['Pick-up or delivery?',
                             'Is this for pick-up or delivery?'],
            'contact':['Name?', 'What is your name?'],
            'phone_number':['Phone number?', 'What is your phone number please?'],
            'location':['Address?','May I have your address?'],
            'repeat':['Sorry I did not get you.', 'Sorry I might not be clear of your answer.'],
            'confirmation':['Got your order for a ', 'I have an order for a ', 'Okay, I have a '],
            'check_deliver':['Your order has been received. It will be delivered in 30 minutes or less and cost $',
                     'Thanks, I got your order. It will be delivered in 30 minutes and cost $',
                     'I have your order. It will be there in 30 minutes and cost $'],
            'check_pick_up':['Your order has been received. It will be ready in 15 minutes or less and cost $',
                     'Thanks, I got your order. It will be ready in 15 minutes and cost $',
                     'I have your order. It will be ready in 15 minutes and cost $'],
            'confirm_action':['Sure thing!',
                              'Got it.',
                              'Thank you.',
                              'Great!'],
            'no_fav': ['Sorry, we do not have your favorite order on file. Your order this time will be saved as your favorite order.']
        }

    def get_res_by_act(self, acts):
        res = [self.corpus[act][np.random.randint(0, len(self.corpus[act]))] for act in acts]
        return ' '.join(res)

    def response(self, acts, signal, order_entry, contact_entry):
        res = ''
        if acts[0] == 'confirmation' or acts[0] == 'fav_confirmation':
            res += self.get_res_by_act(['confirmation'])
            res += '{} {} on {} crust for {}. '.format(order_entry.get_by_key('pizza_size'),
                                               order_entry.get_by_key('pizza_type'),
                                               order_entry.get_by_key('crust_type'),
                                               order_entry.get_by_key('delivery_type'))
            if acts[0] == 'fav_confirmation':
                res += ' to {} under the name of {}.'.format(contact_entry.get_by_key('location'),contact_entry.get_by_key('contact'))
            res += 'Is that Okay?'
        elif acts[0] in ('check_deliver','check_pick_up'):
            res += self.get_res_by_act(acts)
            res += '{}.'.format(signal)
        elif acts[0] == 'phone_contact':
            res += 'I have your address at {}. Is that okay?'.format(contact_entry.get_by_key('location'))
        elif acts[0] == 'fav':
            res = 'I have your favorite order of '
            res += '{} {} on {} crust for {}. '.format(order_entry.get_by_key('pizza_size'),
                                               order_entry.get_by_key('pizza_type'),
                                               order_entry.get_by_key('crust_type'),
                                               order_entry.get_by_key('delivery_type'))
            res += 'Is that right?'
        elif acts[0] == 'query':
            res = 'I have your order of '
            res += '{} {} on {} crust for {}. '.format(order_entry.get_by_key('pizza_size'),
                                               order_entry.get_by_key('pizza_type'),
                                               order_entry.get_by_key('crust_type'),
                                               order_entry.get_by_key('delivery_type'))
            res += ' Thanks!'
        else:
            res += self.get_res_by_act(acts)
        return res


