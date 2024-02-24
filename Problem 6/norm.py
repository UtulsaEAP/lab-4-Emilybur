"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Emily Burke
Lab Time: friday at 3
"""

def norm():
    # Write your code here
    num=[]
    nums= int(input())
    for i in range(nums):
        val = float(input())
        num.append(val)
    max=max(num)
    for i in range (num):
        print(f'{num[i]/max:.2f}')
    if __name__ == "__main__":
        norm()