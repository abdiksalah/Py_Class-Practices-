favorite_languages ={
    'jen': ['python', 'ruby'],
    'sarah':['c'],
    'edward':['ruby', 'go'],
    'pil':['python', 'haskell'],
    }
for name, language in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\it" + language.title())