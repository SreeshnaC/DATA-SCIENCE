import matplotlib.pyplot as plt

with open("3_data.txt") as f:
    data = f.read().strip().split('\n')

x = [float(row.split()[0]) for row in data if row.strip()]
y = [float(row.split()[1]) for row in data if row.strip()]

# Plotting
plt.plot(x, y, marker='o', linestyle='-')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line Graph from File Data')
plt.grid(True)
plt.show()
