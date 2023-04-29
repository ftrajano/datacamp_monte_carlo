# Bootstraping (sampling with replacement)

import random 
import numpy as np

nba_heights = [196, 191, 198, 216, 188, 185, 211, 201, 188, 191, 201, 208, 191, 183, 196]
simu_heights = []

for i in range(1000):
    boostrap_sample = random.choices(nba_heights, k=15)
    simu_heights.append(np.mean(boostrap_sample))
upper = np.quantile(simu_heights, 0.975)
lower = np.quantile(simu_heights, 0.025)
print(f"Intervalo de confiança: [{lower:.2f}, {upper:.2f}]")
print(f"Mean: {np.mean(simu_heights)}")
