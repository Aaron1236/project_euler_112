#Project Euler 112
#Aaron McKeown 2/17/2017
#Answer: 1,587,000

"""
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy.
In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""

#determine whether a number is bouncy or not
#track the ratio of bouncy/ non bouncy

#while ratio is less than .99
#determine if number is bouncy
#apply results to running ratio
#iterate to next number to be checked

def bounce_o_not(num):
    #returns 1 if num is bouncy, returns 0 is num is not bouncy
    if increasing(num) is True or decreasing(num) is True:
        return 0
    else:
        return 1

def increasing(num):
    i = 0
    num = str(num)
    while num[i] <= num[i + 1]:
        if i + 2 is len(num):
            return True
        i += 1
    return False

def decreasing(num):
    i = 0
    num = str(num)
    while num[i] >= num[i + 1]:
        if i + 2 is len(num):
            return True
        i += 1
    return False
#Initializations
bounce = 0
notbounce = 99 #no number below 100 are bouncy. starting at 100 is a good way to save time
num = 99 #no number below 100 are bouncy. starting at 100 is a good way to save time

while (bounce / (bounce + notbounce)) < .99:
    num += 1
    if bounce_o_not(num) is 1:
        bounce += 1
    elif bounce_o_not(num) is 0:
        notbounce += 1


print('ratio is ', bounce / (bounce + notbounce), 'bounce count ', bounce, 'num ', num)

