# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
import math
for li in l:
    for i in range(li+1):
        if i!=0 and li%i==0 : print(i)
    print("next")