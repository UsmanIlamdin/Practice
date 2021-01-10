from collections import ChainMap


fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog  = {'name': "Clifford", 'hands': "paws", 'color': "red"}

# one way is
dog_fish = {**fish, **dog}
#aother way
dog_fish1 =dict(ChainMap(fish,dog))

print(dog_fish)
print(dog_fish1)