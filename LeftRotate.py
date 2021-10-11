def LeftRotate( l, k ):






if __name__=='__main__':
    l = [ 1, 2, 3, 4, 5]
    r = LeftRotate( l, 1 )
    print( r )
    assert r == [5, 1, 2, 3, 4]
