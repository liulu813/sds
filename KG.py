class knowledge_table:
    def __init__(self):
        self.full_state = {'pizza_type', 'pizza_size', 'pizza_toppings', 'crust_type', 'sides', 'drinks', 'delivery_type'}

        self.partial_state = {'pizza_type', 'pizza_size', 'crust_type', 'delivery_type'}

        self.contact_state = {'contact', 'phone_number', 'location'}

        self.pizza_type = {'hawaiian', 'meat lovers', '4 cheese', 'pepperoni', 'veggie supreme', 'vegan'}

        self.pizza_size = {'small', 'medium', 'large'}

        self.pizza_topping_table = {'hawaiian':['pineapple' , 'ham', 'mozzarella'],
                              'meat lovers': ['mozzarella', 'pepperoni', 'ham', 'bacon', 'sausage'],
                              '4 cheese': ['mozzarella', 'cheddar', 'swiss', 'provolone'],
                              'pepperoni': ['mozzarella', 'pepperoni'],
                              'veggie supreme': ['mozzarella', 'green peppers', 'red onions', 'mushrooms', 'black olives'],
                              'vegan': ['green peppers', 'red onions', 'mushrooms', 'black olives']}

        self.topping_type = {'mozzarella':'cheese','cheddar':'cheese','swiss':'cheese','provolone':'cheese',
                        'pineapple':'veggie','green peppers':'veggie','red onions':'veggie',
                          'mushrooms':'veggie','black olives':'veggie','pepperoni':'meat','ham':'meat','bacon':'meat_lux','sausage':'meat_lux'}

        self.crust_type = {'thin', 'regular', 'deep dish', 'gluten free'}

        self.sides = {'bread sticks','cheese sticks','green salad','caesar salad'}

        self.drinks = {'cola','root beer','orange soda','lemon soda','mineral water','ginger ale'}

        self.delivery_type = {'pick-up', 'delivery'}

        self.price_table = {
            'cheese':1.5, 'veggie':2., 'meat':2.5, 'meat_lux':3.,
            'bread sticks':7.,'cheese sticks':9.,'green salad':10.,'caesar salad':12.,
            'cola':3.50, 'root beer':3.50, 'orange soda':3.50, 'lemon soda':3.50, 'mineral water':4.50, 'ginger ale':3.50,
            'pick-up':0, 'delivery':3.,
            'thin':{'small':10., 'medium':12., 'large':14.},
            'regular':{'small':10., 'medium':12., 'large':14.},
            'deep dish':{'small':12., 'medium':14., 'large':16.},
            'gluten free':{'small':15., 'medium':18., 'large':21.}
        }

        self.entity_name_table = {
            'pizza_type':self.pizza_type, 'pizza_size':self.pizza_size,
            'crust_type':self.crust_type, 'delivery_type':self.delivery_type
        }

