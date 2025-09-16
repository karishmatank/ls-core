## Q1
print(range(0, 25, 3)[6])

## Q2
substring = 'Launch School'
c_index = substring.find('c')
print(substring[c_index:c_index + 6])

## Q3
original_tuple = (1, 2, 3, 4, 5)
new_tuple = original_tuple[len(original_tuple)-2:0:-1]
print(new_tuple)

## Q4
pets = {
    'Cat': 'Meow',
    'Dog': 'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog'])
print(pets.get('Lizard', None)) # Alternatively, just pets.get('Lizard')
print(pets.get('Lizard', '<silence>'))

## Q7
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

print(info.replace(':', '+'))
print('+'.join(info.split(':')))

## Q9
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606
print(stuff)

## Q10
cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

## Q12
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1)
print(3 in numbers2)
print(3 in numbers3)
print(3 in numbers4)
print(3 in numbers5)

## Q14
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

print(list(zip(my_str, my_list, my_tuple, my_range)))