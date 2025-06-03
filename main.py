import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('data.csv')

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Population'], marker='o')
plt.title('World Population Growth')
plt.xlabel('Year')
plt.ylabel('Population (Billions)')
plt.grid(True)

# Save the plot
plt.savefig('population_growth.png')
plt.show()
