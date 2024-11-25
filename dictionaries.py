# working with dictionaries
alien_0 = {'colour': 'green', 
           'points': 5
           }

print(alien_0['colour'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

print(alien_0)

del alien_0['points']
print(alien_0)
# create an empty dictionary
alien_1 = {}
print(alien_1)

# favourite languages dict

favourite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'rust',
    'phil': 'python',
}
print(favourite_languages)

# looping through dictionaries

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
print(user_0)

for key, value in user_0.items():
    print(f"\nKey: {key} \nValue: {value}")

for name in favourite_languages.keys():
    print(name.title())

# loop through dict in a certain order
for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for polling.")

# loop through values
print("\n")
print("The following languages are favourites.")
for language in favourite_languages.values():
    print(language.title())

# loop through values with a 'set' to group uniques
print("\n")
print("The following languages are favourites.")
for language in set(favourite_languages.values()):
    print(language.title())

# rivers
rivers = {
    'nile': 'egypt',
    'thames': 'england',
    'seine': 'france',
}
print("\n")
print(rivers)

for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}.")

for key in rivers.keys():
    print(key)
for value in rivers.values():
    print(value)

names_to_poll = ['jim', 'jen', 'pete', 'phil', 'clive']
for name in names_to_poll:
    if name in favourite_languages.keys():
        print(f"Thank you for already taking the poll {name}")
    else:
        print(f"Hello {name} we would like to invite you to poll.")

alien_1 = {
    'colour': 'yellow',
    'points': 10,
}
alien_2 = {
    'colour': 'red',
    'points': 15
}

# nest a number of dicts in a list 

aliens = [alien_0, alien_1, alien_2]
print(aliens)
for alien in aliens:
    print(alien)

# auto generate a lot of aliens
aliens = []
for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'} 
    aliens.append(new_alien)

for alien in aliens[:10]:
    print(alien)
print("...")

print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15