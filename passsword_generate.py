import random
import string


#  password generator
def creating_passwords():
    password = ""
    rand = ""
    for i in range(3):
        rand = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                              'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
        password += rand
        numbers = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        password += numbers
    password += rand.upper()
    for i in range(2):
        special_characters = random.choice(['~', '!', '@', '#', '$', '%', '^', '&', '*', '_'])
        password += special_characters

    pass_word = list(password)
    random.shuffle(pass_word)
    print(''.join(pass_word))


creating_passwords()

