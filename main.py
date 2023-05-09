from random import sample

# Voila mon code pour un générateur de mot de passe aléatoire

listnumber = list(range(1, 9))
listalphabet = ['a', 'b ', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
listspecial = ['$', '*', '!', '?']

listalphabet = [letter.replace("'", "") for letter in listalphabet]
password_list = sample(listnumber, 4) + sample(listalphabet, 7) + sample(listnumber, 4) + sample(listspecial, 2)
password_str = "".join(str(x) for x in password_list)
print("Voici votre mot de passe entre : ")
print(password_str)

