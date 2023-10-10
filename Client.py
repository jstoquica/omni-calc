from omniORB import CORBA
import Middleware

orb = CORBA.ORB_init([], CORBA.ORB_ID)
ior = input("Enter IOR of Calculator object: ")

obj = orb.string_to_object(ior)
calculator = obj._narrow(Middleware.Calculator)

if calculator is None:
    print("Object reference is not a Calculator")
else:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    result_add = calculator.add(x, y)
    result_subtract = calculator.subtract(x, y)
    result_multiply = calculator.multiply(x, y)

    try:
        result_divide = calculator.divide(x, y)
        print(f"Add: {result_add}, Subtract: {result_subtract}, Multiply: {result_multiply}, Divide: {result_divide}")
    except Middleware.DivideByZero as e:
        print(f"Add: {result_add}, Subtract: {result_subtract}, Multiply: {result_multiply}, {e}")

