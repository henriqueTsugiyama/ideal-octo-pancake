import math

def is_prime(arg_num):

    """return whether it is a prime number"""

    if arg_num <= 1:
        return False
    for i in range(2,int(math.sqrt(arg_num) + 1)):
        if arg_num % i == 0:
            return False
    return True

def main():

    """contém toda a lógica principal"""

    for i in range(100):
        if is_prime(i):
            print (i, end=' ')
    print()

if __name__ == '__main__':
    main()
