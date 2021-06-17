class car():

  #init method or constructor
  def __init__(self,model,colour):
    self.model = model
    self.colour = colour
  
  def show(self):
    print("Model is", self.model)
    print("colour is", self.colour)

audi = car("audi a4", "blue")
ferrari = car("Ferrari 488", "green")

audi.show()
ferrari.show()
