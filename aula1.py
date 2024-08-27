class Exemplo:
     def __init__(self, a=2, b=3):
         self.a = a
         self.b = b

     def f(self, x):
         return self.a*x +self.b
     
     obj1 = Exemplo()
         
print(obj1.f(1))