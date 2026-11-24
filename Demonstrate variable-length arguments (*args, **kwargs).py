def numbers(*args):
    print("Numbers:", args)

def details(**kwargs):
    print("Details:", kwargs)

numbers(10, 20, 30)

details(name="Ravi", age=18, city="Hyderabad")