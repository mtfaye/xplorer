"""Groupby functions.
"""

import pandas as pd 


def gbyone(df, i):
    """ Calculates groupby functions of one given categorical column with all the numerical column of dataframe.
    Args: df = dataframe, 
           i = column name in string - categotical column only. 
    Returns: Dataframe
    """
    return df.groupby(i).mean()


def gbytwo(df, v, x):
    """ Calculates groupby functions of two given categorical column with all the numerical column of dataframe.
    Args: df = dataframe, 
          v, x = column name in string categorical column only. 
    Returns: Dataframe
    """
    return df.groupby([v, x]).mean()
   

def gbyselectnum(df, y, z):
     """ Calculates groupby functions of one given categorical column with one given numerical column.
    Args: df = dataframe, 
          y = column name in string categorical column only. 
          z = column name in string numerical column only.
    Returns: Dataframe
    """
    return df.y.groupby(z).mean()
