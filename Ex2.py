# Write a function that prints all factors of the given parameter x
import math

def print_factor(x):
  for i in range(x+1):
    if i!=0 and x%i==0 : print(i)
def main():
    x=int(input())
    print_factor(x)
    
if __name__ == '__main__':
    main()