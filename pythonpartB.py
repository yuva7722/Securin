def partB(dicemat):
    total_outcomes = 0
    for r in dicemat:  
        r_sum = sum(r)  
        total_outcomes += r_sum
    prob = {}
    for i in range(2, 13):
        sumoutcome = sum(row.count(i) for row in dicemat)
        prob[i] = sumoutcome/ total_outcomes
    return prob

def transformation(dice_a, dice_b, total_outcomes):
    orgdist = partB(distribution)
    
    targetdist = orgdist.copy()  
    needed_outcomes = {sum_value: int(probability * total_outcomes) for sum_value, probability in orgdist.items()}
    
    new_dice_a = []
    for spots in dice_a:
        if spots <= 4:
            new_dice_a.append(spots)
        else:
            for face in range(1, 7):
                if needed_outcomes[face + 1] >= 0:
                    new_dice_a.append(face + 1)
                    needed_outcomes[face + 1] -= 1
                    break

    new_dice_b = dice_b.copy()    
    return new_dice_a, new_dice_b

Dice_A = [1, 2, 3, 4, 5, 6];Dice_B = [1, 2, 3, 4, 5, 6];total_outcomes = 36

def create_distribution():
    dicemat = [[0] * 6 for _ in range(6)]
    for i in range(1, 7):
        for j in range(1, 7):
            dicemat[i-1][j-1] = i + j
    return dicemat

distribution = create_distribution()


New_Dice_A, New_Dice_B = transformation(Dice_A, Dice_B, total_outcomes)
print("Transformed Dice A:", New_Dice_A)
print("Transformed Dice B:", New_Dice_B)
