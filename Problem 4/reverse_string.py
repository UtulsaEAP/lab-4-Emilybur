"""
Complete the following python code to reverse the string entered by the user.

Name:Emily Burke
Lab Time: Friday at 3
"""

def reverse_string():
    # YOUR CODE HERE
    reverse_string = str(input())
    stop = ['Done', 'done', 'd']
    while reverse_string not in stop:
        print(reverse_string[::-1])
        
    if __name__ == "__main__":
        reverse_string()