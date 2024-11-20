import copy
site = {
    'html': {
        'head': {
            'title': 'Buy/sell a cheap phone'
        },
        'body': {
            'h2': 'We have the cheapest price for an iPhone',
            'div': 'Buy',
            'p': 'Sell'
        }
    }
}

def change_value(struct, key, value):
    if key in struct:
        struct[key] = value
    else:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                change_value(sub_struct, key, value)

    return struct

def display_struct(struct, spaces=1):
    for key, value in struct.items():
        if isinstance(value, dict):
            print(' ' * spaces, key)
            display_struct(value, spaces + 3)
        else:
            print("{}{}:{}".format(' ' * spaces, key, value))

def make_site(name):
    struct_site = copy.deepcopy(site)
    new_title = 'Buy/sell a cheap {}'.format(name)
    struct_site = change_value(struct_site, 'title', new_title)
    new_h2 = 'We have the cheapest price for an {}'.format(name)
    struct_site = change_value(struct_site, 'h2', new_h2)
    return struct_site

sites = []
sites_count = int(input('How much sites: '))
for _ in range(sites_count):
    product_name = input('Enter the name of products for site: ')
    new_site = make_site(product_name)
    sites.append(new_site)
    for i_site in sites:
        display_struct(i_site)