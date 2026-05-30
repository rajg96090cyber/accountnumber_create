import datetime 
import random

# x = datetime.datetime.now()

# print(random.randint(10,99))

# # print(x.second)



stateCode = {
    "MP":11,
    "UP":74,
    "BR":79,
    "UK":62,
    "MH":24
}

def generateAccountNumber(state):

    x = datetime.datetime.now()

    account = ""
    account += str(stateCode[state])
    account += str(x.year%100)
    account += str(x.day)
    sec = x.second
    if sec<10:
        sec = "0"+str(sec)
    account += str(sec)

    account +=  str(random.randint(10,99))

    return account



print(generateAccountNumber("UP"))
