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


import matplotlib.pyplot as plt
students = ["Vikky","Rahul","Aman","Neh"]
marks = [85,90,78,95]
plt.bar(students, marks,width=0.6)
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()


#Horizontal Bar Chart
plt.barh(students,marks)
plt.show()


#Multiple Bar Chart
students = ["A", "B", "C", "D"]
python = [80,70,90,60]
java = [70,75,85,80]
import numpy as np
x = np.arange(len(students))
width = 0.35
plt.bar(x - width/2, python, width, label="Python)
plt.bar(x + width/2, java, width, label="Java")
plt.xticks(x, students s)
plt.legend()
plt.show()


import matplotlib.pyplot as plt
subjects = ["AI","Pyhton","Java","SQL"]
hours = [35,25,20,20]
explode = [0.1,0,0,0]
mycolours ["Red", "hotpink", "b", "#4CAF50"]
plt.pie(hours,
labels=subjects,
autopct="%1.1f%%", #Percentage in Pie Chart
explode=explode, #Explode Pie Chart
shadow = True, #add shadow
colors = mycolors #add colors
)
plt.title("Study Time")
plt.legend()
plt.show()


