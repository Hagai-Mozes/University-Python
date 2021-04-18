''' Exercise #5. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def reverse_string(s):
    if len(s)==1:
        return s
    else:
        return s[-1]+reverse_string(s[:-1])


#########################################
# Question 2 - do not delete this comment
#########################################
def find_maximum(lst):
    if len(lst)==0:
        return -1
    else:
        if lst[-1]>find_maximum(lst[:-1]):
            return lst[-1]
        else:
            return find_maximum(lst[:-1])
        

#########################################
# Question 3 - do not delete this comment
#########################################
def is_palindrome(s):
    if len(s)<2:
        return True
    else:
        return s[0]==s[-1] and is_palindrome(s[1:-1])

#########################################
# Question 4 - do not delete this comment
#########################################
def climb_combinations(n):
    if n<3:
        return n
    else:
        return climb_combinations(n-1)+climb_combinations(n-2) 

#########################################
# Question 5 - do not delete this comment
#########################################
def is_valid_paren(s, cnt=0):
    if cnt==-1 or (len(s)==0 and cnt>0):
        return False
    elif len(s)==0:
        return True
    else:
        if s[0]=='(':
            cnt+=1
        elif s[0]==')':
            cnt-=1
        return True and is_valid_paren(s[1::], cnt)

#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################

print(reverse_string("abc") == 'cba')
print(reverse_string("Hello!") == '!olleH')

print(find_maximum([9,3,0,10]) == 10)
print(find_maximum([9,3,0]) == 9)
print(find_maximum([]) == -1)

print(is_palindrome("aa") == True)
print(is_palindrome("aa ") == False)
print(is_palindrome("caca") == False)
print(is_palindrome("abcbbcba") == True)

print(climb_combinations(3) == 3)
print(climb_combinations(10) == 89)

print(is_valid_paren("(.(a)(") == False)
print(is_valid_paren("p(()r((0)))()") == True)

# ============================== END OF FILE =================================
