import numpy as np
import random

def roll_dice(n: int, seed: int) -> str:
    """
    Simulates rolling a six-sided dice n times using a given random seed.

    Parameters
    ----------
    n : int
        Number of times to roll the dice.
    seed : int
        Seed for the random number generator.

    Returns
    -------
    str
        A string containing the mean outcome of the dice rolls, formatted as
        "A média dos lançamentos é X", where X is the mean outcome rounded to
        two decimal places.
    """
    random.seed(seed)
    dice_rolls = []
    for i in range(n):
        dice_rolls.append(random.randint(1, 6))
    mean_outcome = np.mean(dice_rolls)
    return f"A média dos lançamentos é {mean_outcome:.2f}"