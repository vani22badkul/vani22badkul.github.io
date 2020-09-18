


def most_frequent(text):
    letters = [letter.lower() for letter in text if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print(letter, count)

def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary

most_frequent('Mississippi')
