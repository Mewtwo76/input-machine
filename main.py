import math
import random
import prydain


user1 = prydain.User("yournamehere", "memes", 13, "fitMC")



users = [user1]
currentUser = None

def login():
  global currentUser
  global users
  input2 = input("username: ").strip()
  input1 = input("password: ").strip()
  for user in users:
    if user.authenticate(input2, input1):
      currentUser = user
      return True
  currentUser = None
  return False

while True:
    x = []
    input1 = input(f'{currentUser.id + "s" if currentUser else ""} input> ')

    if "login" == input1.lower():
        print("enter your login")
        if login():
          print("correct!")
        else:
          print("wrong pwd")

    if currentUser:
      if "age".lower() == input1.lower():
        print(currentUser.myAge())        

      if "youtube".lower() == input1.lower():
        print(currentUser.myYoutube())

      if "logout" == input1.lower():
        print(f"{currentUser.id} has been succesfully logged out!")
        currentUser = None
    
      if "calculator" == input1.lower():
        print("what do you want to calculate? addition mode only. enter 2 value. numbers only.")

        x = lambda q, w : q + w
        y = lambda e, r : e - r
        z = lambda t, u : t / u
        v = lambda d, s : d * s
        input3 = int(input("first value> "))
        input4 = int(input("second value> "))
        print(x(input3, input4))
        print(y(input3, input4))
        print(z(input3, input4))
        print(v(input3, input4))

