"""Utility functions for data visualization."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
plt.rcParams.update({'figure.max_open_warning': 0})



def hist(num, dir_path):
    """Writes png files for each value.
    Args : 
        num = pandas datafram of numerical columns only. 
        dir_path = directory for saved files in string. 
    Returns : 
        png files on dir_path
    """
    print('Writing graphs images...')
    for col in num.columns:
        sns.set()
        fig, ax = plt.subplots()
        sns.set(style="whitegrid")
        sns.distplot(num[col])
        fig.set_size_inches(22,14)
        plt.savefig(dir_path/'{}'.format(col), bbox_inches='tight')
    print('Done.')


def bar(cat, dir_path):
    """Writes png files for each value.
    Args : 
        cat = pandas datafram of categorical columns only. 
        dir_path = directory for saved files in string. 
    Returns : 
        png files on dir_path
    """
    for col in cat.columns:
        sns.set()
        fig, ax = plt.subplots()
        sns.set(style="whitegrid")
        sns.countplot(x=col, data=cat, palette='Blues_d')
        fig.set_size_inches(22,14)
        plt.savefig(dir_path/'{}'.format(col), bbox_inches='tight')
    print('Done.')
    
    
def filter_five(cat, dir_path):
    """Writes png files for each value.
    Args : 
        cat = pandas datafram of categorical columns only. 
        dir_path = directory for saved files in string. 
    Returns : 
        png files on dir_path
    """ 
    for col in cat.columns:
        sns.set()
        fig, ax = plt.subplots()
        sns.set(style="whitegrid")
        sns.countplot(x=col, data=cat, order=pd.value_counts(cat[col]).iloc[:5].index, palette='Blues_d')
        fig.set_size_inches(22,14)
        plt.savefig(dir_path/'{}'.format(col), bbox_inches='tight')
    print('Done.')
    
    
def filter_eight(cat, dir_path):
    """Writes png files for each value.
    Args : 
        cat = pandas datafram of categorical columns only.
        dir_path = directory for saved files in string. 
    Returns : 
        png files on dir_path
    """ 
    for col in cat.columns:
        sns.set()
        fig, ax = plt.subplots()
        sns.set(style="whitegrid")
        sns.countplot(x=col, data=cat, order=pd.value_counts(cat[col]).iloc[:8].index, palette='Blues_d')
        fig.set_size_inches(22,14)
        plt.savefig(dir_path/'{}'.format(col), bbox_inches='tight')
    print('Done.')
      
      
def filter_ten(cat, dir_path):
    """Writes png files for each value.
    Args : 
        cat = pandas datafram of categorical columns only. 
        dir_path = directory for saved files in string. 
    Returns : 
        png files on dir_path
    """ 
    for col in cat.columns:
        sns.set()
        fig, ax = plt.subplots()
        sns.set(style="whitegrid")
        sns.countplot(x=col, data=cat, order=pd.value_counts(cat[col]).iloc[:10].index, palette='Blues_d')
        fig.set_size_inches(22,14)
        plt.savefig(dir_path/'{}'.format(col), bbox_inches='tight')
    print('Done.')


def plotSimplecorr(simple_corr, dir_path):
    '''Plots a graphical correlation matrix for each pair of numerical columns in the dataframe.
    Args: df = pandas DataFrame.
    '''
    fig, ax = plt.subplots(figsize=(22,14))
    sns.heatmap(simple_corr, annot=True, ax=ax)
    plt.savefig(dir_path/'Correlation.png', bbox_inches='tight')
    print('Done.')
