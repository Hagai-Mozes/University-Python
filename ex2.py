""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################

a = 8  # Replace the assignment with a positive integer to test your code.
A = [12,4,0,8]  # Replace the assignment with other lists to test your code.

for i in A:
    if i%a == 0:
        print(A.index(i))
        break
else:
    print(-1)
        



# End of code for question 1

#########################################
# Question 2 - do not delete this comment
#########################################
B = ['hello', 'world', 'course', 'python', 'day','']
# Replace the assignment with other lists of strings (str) to test your code.

# Write the code for question 2 using a for loop below here.
sum_len = 0
longer_num = 0
for i in B:
    sum_len += len(i)
ave_len = sum_len/len(B)
for i in B:
    if len(i) > ave_len:
        longer_num += 1
print("The number of strings longer than the average is:", longer_num)
        

# Write the code for question 2 using a while loop below here.
sum_len = 0
longer_num = 0
my_str = ""
i=0
j=0
while i<(len(B)):
    my_str = B[i]
    sum_len += len(my_str)
    i +=1
ave_len = sum_len/len(B)

while j<(len(B)):
    my_str = B[j]
    if len(my_str)>ave_len:
        longer_num +=1
    j+=1
print("The number of strings longer than the average is:", longer_num)

# Write the rest of the code for question 2 below here.



# End of code for question 2

#########################################
# Question 3 - do not delete this comment
#########################################

C = [0]  # Replace the assignment with other lists to test your code.


# Write the rest of the code for question 3 below here.
pro_sum = 0
i = 0
if len(C) == 1:
    pro_sum = C[0]
else:
    while i < (len(C)-1):
        pro_sum += C[i]*C[i+1]
        i+=1
print (pro_sum)

# End of code for question 3


#########################################
# Question 4 - do not delete this comment
#########################################

D = [1, 3,80,-80]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 4 below here.
new_lst = D[0:2]
my_diff = abs(D[1]-D[0])
for i in D[2::]:
    if abs(i-new_lst[-1]) > my_diff:
        my_diff = abs(i-new_lst[-1])
        new_lst.append(i)
print(new_lst)

# End of code for question 4

#########################################
# Question 5 - do not delete this comment
#########################################

my_string = 'hfhbhffhfh'  # Replace the assignment with other strings to test your code.
k = 2  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.

for i in my_string:
    if my_string.find(i*k) > -1:
        print ("For length %s, found the substring %s!"%(k,i*k))
        break
else:
    print ("Didn't find a substring of length",k)

# End of code for question 5
