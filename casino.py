def casino(quarters,m1,m2,m3):
    plays = 0
    machine = 1

    while quarters > 0:
        quarters -= 1
        plays += 1
        if machine == 1:
            m1 += 1
            if m1 == 35:
                quarters += 30
                m1 = 0
            machine = 2
        elif machine == 2:
            m2 += 1
            if m2 == 100:
                quarters += 60
                m2 = 0
            machine = 3
        else:
            m3 += 1
            if m3 == 10:
                quarters += 9
                m3 = 0
            machine = 1
        print(f"Martha plays {plays} times before going broke.")
        casino(quarters=100,m1=0,m2=0,m3=0)







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

print:(f"Martha plays {plays} before going broke") """



