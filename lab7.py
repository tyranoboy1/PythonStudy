print("학번: 201704033  이름 : 한지훈")
def genPrime(maxnum) :
    num = 2
    while num < maxnum :
        is_prime = True
        for i in range(2,num):
            if num % i == 0 :
                is_prime = False
                break
        if(is_prime):yield  num
        num+=1

it = genPrime(50)
for i in it:
    print(i, end=",")
