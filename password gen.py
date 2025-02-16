import random
import time
import string


def Alphanumerical():

    adverb = [
    "quickly", "silently", "eagerly", "gracefully", "carefully", "happily", "angrily", "patiently", "lazily", "naturally", "enthusiastically", "smoothly", "boldly", "brightly", "clearly", "neatly", "reliably", "comfortably", "sharply", "loudly", "abruptly", "calmly", "exactly", "mysteriously", "innocently", "warmly", "precisely", "briskly", "cheerfully", "intentionally", "sweetly", "freely", "generously", "recklessly", "cautiously", "safely", "timidly", "quickly", "carelessly", "gently", "heavily", "immediately", "effortlessly", "harshly", "steadily", "subtly", "safely", "foolishly", "occasionally", "constantly"
    ]
    adjective = ["beautiful", "dangerous", "careful", "intelligent", "generous", "honest", "mysterious", "spicy", "quiet", "loud", "bright", "warm", "cold", "heavy", "light", "expensive", "eager", "fearless", "powerful", "delicate", "sharp", "strong", "hard", "soft", "easy", "rough", "smooth", "honorable", "friendly", "trustworthy", "optimistic", "miserable", "creative", "lazy", "patient", "playful", "complicated", "peaceful", "kind", "cheerful", "curious", "romantic", "generous", "delicious", "fashionable", "rich", "unique", "colorful", "beautiful", "unpredictable", "unreliable", "unstoppable"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    symbols = ["!", "@", "$", "%", "&"]

    random.shuffle(adverb)
    random.shuffle(adjective)
    random.shuffle(symbols)
    random.shuffle(numbers)

    generated_password = adverb[0] + adjective[0] + numbers[0] + numbers[1] + numbers[2] + symbols[0]

    return generated_password

def PIN():
   amount = int(input("Enter length of pin: "))
   nums = [str(i) for i in range(amount)]
   random.shuffle(nums)

   pincode = ''.join(nums[:amount])

   return pincode

def random_pass():
  amount = int(input("Enter length of password: "))
  chars = "0123456789!@#$%&*()QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm"
  password = ""

  for i in range(amount):
    password += "".join(random.choice(chars))
  
  return(f"{password} \r")



  
    
    
  
    

 

def coolprintthing():
  target_password = generated_password


  char_set = string.ascii_letters + string.digits + string.punctuation
  sleeptime = 0.0025

  if password_type == "pin":
     char_set = string.digits
     sleeptime = 0.1

  if password_type == "random":
     sleeptime = 0.0005
     char_set = string.ascii_letters + string.punctuation + string.digits

  guessed_password = " "

  for i in range(len(target_password)):
    while True:
      guessed_password = guessed_password[:i] + random.choice(char_set)

      print(f"    GENERATING...  {guessed_password}", end = "\r" )
      random_char = random.choice(char_set)


      time.sleep(sleeptime)

      if random_char == target_password[i+1]:
                guessed_password += random_char
                break 

  print(f"Successful generation! \033[1m{guessed_password}\033[0m is your {password_type} password!")


password_type = input("What sort of password do you require? (Alphanumerical, PIN, Random, Passphrase or Long): ")

if password_type not in ["alphanumerical", "pin", "PIN", "random", "passphrase", "long"]:
  print("Error, invalid password type!")
  exit()

if password_type == "alphanumerical":
  generated_password = Alphanumerical()

elif password_type == "pin":
  generated_password = PIN()

elif password_type == "random":
  random_pass()
  generated_password = random_pass()

coolprintthing()










  

