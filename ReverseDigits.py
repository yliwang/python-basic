def ReverseDigits( n ):
    s = str( n )
    s = s[::-1]
    r = int(s)

    return r


if __name__=='__main__':
    n = ReverseDigits( 123 )
    print( n )
