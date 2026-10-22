def casino(quarters,m1,m2,m3):
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

print:(f"Martha plays {plays} before going broke")



