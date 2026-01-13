print("\033[42m----WEIGHT_CONVERSION----\033[0m")
print("\033[36m choice 1 converts kg to pound\n choice 2 converts pound to kg\n\033[0m")
choice=int(input("\033[35mENTER YOUR CHOICE:\033[0m"))
if choice==1:
    print("\033[40mCONVERTING WEIGHT TO POUNDs\033[0m")
else:print("\033[40mCONVERTING WEIGHT TO KGs\033[0m")
weight=float(input("\033[32mENTER YOUR BODY WEIGHT:\033[0m"))
if choice==1:
    print("\033[33m weight in kg is \033[0m ",(weight*2.20462))
else:
    print("\033[33m weight in pounds\033[0m ",(weight*0.453592))

