def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
    n = len(energyDrinkA)
    dpA = [0] * n
    dpB = [0] * n

    dpA[0] = energyDrinkA[0]
    dpB[0] = energyDrinkB[0]

    for i in range(1, n):
        dpA[i] = max(dpA[i-1] + energyDrinkA[i], dpB[i-1])
        dpB[i] = max(dpB[i-1] + energyDrinkB[i], dpA[i-1])

    return max(dpA[-1], dpB[-1])


# Example 1:

# Input: energyDrinkA = [1,3,1], energyDrinkB = [3,1,1]

# Output: 5

# Explanation:

# To gain an energy boost of 5, drink only the energy drink A (or only B).

# Example 2:

# Input: energyDrinkA = [4,1,1], energyDrinkB = [1,1,3]

# Output: 7

# Explanation:

# To gain an energy boost of 7:

# Drink the energy drink A for the first hour.
# Switch to the energy drink B and we lose the energy boost of the second hour.
# Gain the energy boost of the drink B in the third hour.
