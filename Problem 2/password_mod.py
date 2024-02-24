"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Emily Burke
Lab Time: Friday at 3
"""

def password_mod():
    word = input()
    password = ''
    # Type your code here.
    character= input()
    if (character == 'i'):
        password += '1'
    elif (character == 'a'):
        password += '@'
    elif (character == 'm'):
        password += 'M'
    elif (character == 'B'):
        password += '8'
    elif (character == 's'):
        password += '$'
    else:
        password += character 
    print(password)

    if __name__ == "__main__":
        password_mod()