# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


x = 20
factors = [2, 3]
answ = 0

if x > 3:
    for i in range(4, x):
        factors.append(i)
        print(i)
        for j in factors:
            if j == i:
                continue
            if i % j == 0:
                factors.remove(i)
                print(-i)
                break
            elif j*j == i:
                factors.append(j)
                print(j)
                break
            elif j*j*j == i:
                factors.append(j)
                print(j)
                break
            
                
            
        print(factors)
else: 
    answ = x



# 2, 3, 