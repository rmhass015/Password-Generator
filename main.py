import random

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '&', '?', '#', '$', '%']

charNum = [chars, nums]
allChars = [chars, nums, symbols]

print("Password Generator")
print("Passwords generated are defined by you!")
print("Please answer the following questions to generate your password! \n")

length = input("How long would you like your password? ")
choice = input("Would you like\n 1: letters\n 2: Letters and numbers\n 3: Letters number and symbols? ")

phrase = []


if int(choice) == 1:
  for i in range(int(length)):
    pletter = random.choice(chars)
    phrase += pletter
  password = ''.join(phrase)
  print(f"You're generated password is: " + password)
elif int(choice) == 2:
  for i in range(int(length)):
    pletter = random.choice(random.choice(charNum))
    phrase += pletter
  password = ''.join(phrase)
  print(f"You're generated password is: " + password)
elif int(choice) == 3:
  for i in range(int(length)):
    pletter = random.choice(random.choice(allChars))
    phrase += pletter
  password = ''.join(phrase)
  print(f"You're generated password is: " + password)
else:
  print("Invaild input, please try again.\n")

