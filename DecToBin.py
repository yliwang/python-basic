def DecToBin( n ):
    b = ''
    while( n > 0 ):
        bit = n&1
        b += str(bit)
        n >>= 1

    b = b[::-1]
    return b


if __name__=='__main__':
    s = DecToBin( 32 )
    print( s )
