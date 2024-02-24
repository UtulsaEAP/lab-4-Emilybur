"""
Complete the following python code to reverse the string entered by the user.

Name:Emily Burke
Lab Time: Friday at 3
"""

def reverse_string():
    # YOUR CODE HERE
    word = str(input())
    stop = ['Done', 'done', 'd']
    while word not in stop:
        print(word[-1::-1])

    if __name__ == "__main__":
        reverse_string()