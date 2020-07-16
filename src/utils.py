"""Utility fonctions for statistical description of datasets.
"""

import numpy as np
import pandas as pd
import pyodbc


def df(file, chunksize):
    """Takes csv files and returns a pandas dataframe.
    """ 
    print('Reading data...')
    reader = pd.read_csv(file, 
                         sep='|',
                         chunksize=chunksize,
                         iterator=True)  
    data = pd.concat(reader, ignore_index=True)
    return data

 
def read_sql(server, database, username, password):
    """Read tables from a remote sql database and returns a pandas dataframe.
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
    """
    print('Computing stats...')
    df.columns = df.columns.str.strip().str.replace('/', '_').str.replace('(', '').str.replace(')', '')
    return df


def num(processed_df):
    """Returns dataframe object with numerical columns only.
    """
    num_df = [col for col in processed_df.columns if processed_df[col].dtype != 'object']
    return processed_df[num_df]

    
def cat(processed_df):
    """Returns dataframe object with categorical columns only. 
    """
    cat_df = [col for col in processed_df.columns if processed_df[col].dtype == 'object']
    return processed_df[cat_df]


def summary(processed_df, num, cat):
    """ Resumes the dataset.
    """
    _dict = [{'Rows': processed_df.shape[0], 
             'Variables': processed_df.shape[1],
             'Numerical': len(num.columns), 
             'Categorical': len(cat.columns), 
             'Missing': processed_df.isnull().sum().sum(),
             '% of Missing': processed_df.isnull().sum().sum() / len(processed_df)}]
    return pd.DataFrame(_dict)


def stats(processed_df):
    """ Takes a dataframe object and returns a dpd Data Profile (Dataframe).
    """
    dpd = pd.DataFrame(index=np.arange(0, len(processed_df.columns)), columns=('column_name', 'col_data_type', 'unique_values_count',  'non_null_values'))
    for ind, cols in enumerate(processed_df.columns):
        dpd.loc[ind] = [cols, processed_df[cols].dtype, processed_df[cols].nunique(), processed_df[cols].count()]
    dpd['%_of_non_nulls'] = (dpd['non_null_values'] / processed_df.shape[0]) * 100 
    dpd['null_values'] = processed_df.shape[0] - dpd['non_null_values']
    dpd['%_of_nulls'] = 100 - dpd['%_of_non_nulls']
    desc = processed_df.describe().T.round(2)
    dpd = pd.merge(dpd, desc, how='left', left_on='column_name', right_index=True)
    return dpd

 
def duplicates(processed_df):
    """Returns a dataframe with dupilcated rows
    """
    dup_bool = processed_df.duplicated(subset=None, keep='first')
    dup = processed_df.loc[dup_bool == True]
    return dup

   
def log_num(num):
    """Returns a log values of a pandas series
    args: pd.Series
    """
    return np.log10(num)    


def sampling(processed_df, sample_size):
    """Sampling the dataset
    Arg: Dataframe and sample size en Integer
    return: dataframe size of the sampling.
    """
    return processed_df.sample(sample_size)

    
def simple_corr(sampling):
    """Takes a dataframe a return table of pearson correlation between numerical variables.
    Args: dataframe
    returns: dataframe
    """
    return sampling.corr(method='pearson')

def _encoder(sampling):
    """Encodes all categorical variables.
    Args: dataframe
    return: dataframe
    """
    return pd.get_dummies(sampling, columns=None, drop_first=True)
    

def _corr(_encoder, col, k):
    """Takes the 10 highest corr coeff of a choson variable col. 
    args: dataframe of encoded variables, col : chosen of target variable (string), k : treshold (int)
    return : dataframe
    """
    c = _encoder.corr().nlargest(k, col)[col].index
    cm = _encoder[c].corr().round(2)
    return cm  


def toExcel(summary, stats, duplicates, simple_corr, _corr, dir_path):
    """Takes processed_df and writes excel file to a specific directory.
    """  
    print('Writing report...')    
    writer = pd.ExcelWriter(dir_path/'your_report.xlsx', engine='xlsxwriter' )
    workbook = writer.book
    worksheet = workbook.add_worksheet('Report')
    writer.sheets['Report'] = worksheet
    worksheet.write_string(0, 0, 'Summary')
    summary.to_excel(writer, sheet_name = 'Report', startrow=1, startcol=0)
    worksheet.write_string(summary.shape[0] + 4, 0, 'Stats')
    stats.to_excel(writer, sheet_name = 'Report', startrow=summary.shape[0] + 5, startcol=0)
    worksheet.write_string(stats.shape[0] + 9, 0, 'Duplicates')
    duplicates.to_excel(writer, sheet_name = 'Report', startrow=stats.shape[0] + 10, startcol=0)
    worksheet.write_string(stats.shape[0] + 14, 0, 'Coef Correlation between Numerical Variables')
    simple_corr.to_excel(writer, sheet_name = 'Report', startrow=stats.shape[0] + 15, startcol=0)
    worksheet.write_string(stats.shape[0] + 24, 0, 'Coef Correlation between Categorical variables and a chosen target variable')
    _corr.to_excel(writer, sheet_name = 'Report', startrow=stats.shape[0] + 25, startcol=0)
    writer.close()
    print('Done.')


def sep():
    pass
