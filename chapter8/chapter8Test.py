# Answers at https://docs.google.com/forms/d/e/1FAIpQLSfBf5BqDX7FqSq6_6yAen0mZyP48U_geCWRJL0PWgomqrATuA/viewscore?viewscore=AE0zAgCGVkTzdp8Lxqk0YasibyYSihyFSjRServWOs3Sj0bHf9OTCFQhpOAwzZxB_A

# def blue_fairy():
#  return "Always let your conscience be your guide"

# print(blue_fairy())


# blue_fairy():
# def blue_fairy():
#    print("Always let you conscience be your guide")
# Error, not sure why yet

# def rafiki(lion):
#    print(lion+" "+
#    "Oh yes, the past can hurt. "+
#        "But the way I see it, "+ 
#        "you can either run from it or learn from it")

# rafiki("Simba")

# def dory(fish, minutes_since_last_talked):
#    if minutes_since_last_talked>10:
#        print("Who are you?", end=" ")
#    else:
#        if fish=="Nemo":
#            print("Just keep swimming", end=" ")
#        else:
#            print("I don't know you", end=" ")

# print(dory("Nemo", 90))
# The answer will be Who are you? None
# It only goes through first line of function
# and since print() returns none, that is what it will print 

# def emperor(word_a, word_b):
#    my_string=("The +word_b+ that blooms " +
#        "in adversity is the most " +
#        "rare and +word_a+ of all.")
#    return my_string
# word_1='flower'
# word_2='beautiful'
# print(emperor(word_b=word_1, word_a=word_2))
# Only the string will be printed, because the definitions that appear afterwords have not been called

# def see_character(name, age, species="human"):
#    print(name, age, species)

# see_character("Ariel", 16, "mermaid")

# x=5
# def some_func(x):
#     print(x, end=" ")
# print(x, end=" ")
# some_func(1)
# x = x-1
# print(x, end=" ")
# some_func(1)
# It will return 5 1 4 1

# def fun_a(number):
#     return number+5

# def fun_b(number):
#     return number*2
# print(fun_a(fun_b(5)))
# Will return 15,  which I don't understand why.
# I thought it would multiply them

def do_somethin(a_list):
    my_string=""
    for element in a_list:
        my_string+=element[0]
    return my_string
aladdin_characters=["Jasmine","Aladdin","Fazahl", "Abu", "Razoul"]
print(do_somethin(aladdin_characters))