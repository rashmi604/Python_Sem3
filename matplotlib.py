pip install matplotlib #in terminal
import matplotlib.pyplot as plt


#MY FIRST GRAPH
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,15,30,25]
plt.plot(x, y)
plt.show()


#Second plot(Monthly Sales)
import matplotlib.pyplot as plt
months = ["Jan","Feb","Mar","Apr","May"]
sales = [100,150,120,180,200]
plt.plot(months, sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


#Change Line Style
plt.plot(
    months,
    sales,
    color="red",
    linestyle="--",
    linewidth=2,
    marker="o"
)


import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]

sales_2025 = [100, 150, 120, 180, 220]
sales_2026 = [120, 170, 160, 200, 250]

plt.plot(months, sales_2025, marker="o")
plt.plot(months, sales_2026, marker="s")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend(["2025", "2026"]) # Note: corrected from plt.legend("center") for proper labeling
plt.show()