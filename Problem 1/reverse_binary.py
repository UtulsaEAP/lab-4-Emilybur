"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Emily Burke
Lab Time: Friday at 3

"""


def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE

    while user_num > 0:
        print(user_num % 2, end ="")
        user_num = user_num //2


if __name__ == "__main__":
    reverse_binary()
 