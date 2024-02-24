"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Emily Burke
Lab Time: Friday at 3
"""

def password_mod():
    word = input()
    password = ''
    # Type your code here.
    replacements  = {
        'i': '1',
        'a': '@',
        'm': 'M',
        'B': '8',
        's': '$'
    }
    password_mod=''
    for char in password:
        password_mod += replacements.get(char,char) 
    password_mod = str(password_mod)
    password_mod += '!'
    print(password_mod)

    if __name__ == "__main__":
        password_mod()