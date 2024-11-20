def find_key(struct, key, max_depth = None, depth = 1):
    result = None

    if max_depth and max_depth < depth:
        return result
    
    if key in struct:
        return struct[key]
    
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct,key, max_depth, depth=depth+1)

            if result is not None:
                break

    return result

site = {
    'html': {
        'head': {
            'title': 'My website'

        },
        'body': {
            'h2': 'Here my header',
            'div': 'Here some block',
            'p': 'And here new stroke'
        }
    }
}

while True:
    key = input('Enter key:')
    answer = input('Do you want enter max depth? Y/N:')
    if answer.lower() == 'y':
        max_depth = int(input('Enter max depth:'))
    else:
        max_depth = None
    print('Key value:', find_key(struct=site, max_depth=max_depth, key=key))