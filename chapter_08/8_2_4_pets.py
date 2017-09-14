def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("\nMy " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('willie')
describe_pet(pet_name='willie')

describe_pet('tom', 'cat')
describe_pet(pet_name='jerry', animal_type='mouse')
describe_pet(animal_type='bird', pet_name='mike')