import random
import string

str = 'qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*_+'
from collections import Counter
def randomcode(n:int,Len):
    used=Counter()
    ans=list()
    for _ in range(n):

        code=[random.choice(str) for i in range(Len)]
        code = ''.join(code)
        while used[code]!=0:
            code = [random.choice(str) for i in range(Len)]
            code = ''.join(code)
        used[code]=1
        ans.append(code)
    return ans

print(randomcode(200,10))
