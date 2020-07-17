import pandas as pd 

def groupbyHelper(df, v, x, y, z):
    """ Calculates 2x2 groupby functions of four given column.
    Args:
    Column name in string.
    Returns:
    Dataframe
    """
    if v == None:  
        df[x].groupby([y, z]).mean()
    elif v and y == None:
        df[x].groupby(z).mean()
    elif v and z == None:
        df[x].groupby(y).mean()
    elif x == None
        df[v].groupby([y, z]).mean()
    elif x and y == None:
        df[v].groupby(z).mean()
    elif x and z == None:
        df[v].groupby(y).mean()
    elif x == None:
        df[v].groupby([y, z]).mean()
    elif y == None:
        df[v, x].groupby(z).mean()
    elif z == None:
        df[[v, x]].groupby(y).mean()
    else:
        df_groupby = df[[v, x]].groupby([y, z]).mean()
        
    return df_groupby
        
        
        

