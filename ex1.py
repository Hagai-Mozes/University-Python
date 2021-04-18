
''' Exercise #1 - Python.'''

#########################################
# Question 1 - do not delete this comment
#########################################
R = 5 # Replace ??? with a positive float of your choice.
# Write the rest of the code for question 1 below here.
pi = 3.14
my_diam = 2*R
my_circ = my_diam*pi
my_area = (R**2)*pi
print("Diameter is:", my_diam)
print("Circumference is:", my_circ)
print("Area is:", my_area)



#########################################
# Question 2 - do not delete this comment
#########################################
S = "Hello, dear world!" # Replace ??? a string of your choice.
# Write the rest of the code for question 2 below here.
l = len(S)
if l > 10:
    print(S[:10].lower() + S[10::].upper())
else:
    print("$"+S[1:-1]+"@")



#########################################
# Question 3 - do not delete this comment
#########################################
number  = -354686 # Replace ??? with a int of your choice.
# Write the rest of the code for question 3 below here.
is_even = not bool(number%2)
str_result = ["odd", "even"]
print("I am",number,"and I am",str_result[is_even])



#########################################
# Question 4 - do not delete this comment
#########################################
a = 9 # Replace ??? with a positive int of your choice.
b = 5  # Replace ??? with a positive int of your choice.
c = 5  # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 4 below here.
cur_result = (a+b)**(1/c)
print (F"{cur_result:.5f}")
cur_result = (a**b)**(1/c)
print (F"{cur_result:.5f}")
cur_result = (a/b)-(b/c)
print (F"{cur_result:.5f}")


#########################################
# Question 5 - do not delete this comment
#########################################
year = 1900 # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 5 below here.
is_leap = False
str_leap = ["is not","is"]
if (year%4 == 0 and year%100 != 0) or year%400 ==0:
    is_leap = True
print(F"{year} {str_leap[is_leap]} a leap year")
