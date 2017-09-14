favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("------------------------------")

for name in favorite_languages.keys():
    print(name.title())


print("------------------------------")

for name in favorite_languages:
    print(name.title())


print("------------------------------")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " +
              favorite_languages[name].title() + "!")


print("------------------------------")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")