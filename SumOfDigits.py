def SumOfDigits( n ):
    s = str(n)
    t = 0
    for x in s:
        t += int( x )

    return t


if __name__=='__main__':
    s = SumOfDigits( 12345 )
    print( s )
