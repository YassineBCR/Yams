

def is_yams(dices: list):
    x=dices[0][1]
    for r in dices:
        print(f"x={x} r = {r[1]}")
        if r[1] != x:
            return 0
        else: 
            x=r[1]
    return 50  