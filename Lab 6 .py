# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(password):
    result=""
    for i in range(0,len(password)):
        if (int(password[i])+3>=10):
            result+=str((int(password[i])+3)%10)
        else:
            result+=str(int(password[i])+3)
    return result


def decode(password):
    result=""
    for i in range(0,len(password)):
        if (int(password[i]) - 3 < 0):
            result += str((int(password[i]) - 3) % 10)
        else:
            result += str(int(password[i]) - 3)
    return result


def main():
    user_input=-1
    while user_input!=3:
        print_menu()
        user_input = int(input('Please enter an option: '))
        if user_input==1:
            user_password = input("Please enter your password to encode: ")
            encode_password = (encode(user_password))
            print("Your password has been encoded and stored!")
        if user_input==2:
            print("The encoded password is " + encode_password + ", and the original password is " + decode(encode_password) + ".")
            
main()