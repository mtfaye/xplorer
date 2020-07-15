"""Testing code for the utils fonctions. 
"""
from unittest.mock import Mock    
import pytest
import src.utils 
import pandas 


@pytest.fixture(scope="session")
def result_fixture():
    test_data = r"C:\Users\MouhamethFaye\Documents\demo_package\demo_package\data\Transaction_EN_Final.csv"
    test_chunk = 300000
    df = src.utils.df(test_data, test_chunk)
    return df


def test_dfSize(result_fixture):
    """ Checks if dataframe has over a 300000 rows.
    default chunksize for reading a csv file is 300000.
    """
    
    def is_df_big(result_fixture):
        if len(result_fixture) > 300000:
            return True
        else:
            return False
        
    assert is_df_big(result_fixture) is True 
    
    
def test_dfObjecttype(result_fixture):
    """Checks if a dataframe is passed to all others utils functions
    """
    assert isinstance(result_fixture, pandas.DataFrame)
