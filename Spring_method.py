'''
s = ' abrakatabra '
print(s.lstrip())
s = 'fortune'
print(s.upper())
first_name = "lola"
last_name = 'aderanti'
full_name = first_name.capitalize() + last_name.title()
print(full_name)
print('The upper of first name is:' + first_name.upper())
word = 'cartarract'
print(word[0])
print(word[5])
print('The character with the index of 0 is', word[0],word)
print(word[0:3])
print(word[6:14])
print(word[0] + word[1] + word[3])
print(word[0:7:2])
print(word[ :-1])
print(word[-5:-1])
print(word[-1:-5])
print(word.format())'''
s = 'spammy'
print(s.replace('mm','xx'))
print(s.find('mm'))
print(s.isalpha())
print(s.isdecimal())
print(s.isdigit())
print(s.isprintable())