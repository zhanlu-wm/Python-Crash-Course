favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


for name in favorite_languages.keys():
    print(name.title() + ", thank you for taking the poll.")

print("===================================================")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")