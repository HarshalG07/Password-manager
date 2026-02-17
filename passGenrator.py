from random import *
lowerletters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upperletters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','%','$','&','*','_']
MIN_LEN = 12
MAX_LEN = 16

no_symbols = randint(1,3)
no_numbers = randint(1,4)
no_upper = randint(2,4)
no_lower_lowerLimit = MIN_LEN - no_symbols-no_numbers-no_upper
no_lower_upperLimit = MAX_LEN - no_symbols-no_numbers-no_upper
no_lower = randint(no_lower_lowerLimit,no_lower_upperLimit)

def pass_gen():
    password=[]

    for _ in range(no_symbols):
        x = choice(symbols)
        password.append(x)
    for _ in range(no_numbers):
        x=choice(numbers)
        password.append(x)
    for _ in range(no_upper):
        x=choice(upperletters)
        password.append(x)
    for _ in range(no_lower_lowerLimit,no_lower_upperLimit):
        x=choice(lowerletters)
        password.append(x)
    shuffle(password)

    return "".join(password)
