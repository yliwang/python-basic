def SortList( lst, order ):
    l = lst.copy()
    if order == 'asc':
        l.sort()
    elif order == 'desc':
        l.sort( reverse=True)
    else:
        pass

    return l


if __name__=='__main__':
    lst = [ 1, 3, 2, 5, 4]
    l = SortList( lst, 'asc' )
    print( l )
    l = SortList( lst, 'desc' )
    print( l )
    l = SortList( lst, 'none' )
    print( l )
    
        
