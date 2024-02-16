#chicken has 2 legs x = chicken
#rabbit has 4 legs  y = rabbit
heads = 35
legs = 94
def solve(numheads, numlegs):
    """
    x + y = 35
    2x + 4y = 94

    x + y = 35
    x + 2y = 47

    y = 12
    x = 23
    
    """
    rabbit = (numlegs / 2) - numheads
    chicken = numheads - rabbit
    print("chickens : ", int(chicken))
    print("rabbits : ", int(rabbit))
solve(heads, legs)