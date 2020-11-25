"""Groupby functions.
"""

import pandas as pd 


def gbOne(df, i):
    """ Calculates groupby functions of one given categorical column with all the numerical column of dataframe.
    Args: df = dataframe, 
           i = column name in string - categotical column only. 
    Returns: Dataframe
    """ 
    return df.groupby(i).agg(['min','mean', 'max','count'])

def gbTwo(df, x, y):
    """ Calculates groupby functions of two given categorical column with all the numerical column of dataframe.
    Args: df = dataframe, 
          x, y = column name in string categorical column only. 
    Returns: Dataframe
    """
    return df.groupby([x, y]).agg(['min','mean', 'max','count'])
  

def gbOnebyOne(df, x, y):
    """ Calculates groupby functions of one given categorical column and one given numerical column.
    Args: df = dataframe, 
           x = column name in string categorical column only. 
           y = column name in string numerical column only.
    Returns: Dataframe
    """
    return df.groupby(x)[y].agg(['min','mean', 'max','count'])


def gbTwobyTwo(df, v, x, y, z):
    """ Calculates groupby functions of two given categorical column and two given numerical columns.
    Args: df = dataframe, 
           v, x = columns name in string categorical column only. 
           y, z = columns name in string numerical column only.
    Returns: Dataframe
    """
    return df.groupby([v, x])[y, z].agg(['min','mean', 'max','count'])
    