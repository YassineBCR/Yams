

def is_yams(dices: list):
    x=dices[0]
    for r in dices:
        print(f"x={x} r = {r}")
        if r != x:
            return 0
        else: 
            x=r
    return 50  

def score_grand_suite(dices: list):
    dices.sort()
    print(f"gds{dices}")
    for i in range(len(dices)-1):
        print(f"i={dices[i]} i+1={dices[i+1]}  ")
        if (dices[i]+1) != dices[i+1]:
            return 0
    return 40