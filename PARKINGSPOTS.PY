def occupied(n, y, t):
    spaces = 0
    for i in range(n):
        if y[1] == "C" and t[i] == "C":
        spaces = spaces + 1 
    return spaces

occupied(5,"CC....")