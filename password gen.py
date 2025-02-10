import random
import time
import string


def password(password_type):

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


    

password_type = input("What sort of password do you require? (Alphanumeric, PIN, Random, Passphrase or Long): ")
generated_password = password(password_type)






target = generated_password

char_set = string.ascii_lowercase + string.digits + string.punctuation

guessed_password = ''

for i in range(len(target)):
    while True:
      guessed_password = guessed_password[:i] + random.choice(char_set)

      print(f"    GENERATING...  {guessed_password}", end = "\r" )

      time.sleep(0.01)

      if guessed_password == target[:i + 1]:
         break

print(f"Successful creation! {guessed_password} is your {password_type} password!")

  

