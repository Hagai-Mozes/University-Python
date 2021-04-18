""" Exercise #9. Python for Engineers."""
from builtins import slice

import pandas as pd
import numpy as np
import imageio
import matplotlib.pyplot as plt


#########################################
# Question 1 - do not delete this comment
#########################################
from setuptools.command.rotate import rotate


def load_training_data(filename):
    f=open(filename,'r')
    my_lst = []
    for line in f:
        line=line.strip("\n")
        line=line.split(',')
        my_lst.append(line)
    my_data = np.array(my_lst)
    data = my_data[1::, 1::]
    data=np.array(data,dtype='float')
    column_names=my_data[0,1::]
    row_names=my_data[1::,0]
    f.close()
    return data, column_names,row_names

def get_highest_weight_loss_trainee(data, column_names, row_names):
    max_loss = np.argmax(data[::,0]-data[::,len(data[0])-1])
    return row_names[max_loss]



def get_diff_data(data, column_names, row_names):
    diff_array=np.zeros(data.shape)
    diff_array[:,1:]=data[:, 1:]-data[::, :len(data[0])-1]
    return diff_array

def get_highest_loss_month(data, column_names, row_names):
    my_diff=get_diff_data(data, column_names, row_names)
    max_diff = np.argmin(my_diff.sum(axis=0))
    return column_names[max_diff]




def get_relative_diff_table(data, column_names, row_names):
    my_diff=get_diff_data(data, column_names, row_names)
    rel_diff =np.zeros(data.shape)
    rel_diff[:,1:]=my_diff[:,1:]/data[:,:len(data[0])-1]
    return  rel_diff


#########################################
# Question 2 - do not delete this comment
#########################################


def read_missions_file(file_name):
    try:
        df=pd.read_csv(file_name)
        row_names=df['Kingdom']
        df=df.drop('Kingdom', 1)
        df1=df.set_index(row_names)
    except IOError:
        raise IOError ("An IO error occurred")
    return df1




def sum_rewards(bounties):
    return sum(bounties['Bounty']-bounties['Expenses'])


def find_best_kingdom(bounties):
    return pd.Series.idxmax((bounties['Bounty']-bounties['Expenses'])/bounties['Duration'], axis=1)


#########################################
# Question 3 - do not delete this comment
#########################################

def compute_entropy(img):
    im=imageio.imread(img)
    n_hist=np.zeros(len(im[0,:]+1))
    for i in im:
        n_hist+=(np.bincount(i, minlength=len(im[0,:]+1)))
    n_hist=n_hist/im.size
    #n_hist=np.nan_to_num(n_hist)
    n_hist=n_hist[n_hist!=0]
    s=0
    for p in n_hist:
        s-=(p*np.log2(p))
    return s

def nearest_enlarge(img, a):
    im = imageio.imread(img)
    x,y=im.shape
    n_im = np.zeros((x*a,y*a))
    for i in range(x*a):
        for j in range(y*a):
            n_x,n_y=int(np.floor(i/a)), int(np.floor(j/a))
            n_im[i,j]=im[n_x,n_y]
    return n_im