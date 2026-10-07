""" def wizards(N,start,duels):
    owner = start
    changed_hands= 1
    #print(duels[0][1])
    if duels[0][1] == owner:
        owner = duels[0][0]
        changed_hands +=1
        print(owner)

wizards(3, "A", ["BA", "CB", "DA"]) """


def wizards(N,start,duels):
    owner = start
    num_owners= 1
    #print(duels[0][1])
    if duels[i][1] == owner:
        owner = duels[0][0]
        num_owners +=1
        print(owner, num_owners)
        for i in range [N]:
            if duels [i][1] == owner:
                owner = duels[i][0] 
                num_owners += 1
    print(owner, num_owners)

wizards(3, "A", ["BA", "CB", "DA"])