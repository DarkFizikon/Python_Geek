synonims_dict = dict()

pairs_count = int(input('Enter the numbers pair words: '))

for i_pair in range(pairs_count):
    first_word, second_word = input(f'{i_pair + 1} pair: ').lower().split(' - ')
    synonims_dict[first_word] = second_word
    synonims_dict[second_word] = first_word

while True:
    word = input('Enter the word: ').lower()
    if word in synonims_dict:
        print('Synonim: ', synonims_dict[word].capitalize())
        break
    else:
        print('The word isn\'t in dictionary')