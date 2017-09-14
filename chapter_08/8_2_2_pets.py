def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='cat', pet_name='tom')
describe_pet(pet_name='jerry', animal_type='mouse')