def SumOfNumbersInString( s ):
    l = s.split(' ')
    t = 0
    for x in l:
        if x.isnumeric():
             t += int(x)


    return t


if __name__=='__main__':
    s = '123 abc 45678 defghijk 1'
    t = SumOfNumbersInString( s )
    print( t )
    assert t == 123+45678+1
    
    
    
