class Entry:
    def __init__(self, title):
        self.title = title
        self.item = dict(zip(self.title, [None] * len(self.title)))

    def get_by_key(self, key):
        return self.item.get(key, None)

    def get_keys(self):
        return  self.item.keys()

    def get_values(self):
        return self.item.values()

    def get_item(self):
        return self.item

    def add(self, key, value):
        self.item[key] = value

    def remove(self, key):
        self.item[key] = None

    def clear(self):
        for k in self.item.keys():
            self.item[k] = None

    def fill_dummy(self):
        for k in self.item.keys():
            self.item[k] = 'dummy'

    def return_candidate_state(self):
        if None in self.item.values():
            return [k for k, v in self.item.items() if v == None]
        else:
            return []

class Db:
    def __init__(self):
        self.db = {}

    def add(self, phone, order_entry, contact_entry, fav_bool):
        if phone not in self.db:
            self.db[phone] = [(order_entry, contact_entry, fav_bool)]
        else:
            self.db[phone].append((order_entry, contact_entry, fav_bool))

    def remove(self, phone):
        if phone in self.db:
            return self.db.pop(phone)
        else:
            return None

    def get_entry(self, phone):
        res = self.db.get(phone, None)
        return res

    def get_fav_order(self, phone):
        if phone not in self.db:
            return None, None
        for each_o, each_c, fav in self.db[phone]:
            if fav:
                return each_o, each_c
        return None, None

    def get_len(self):
        return len(self.db)




