# # print("Hello World !")
# # print("I am learning Python.")
# # print("It is awesome!")

# # x = 4 
# # y = "Sally"
# # z = "3.5"

# # print(x)
# # print(y)
# # print(z)

# # fruits = ["apple", "banana", "cherry"]
# # x,y,z = fruits
# # print(x)
# # print(y)
# # print(z)

# # x1 = "Hello World"
# # x2 = 20
# # x7 = range(5)

# #Integers
# x= int(1)
# y = int(2.8)
# z= int("3")
# print(x,y,z)
# print(type(x))
# print(type(y))
# print(type(z))


# #Floats:
# x=float(1)
# y=float(2.8)
# z=float("3")
# w=float("4.2")
# print(x,y,z)
# print(type(x))
# print(type(y))
# print(type(z))


# x=15
# y=4

# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y)
# print(x**y)
# print(x//y)

# # x=5
# # x=x+3
# # x=x-3
# # x=x*3
# # x=x/3
# # x=x%3
# # x=x//3
# # x=x**3
# # x=x&3
# # x=x|3
# # x=x^3
# # x=x>>3
# # x=x<<3


# x=5
# y=3

# print(x==y)
# print(x!=y)
# print(x>y)
# print(x<y)
# print(x>=y)
# print(x<=y)


#Print the grades of 5 subjects percentage if 90% or greater print A, if  75% or greater print B,if  60% or greater print C,
# if  45% or greater print D, else everything F

# Simple beginner-friendly approach without loops or lists

sub1 = float(input("Enter marks for subject 1: "))
sub2 = float(input("Enter marks for subject 2: "))
sub3 = float(input("Enter marks for subject 3: "))
sub4 = float(input("Enter marks for subject 4: "))
sub5 = float(input("Enter marks for subject 5: "))

# Calculate average percentage directly
percentage = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 45:
    print("Grade: D")
else:
    print("Grade: F")

