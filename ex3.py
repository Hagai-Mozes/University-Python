''' Exercise #3. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def sum_divisible_by_k(lst, k):
    my_sum = 0
    for i in lst:
        if i%k==0:
            my_sum +=i
    return my_sum  # replace this with your implementation


#########################################
# Question 2 - do not delete this comment
#########################################
def mult_odd_digits(n):
    my_pro = 1
    while n !=0:
        if n%2 == 1:
            my_pro *= n%10
        n = n//10
    return my_pro

            # replace this with your implementation


#########################################
# Question 3 - do not delete this comment
#########################################
def count_longest_repetition(s, c):
    my_count=0
    cur_count=0
    for i in s:
        if i==c:
            cur_count+=1
        else:
            cur_count=0
        my_count = max(my_count,cur_count)
    return my_count

# replace this with your implementation


#########################################
# Question 4 - do not delete this comment
#########################################
def upper_strings(lst):
    if type(lst)==list:
        for i in range(0,len(lst)):
            if type(lst[i]) == str:
                lst[i] = str.upper(lst[i])
    else:
        return -1
        
    # replace this with your implementation


#########################################
# Question 5 - do not delete this comment
#########################################
def div_mat_by_scalar(mat, alpha):
    new_mat = []
    for i in range(0,len(mat)):
        new_mat.append([])
        for j in mat[i]:
            new_mat[i].append(j//alpha)
    return new_mat

      # replace this with your implementation


#########################################
# Question 6 - do not delete this comment
#########################################
def mat_transpose(mat):
    mat_t = []
    for i in range(0,len(mat[0])):
        mat_t.append([])
        for j in range(0,len(mat)):
            mat_t[i].append(mat[j][i])
    return mat_t

      # replace this with your implementation

