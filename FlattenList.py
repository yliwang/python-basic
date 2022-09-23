def FlattenList( l ):



if __name__=='__main__':
    r = FlattenList( [1, [2], [3,4,5], [6,7], 8] )
    assert r == [1, 2, 3, 4, 5, 6, 7, 8]
