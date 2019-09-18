from wit import Wit

access_token = 'THG6FDGCGQ6XRO7TH3XYTRCMOYON33FM'
client = Wit(access_token = access_token)

def wit_parse(message):
    if 'cancel' in message.lower():
        return ['cancel'], ['cancel']
    if 'start-over' in message.lower():
        return ['start-over'], ['start-over']
    if 'repeat' in message.lower():
        return ['repeat'], ['repeat']
    if 'favorite' in message.lower():
        return ['favorite'], ['favorite']
    if 'query' in message.lower():
        return ['query'], ['query']
    resp = client.message(message)
    entities = None
    values = None

    try:
        entities = list(resp['entities'].keys())
        values = [resp['entities'][key][0]['value'] for key in entities]
    except:
        pass

    return entities, values