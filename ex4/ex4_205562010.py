''' Exercise #4. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def second_most_popular_character(my_string):
    char_dict = {}
    for char in my_string.lower():
        char_dict[char] = char_dict.get(char,0) +1
    sorted_chars = sorted(char_dict)
    sorted_chars.sort(key=char_dict.get, reverse=True)
    for i in sorted_chars:
        if char_dict[i]< char_dict[sorted_chars[0]]:
            return i


#########################################
# Question 2 - do not delete this comment
#########################################
def diff_sparse_matrices(lst):
    new_dic = lst[0]
    for dic in lst[1::]:
        for key in dic.keys():
            new_dic[key] = new_dic.get(key,0)-dic[key]
            if new_dic[key]==0:
                new_dic.pop(key)
    return new_dic


#########################################
# Question 3 - do not delete this comment
#########################################
def find_substring_locations(s, k):
    my_dic={}
    for i in range(len(s)-k+1):
        my_str = s[i:i+k]
        val = my_dic.get(my_str,[])
        val.append(i)
        my_dic[my_str]=val
    return my_dic


#########################################
# Question 4 - do not delete this comment
#########################################
def count_lines(in_file, out_file):
    count_l = 0
    in_file = open(in_file,'r')
    out_file = open(out_file, 'w')
    for i in in_file:
        count_l +=1
    out_file.write(str(count_l))
    in_file.close()
    out_file.close()
             
#########################################
# Question 5 - do not delete this comment
#########################################
def simple_sent_analysis(in_file):
    try:
        f=open(in_file,'r')
    except IOError:
        print("Cannot encode",in_file, "due to IO error")
        return {}
    my_dic = {'happy':0,'sad':0}
    for line in f:
        for x in '!?, -.%$;':
            line = line.replace(x,' ')
        lst_words = line.split()
        for word in lst_words:
            if word.lower()=="happy":
                my_dic["happy"]+=1
            if word.lower()=="sad":
                my_dic["sad"]+=1
    f.close()
    return my_dic


#########################################
# Question 6 - do not delete this comment
#########################################
def calc_profit_per_group(in_file):
    try:
        f=open(in_file,'r')
        my_dic={}
        my_names=[]
        for line in f:
            cur_ser = line.split(",")
            if (len(cur_ser) !=3):
                f.close()
                raise ValueError ('Invalid input')
            genre = cur_ser[2].strip()
            try:
                profit = float(cur_ser[1])
            except ValueError:
                f.close()
                raise ValueError('Invalid input') from None
            ser_name = cur_ser[0].strip()
            if ser_name in my_names:
                f.close()
                raise ValueError ('The series '+ ser_name+' appears more than once.')
            if (not(genre == "neutral" or genre == "sad" or genre == "happy")):
                f.close()
                raise ValueError ('Invalid input')
            my_dic[genre]=my_dic.get(genre,[])
            my_dic[genre].append(profit)
            my_names.append(ser_name)
        for key in my_dic.keys():
            my_dic[key]=sum(my_dic[key])/len(my_dic[key])
        for key in "neutral","sad","happy":
            my_dic[key] = my_dic.get(key,'NA')
        f.close()
        return my_dic
    except IOError:
        print("Cannot use",in_file, "due to IO error")
    

#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

# ============================== END OF FILE =================================
