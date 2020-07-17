import pandas as pd 

df = pd.DataFrame(dict(A=['coke', 'sprite', 'coke', 'sprite',
                          'sprite', 'coke', 'coke'],
                       B=['alpha','gamma', 'alpha', 'beta',
                          'gamma', 'beta', 'beta'],
                       col_1=[1,2,3,4,5,6,7],
                       col_2=[1,6,2,4,7,9,3]))

def groupbyHelper(df, v, x, y, z):
    """ Calculates 2x2 groupby functions of four given column.
    Args:
    Column name in string.
    Returns:
    Dataframe
    """
    df_groupby = df[[v, x]].groupby([y, z]).mean()
    return df_groupby

groupbyHelper(df, 'A', 'B', 'col_1', 'col_2')

