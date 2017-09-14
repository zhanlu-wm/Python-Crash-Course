favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


print("The following language have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("=============================================")

print("The following language have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())