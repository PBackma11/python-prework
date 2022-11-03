# Question 1
# # Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):

user="perry backman"
hello="Hello, " + user
print(hello.title()+"!")


# # Question 2
# # Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

odd_numbers = list(range(1, 101, 2))
print(odd_numbers)


# # Question 3
# # Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):

num=[11,52,19,1003]
print(max(num))


# # Question 4
# # Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):

year=int(input('Enter Year: '))

if (year%4==0 and year%100!=0) or (year%400==0):
     True
     print(year, "is a leap year.")
else:
     False
     print(year, "is not a leap year.")


# Question 5
# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

list1=[2, 10, 7, 6, 5, 8, 2, 6]

print(list1)
for i in range(0, len(list1)-1):
    if list1[i]+1 == list1[i+1]:
        True
        print("the list has consecutive numbers")
    else:
        False
        print("the list does not have consecutive numbers.")
        
