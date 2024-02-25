import numpy as np
import scipy.stats as stats

# Sample Space
sample_space_coin_toss = ['H', 'T']

# Probability of getting heads (classical approach)
prob_heads_classical = 1 / len(sample_space_coin_toss)
print("Probability of getting heads (Classical approach):", prob_heads_classical)

# Random Variable for Coin Toss (0 for Tails, 1 for Heads)
def coin_toss():
    return np.random.choice([0, 1])

# Probability associated with random variable (Coin Toss)
def prob_coin_toss(num_heads):
    return sum(1 for _ in range(10000) if coin_toss() == num_heads) / 10000

# Probability Mass Function (PMF) for Coin Toss
pmf_coin_toss = {num_heads: prob_coin_toss(num_heads) for num_heads in range(2)}
print("PMF for Coin Toss (0 for Tails, 1 for Heads):", pmf_coin_toss)

# Continuous Random Variable for Height (Assuming Uniform Distribution)
heights = np.random.uniform(100, 190, 10000)

# Probability Density Function (PDF) for Height
pdf_height = stats.gaussian_kde(heights)
print("PDF for Height (Sample):", pdf_height)

# Mean and Variance for Height
mean_height = np.mean(heights)
variance_height = np.var(heights)
print("Mean Height:", mean_height)
print("Variance of Height:", variance_height)
