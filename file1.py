#hello
#world
#test
print("Hello world")
name=input('enter your name:')
print(name)

contact=eval(input('enter your mobile number'))
def print_info(contact):
    assert contact is int,'enter only int'
    print(f'your number is {contact} ')


print_info(contact)