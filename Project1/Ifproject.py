name = input("Please type your name.")
age = int(input("Please type your age"))

if 18 <= age < 31:
    print("Welcome to club 18-30 holidays, {0}".format(name))
else:
    print("Sorry but you are not in the age bracket for club 18-30 holidays, Thank you, {0}".format(name))
