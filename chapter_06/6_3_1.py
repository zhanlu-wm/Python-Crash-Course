# for k, v in dict.items()


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last':'fermi'
}


for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


print("-------------------------------------------")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")