import numpy as np

# Parameters
n = 50000  #EHCPs per year
mean_cost = 22000  # Mean cost
std_dev_cost = 10000  # Standard deviation of cost
df = 15  # Degrees of freedom, change - decrease this to increase the frequency of extreme values
deficit = 4.3e9  # Deficit 4.3 billion from reference
years_to_pay_off = 10  # Years over which to pay off the deficit

# Generate random t-distribution values for Year 0
X_0 = np.random.standard_t(df, size=n) * std_dev_cost + mean_cost

total_cost_0 = np.sum(X_0)
C_0 = total_cost_0 + deficit / years_to_pay_off

# Print the initial value of C_0
print(f"C_0 (Year 0 budget): {C_0:.2f}")

# Use recursion to calculate C_1 through C_10
C_previous = C_0

for year in range(1, 11):
    # Generate random t-distribution values for the current year (X_i's)
    X_current = np.random.standard_t(df, size=n) * std_dev_cost + mean_cost
    
    # Calculate the total cost for the current year (sum of X_i's)
    total_cost_current = np.sum(X_current)
    
    # Calculate C_t using the recurrence relation
    C_current = C_previous + total_cost_current
    
    # Print the budget for the current year
    print(f"C_{year} (Year {year} budget): {C_current:.2f}")
    
    # Update C_previous for the next iteration
    C_previous = C_current
