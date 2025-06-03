import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')


plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Population'], marker='o')
plt.title('World Population Growth')
plt.xlabel('Year')
plt.ylabel('Population (Billions)')
plt.grid(True)


plt.savefig('population_growth.png')
plt.show()
