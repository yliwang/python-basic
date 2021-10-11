def CountHeadsAndLegs( m, n ):
    x = max( m, n )
    for i in range( 1, x ):
        for j in range( 1, x ):
            if i+j == m and i*2 + j*4 == n:
                return (i, j )


    return None



if __name__=='__main__':
    r = CountHeadsAndLegs( 35, 94 )
    print( r )
    assert r == (23, 12)
