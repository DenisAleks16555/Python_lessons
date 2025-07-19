class Auto:
    def __init__(self):
      self.form = "Седан"
      self.color = "Белый" 
      self.power = 200 
   

bmv = Auto()

print(bmv)
print(bmv.form)
print(bmv.color)
print(bmv.power)

bmv.power = 250
print(bmv.power)

audi = Auto()
print(audi.power)
