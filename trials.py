"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    pass  # TODO: replace this line with your code
    for item in items:
        print(item)


def get_all_evens(nums):
    pass  # TODO: replace this line with your code
    evens = []

    for num in nums:
        if num % 2 == 0:
            evens.append(num)

    return evens


def get_odd_indices(items):
    pass  # TODO: replace this line with your code
    result = []

    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])
    
    return result


def print_as_numbered_list(items):
    pass  # TODO: replace this line with your code
    i = 1

    for item in items:
        print(f'{i}. {item}')
        i += 1



def get_range(start, stop):
    pass  # TODO: replace this line with your code
    nums = []

    for num in range(start, stop):
        if num < stop:
            nums.append(num)
    
    return nums


def censor_vowels(word):
    pass  # TODO: replace this line with your code
    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)
    
    return ''.join(chars)
    

def snake_to_camel(string):
    pass  # TODO: replace this line with your code
    camelCase = []

    for word in string.split('_'):
        camelCase.append(f'{word[0].upper()}{word[1:]}')
    
    return ''.join(camelCase)

def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
