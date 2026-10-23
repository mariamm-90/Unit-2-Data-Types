def casino(quarters, m1, m2, m3):
    plays = 0

    while quarters > 0:

        #machine 1
        quarters -= 1
        plays += 1
        m1 += 1
        if m1 == 35:
            quarters += 30
            m1 = 0
        if quarters == 0:
            break

        #MACHINE 2    
        quarters -= 1
        plays += 1
        m2 += 1
        if m2 == 100:
            quarters += 60
            m2 = 0
        if quarters == 0:
            break
            
        #MACHINE 3
        quarters -= 1
        plays += 1
        m3 += 1
        if m3 == 10:
            quarters += 9
            m3 = 0
        if quarters == 0:
            break

    print(f"Dasha plays {plays} times before going broke")
    return plays
casino(quarters=48, m1=3, m2=10, m3=4)





""" def casino(quarters,m1,m2,m3):
    plays = 0
    machine = 1

    while quarters > 0:
        if plays[0] == 35:
            quarters += 30 and plays[0] == 0
        else:
            quarters -= 1
            plays [0] += 1
            if plays[1] == 100:
                quarters += 60 and plays [1] == 0
            else:
                quarters -= 1 
                plays[1] += 1
                if plays[2] == 10:
                    quarters += 9 and plays [2] == 0
                else:
                    quarters -= 1
                    plays[2] += 1
        if quarters == 0:
            break

print:(f"Martha plays {plays} times before going broke") """



