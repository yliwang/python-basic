def RemoveDuplicate( l ):
    prev = None
    r = []
    for x in l:
        if prev == None:
            prev = x
            r.append( x )
        elif prev != x:
            r.append( x )
            prev = x

    return r



if __name__=='__main__':
    l = [0, 0, 1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 2, 2]
    r = RemoveDuplicate( l )
    print( r )
    assert r == [0, 1, 2, 3, 4, 5, 6, 2]
