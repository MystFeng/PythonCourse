import random

pistol_magazine = [0, 0, 0, 0, 0, 0]
random_indices = random.sample(range(len(pistol_magazine)), 3)
print(random_indices)
for index in random_indices:
    pistol_magazine[index] = 1
print(pistol_magazine)