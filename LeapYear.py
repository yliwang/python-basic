def IsLeapYear( y ):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False




if __name__=='__main__':
    r = IsLeapYear( 2020 )
    print ( r )
    assert r == True
