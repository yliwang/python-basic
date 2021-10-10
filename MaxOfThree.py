def MaxOfThree( x, y, z ):
    return max( max(x, y ), z )



if __name__ == '__main__':
    m = MaxOfThree( 1, 5, 3 )
    print( m )
    assert m == 5 
