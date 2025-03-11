pin=input("enter the pin")
if len(pin) in [4,6] and pin.isdigit():
    print(pin,"is valid",True)
else:
    print(pin,"not valid",False)