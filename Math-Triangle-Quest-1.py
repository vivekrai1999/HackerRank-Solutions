for i in range(1,int(input())):
    print(i*((10)**i)//9)
    
# 1     = 1
# 22    = 2 x 11
# 333   = 3 x 111
# 4444  = 4 x 1111
# 55555 = 5 x 11111

# to get series of 1,11,111,1111,11111 use formula (10)**i//9 then multiply each i with this formula
