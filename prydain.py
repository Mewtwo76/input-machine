class Character():
  def __init__(self, name):
    self.name = name

  def whoAmI(self):
    print(self.name)

'''
class Something():
  def __init__(self, age):
    self.age = age

  def whatsurage(self):
    print(self.age)
'''

class User():
  def __init__(self, id, password, age, youtube):
    self.id = id
    self.pwd = password
    self.age = age
    self.utube = youtube
  
  def authenticate(self, id, password):
    if id == self.id:
      if password == self.pwd:
        return True
    return False

  def myAge(self):
    return self.age

  def myYoutube(self):
    return self.utube

'''
class Calculator():
  def __init__(self, value1, value2):
    self.val1 = value1
    self.val2 = value2
'''
