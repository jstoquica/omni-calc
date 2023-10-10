from omniORB import CORBA
import Middleware, Middleware__POA

class Calculator_i(Middleware__POA.Calculator):
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise Middleware.DivideByZero("Cannot divide by zero")

orb = CORBA.ORB_init([], CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")
poaManager = poa._get_the_POAManager()
poaManager.activate()

calculator = Calculator_i()
obj = calculator._this()

print(orb.object_to_string(obj))
print("Middleware Server ready...")

orb.run()

