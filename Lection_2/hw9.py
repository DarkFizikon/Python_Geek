def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1

    return sym_dict

def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)

    return inv

text = input('Enter the text: ')
hist = histogram(text)

print('The original frequency dictionary:')
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

inv_hyst = invert_dict(hist)

print('\nThe inventionary frequency dictionary:')
for i_sym in sorted(inv_hyst.keys()):
    print(i_sym, ':', inv_hyst[i_sym])
    