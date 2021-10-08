def SumOfMultiplesOf3And5( limit ):
    s = 0
    for i in range( limit+1 ):
        if i%3 == 0 or i%5 == 0:
            s += i

    return s








if __name__=='__main__':
    s = SumOfMultiplesOf3And5( 20 )
    print( s )
