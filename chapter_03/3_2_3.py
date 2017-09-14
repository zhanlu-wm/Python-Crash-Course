print("=====================del=====================\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

print("-----------------------------------------")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

print("-----------------------------------------")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[-1]
print(motorcycles)


print("=====================pop()=====================\n")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print("-----------------------------------------")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle)

print("-----------------------------------------")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(popped_motorcycle)


print("=====================remove()=====================\n")

motorcycles = ['honda', 'yamaha', 'suzuki', 'yamaha']
print(motorcycles)

print(motorcycles.remove('yamaha'))     # None
print(motorcycles)

print("-----------------------------------------")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove('ducati')
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
