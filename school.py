class Math ():
  def __init__(self, y: int, x: int):
    """
    Will preform simple math operations on X and Y
    """
    self.y = y
    self.x = x
  
  def add(self):
    return self.y + self.x 
  
  def sub(self):
    return self.y - self.x