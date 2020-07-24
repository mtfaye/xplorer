"""Utility fonctions for statistical description of datasets.
"""

import numpy as np
import pandas as pd
import pyodbc



def read_csv(filepath, chunksize):
    """Takes csv files and returns a pandas dataframe.
    Args: filepath = Path of the csv file in string.
          chunksize = number or rows selected for the reading iterator, in integer. 
    Returns: 
           Pandas dataframe.
    """ 
    print('Reading data...')
    reader = pd.read_csv(filepath, sep='|', chunksize=chunksize, iterator=True)  
    return pd.concat(reader, ignore_index=True)
    

def read_sql(server, database, username, password):
    """Read tables from a remote sql database and returns a pandas dataframe.
    Args: server, database, username, password = all in string.
    Returns: 
           Pandas dataframe.
    
    """        
    con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+
                            ';DATABASE='+database+
                            ';UID='+username+
                            ';PWD='+password)
    query = 'SELECT * FROM dwh.Dim_Canal_can'
    sql_df = pd.read_sql_query(query,con)
    return sql_df


def processed_df(df):
    """Removes weird characters from column names.
    Args: Pandas dataframe. 
    Returns: 
           Pandas dataframe.
    """
    print('Computing stats...')
    df.columns = df.columns.str.strip().str.replace('/', '_').str.replace('(', '').str.replace(')', '')
    return df


def num(df):
    """Returns dataframe object with numerical columns only.
    Args: Pandas dataframe. 
    Returns: 
           Pandas dataframe.    
    """
    num_df = [col for col in df.columns if df[col].dtype != 'object']
    return df[num_df]

    
def cat(df):
    """Returns dataframe object with categorical columns only. 
    Args: Pandas dataframe. 
    Returns: 
           Pandas dataframe.
    """
    cat_df = [col for col in df.columns if df[col].dtype == 'object']
    return df[cat_df]


def summary(df, num, cat):
    """ Resumes the dataset.
    Args: df, num and cat are all Pandas dataframe. 
    Returns: 
           Pandas dataframe.
    """
    _dict = [{'Rows': df.shape[0], 
             'Variables': df.shape[1],
             'Numerical': len(num.columns), 
             'Categorical': len(cat.columns), 
             'Missing': df.isnull().sum().sum(),
             '% of Missing': df.isnull().sum().sum() / len(df)}]
    return pd.DataFrame(_dict)


def stats(df):
    """ Takes a dataframe object and returns a dpd Data Profile (Dataframe).
    Args: df = Pandas dataframe. 
    Returns: 
           Pandas dataframe.
    """
    dpd = pd.DataFrame(index=np.arange(0, len(df.columns)), 
                       columns=('column_name', 
                                'col_data_type', 
                                'unique_values_count', 
                                'non_unique_values_count',
                                'non_null_values'))
    
    for ind, cols in enumerate(df.columns):
        dpd.loc[ind] = [cols, df[cols].dtype,
                         df[cols].nunique(),
                         df.shape[0] - df[cols].nunique(),
                         df[cols].count()
                         ]
    dpd['%_of_non_nulls'] = (dpd['non_null_values'] / df.shape[0]) * 100 
    dpd['null_values'] = df.shape[0] - dpd['non_null_values']
    dpd['%_of_nulls'] = 100 - dpd['%_of_non_nulls']
    desc = df.describe().T.round(2)
    dpd = pd.merge(dpd, desc, how='left', left_on='column_name', right_index=True)
    return dpd

 
def duplicates(df):
    """Returns a dataframe with dupilcated rows.
    Args: df = Pandas dataframe. 
    Returns: 
           Pandas dataframe.
    """
    dup_bool = df.duplicated(subset=None, keep='first')
    return df.loc[dup_bool == True]

   
def log_num(df):
    """Returns a log values of a pandas series
    args: df = pd dataframe
    """
    return np.log10(df)    


def sampling(df, ss):
    """Sampling the dataset
    Arg: df = Dataframe 
         ss = sample size in Integer
    return: dataframe size of the sampling.
    """
    return df.sample(ss)

    
def simple_corr(df):
    """Takes a dataframe a return table of pearson correlation between numerical variables.
    Args: dataframe
    returns: dataframe
    """
    return df.corr(method='pearson')


def enCoder(df):
    """Encodes all categorical variables.
    Args: dataframe
    return: dataframe
    """
    return pd.get_dummies(df, columns=None, drop_first=True)
    
    
def correlor(df, col, k):
    """Takes the 10 highest corr coeff of a choson variable col. 
    args: dataframe of encoded variables, col : chosen of target variable (string), k : treshold (int)
    return : dataframe
    """
    c = df.corr().nlargest(k, col)[col].index
    return df[c].corr().round(2)
     
     
def toExcel(summary, stats, duplicates, simple_corr, correlor, dir_path):
    """Takes df and writes excel file to a specific directory.
    """  
    print('Writing report...')    
    writer = pd.ExcelWriter(dir_path/'your_report.xlsx', engine='xlsxwriter' )
    workbook = writer.book
    worksheet = workbook.add_worksheet('Report')
    writer.sheets['Report'] = worksheet
    worksheet.write_string(0, 0, 'Summary')
    summary.to_excel(writer,
                      sheet_name = 'Report', 
                      startrow=1, 
                      startcol=0)
    worksheet.write_string(summary.shape[0] + 4, 0, 'Stats')
    stats.to_excel(writer,
                    sheet_name = 'Report',
                    startrow=summary.shape[0] + 5,
                    startcol=0)
    worksheet.write_string(stats.shape[0] + 9, 0, 'Duplicates')
    duplicates.to_excel(writer, 
                        sheet_name = 'Report',
                        startrow=stats.shape[0] + 10, 
                        startcol=0)
    worksheet.write_string(stats.shape[0] + 14, 0, 'Coef Correlation between Numerical Variables')
    simple_corr.to_excel(writer, 
                         sheet_name = 'Report', 
                         startrow=stats.shape[0] + 15, 
                         startcol=0)
    writer.close()
    print('Done.')


def gbyExcel(df, dir_path):
    """Takes processed_df and writes excel file to a specific directory.
    """   
    writer = pd.ExcelWriter(dir_path/'Groupby_Analysis.xlsx', engine='xlsxwriter' )
    workbook = writer.book
    worksheet = workbook.add_worksheet('Groupby_Analysis')
    writer.sheets['Groupby_Analysis'] = worksheet
    worksheet.write_string(0, 0, 'Groupby_Analysis')
    df.to_excel(writer, sheet_name = 'Groupby_Analysis', startrow=1, startcol=0)
    writer.close()
    print('Done.')