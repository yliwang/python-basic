# python function printing a star triangle

def OutputStarTriangle( n ):
    for i in range( 1,n+1 ):
        for j in range(1,n-i+1):
            print(' ', end='')            
        for j in range(1,2*i):
            print( '*', end='' )
        else:
            print('')



if __name__=='__main__':
    OutputStarTriangle( 5 )
