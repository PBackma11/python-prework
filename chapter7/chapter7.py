# The while loop
# while Boolean or boolean expression:
    #code block
    #to run while
    #condition is true


# You must be over 5 feet to ride my ride
# I have a magic potion lets you grow an inch every time

height=int(input("What is your height in inches? "))
while height<60:
    height+=1
    if height<58:
        continue
    print(f"You are {height} inches tall \n and too short to ride!")
    print("Did you take my magic potion")
    if height==58:
        break
    
print("Thanks for coming")

while True:
    response = input("what do yo wnat to do? Say hi[h], say goodbye[g], or Quit[q]?")
    if response.lower() == "h":
        print("hello")
    elif response.lower()=="g":
        print("goodbye")
    elif response.lower()=="q":
        break
    else:
        print("invalid Option")


