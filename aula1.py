import numpy as np
import random
import sys

def roll_dice(n,seed):
    random.seed(seed)
    dice_rolls = []
    for i in range(n):
        dice_rolls.append(random.randint(1,6))
    mean_outcome = np.mean(dice_rolls)
    return f"A média dos lançamentos é {mean_outcome}"


if __name__ == '__main__':
    n = int(sys.argv[1])
    seed = int(sys.argv[2])
    print(roll_dice(n,seed))
