import numpy as np

# Parameters
num_plans = 50000
mean_cost = 20000
std_dev_cost = 10000
df = 5  # Degrees of freedom (choose based on how heavy you want the tails)

# Simulate the costs of each plan from a t-distribution
plan_costs = np.random.standard_t(df, size=num_plans) * std_dev_cost + mean_cost

# Calculate the total cost
total_cost = np.sum(plan_costs)

print("Total cost for the year = ", total_cost / 1000000000, "billion")
