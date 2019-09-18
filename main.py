from KG import *
from NLG import *
import DB, DM
from NLU import wit_parse

# Init the database, NLG and knowledge graph
database = DB.Db()
NL_generator = NLGer()
k_graph = knowledge_table()
k_graph.contact_state = ['phone_number', 'contact', 'location']

# Hard code the database
samples_1 = {'contact': 'Alex', 'phone_number': '206-555-6789', 'location':'175 Stevens Way'}
for samples in [samples_1]:
    sample_order_entry = DB.Entry(k_graph.partial_state)
    sample_contact_entry = DB.Entry(k_graph.contact_state)
    for k, v in samples.items():
        sample_contact_entry.add(k, v)
    database.add(sample_contact_entry.get_by_key('phone_number'), sample_order_entry, sample_contact_entry, False)

samples_2 = {'contact': 'Alexandra', 'phone_number': '206-555-0000', 'location':'155 Stevens Way'}
samples_3 = {'pizza_type':'4 cheese', 'pizza_size':'medium', 'crust_type':'gluten free', 'delivery_type':'delivery'}
sample_order_entry = DB.Entry(k_graph.partial_state)
sample_contact_entry = DB.Entry(k_graph.contact_state)
for k, v in samples_2.items():
    sample_contact_entry.add(k, v)
for k, v in samples_3.items():
    sample_order_entry.add(k, v)
database.add(sample_contact_entry.get_by_key('phone_number'), sample_order_entry, sample_contact_entry, True)

# Random pick the initial question
start_init = ['pizza_type', 'pizza_type', 'delivery_type'][np.random.randint(0,3)]

# Init the dialogue manager
dm = DM.Dm(database, k_graph, start_init)

print(NL_generator.response(['start', start_init], None, None, None))
while (True):
    inputStr = input("> ")
    inputStr = inputStr.lower()
    if (inputStr == 'quit'):
        break
    e, v = wit_parse(inputStr)
    if (e[0] == 'cancel'):
        print('Your previous order has been cancelled, thanks and have a nice day!')
        break
    if (e[0] == 'repeat'):
            print(outputStr)
            continue
    if (e[0] == 'start-over'):
        print(NL_generator.response(['start', start_init], None, None, None))
        dm = DM.Dm(database, k_graph, start_init)
        continue
    act, signal, order_entry, contact_entry = dm.execute(e, v)
    outputStr = NL_generator.response(act, signal, order_entry, contact_entry)
    print(outputStr)
