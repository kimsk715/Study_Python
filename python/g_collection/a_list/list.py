animals = ['dog', 'cat', 'bird', 'fish']
# print(type(animals))
# print(animals.__str__())

# 인덱스로 접근
print(animals[1])
print("=" * 50)
print(animals[-1])
print(len(animals))

animals.append('hamster')
print(animals)

animals.append('hamster')
print(animals)

del animals[1]
print(animals)

animals.remove('hamster')
print(animals)

for animal in animals:
    print(animal + "..")


index = animals.index('hamster')
print(index)

animals[index] = 'lion'
print(animals)
print(animals * 2)

