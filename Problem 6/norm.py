"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Emily Burke
Lab Time: friday at 3
"""

def norm():
    # Write your code here
    num=[]
    nums=int(input())

    for i in range(nums):
        val = float(input())
        num.append(val)

    for i in range (nums):
        print(f'{num[i]//100.0:.2f}')

    if __name__ == "__main__":
        norm()