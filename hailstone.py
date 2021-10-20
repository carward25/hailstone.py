#name: Cassidy Ward
#date: 10/19/2021
#description: this program takes a positive integer parameter
#as the initial number of a hailstone sequence and returns how many steps it takes to reach 1

def hailstone(n):
    count = 0  # number of steps to 0
    while n != 1:  # as long as n is not 1
        if n % 2 == 0:  # if n is even
            n //= 2
        else:
            n = 3 * n + 1
        count += 1  # increase number of steps
    return count  #return number of steps