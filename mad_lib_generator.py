# A cliche one
print("Welcome to Mad Lib Generator - a very common one")

def name():
    first = input("please enter your name: ").capitalize()
    print("\n Roses are " + first + "'s best friend!?\n")
    return first

#gathering the input
adjective1 = input("tell me an adjective: ").capitalize()
noun1 = input("tell me a noun: ").capitalize()
noun2 = input("tell me another noun: ").capitalize()
adjective2 = input("tell me another adjective: ").capitalize()

#printing the result
print("Roses are " + adjective1)
print(noun1 + " are blue")
print(noun2 + " is " + adjective2)
print("And so are you!")
