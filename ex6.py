''' Exercise #6. Python for Engineers.'''

#########################################
# Question 1.a - do not delete this comment
#########################################
def four_bonacci_rec(n):
    if n<=3:
        return n
    return four_bonacci_rec(n-4)+four_bonacci_rec(n-3)+four_bonacci_rec(n-2)+four_bonacci_rec(n-1)


#########################################
# Question 1.b - do not delete this comment
#########################################
def four_bonacci_mem(n, memo=None):
    if n<=3:
        return n
    if memo==None:
        memo={}
    if n not in memo:
        memo[n]=four_bonacci_mem(n-4,memo)+four_bonacci_mem(n-3,memo)+four_bonacci_mem(n-2,memo)+four_bonacci_mem(n-1,memo)
    return memo[n]

#########################################
# Question 2 - do not delete this comment
#########################################
def climb_combinations_memo(n, memo=None):
    if n<3:
        return n
    if memo==None:
        memo={}
    if n not in memo:
        memo[n]= climb_combinations_memo(n-1,memo)+climb_combinations_memo(n-2,memo)
    return memo[n]


#########################################
# Question 3 - do not delete this comment
#########################################
def catalan_rec(n,memo=None):
    if n<2:
        return 1
    if memo==None:
        memo={}
    cat_n=0
    if n not in memo:
        for i in range(0,n):
            cat_n += catalan_rec(n-i-1,memo)*catalan_rec(i,memo)
        memo[n]=cat_n
    return memo[n]
    

#########################################
# Question 4.a - do not delete this comment
#########################################
def find_num_changes_rec(n, lst):
    if n==0:
        return 1
    if len(lst)==0 or n<0:
        return 0
    sum_op=0
    cur_co=lst[0]
    while cur_co <= n:
        sum_op+=find_num_changes_rec(n-cur_co, lst[1::])
        cur_co+=lst[0]
    return sum_op+find_num_changes_rec(n, lst[1::])
    

#########################################
# Question 4.b - do not delete this comment
#########################################
def find_num_changes_mem(n, lst, memo=None):
    if n==0:
        return 1
    if len(lst)==0 or n<0:
        return 0
    if memo == None:
        memo={}
    sum_op=0
    cur_co=lst[0]
    if (n,tuple(lst)) not in memo:
        while cur_co <= n:
            sum_op+=find_num_changes_mem(n-cur_co, lst[1::], memo)
            cur_co+=lst[0]
        memo[(n,tuple(lst))]=sum_op
    return memo[(n,tuple(lst))]+find_num_changes_mem(n, lst[1::], memo)


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################


#Question 1.a tests - you can and should add more    
print(four_bonacci_rec(0) == 0)
print(four_bonacci_rec(5) == 12)
print(four_bonacci_rec(8) == 85)

#Question 1.b tests - you can and should add more    
print(four_bonacci_mem(0) == 0)
print(four_bonacci_mem(5) == 12)
print(four_bonacci_mem(8) == 85)

#Question 2 tests - you can and should add more    
print(climb_combinations_memo(4) == 5)
print(climb_combinations_memo(42) == 433494437)

#Question 3 tests - you can and should add more    
cat_list = [1,1,2,5,14,42,132,429]
for n,res in enumerate(cat_list):
    print(catalan_rec(n) == res)

#Question 4.a tests - you can and should add more        
print(find_num_changes_rec(5,[1,2,5,6]) == 4)
print(find_num_changes_rec(4,[1,2,5,6]) == 3)
print(find_num_changes_rec(-1,[1,2,3,4]) == 0)
#Question 4.b tests - you can and should add more        
print(find_num_changes_mem(5,[1,2,5,6]) == 4)
print(find_num_changes_mem(4,[1,2,5,6]) == 3)
print(find_num_changes_mem(5,[2,1,5,6]) == 4)

# ============================== END OF FILE =================================
