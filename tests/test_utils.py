"""Unit testing for utility fonctions. 
"""
import pandas
import pytest
import src.utils


@pytest.fixture(scope="session")
def result_fixture():
    test_data = r"C:\Users\MouhamethFaye\Documents\demo_package\demo_package\data\Transaction_EN_Final.csv"
    test_chunk = 300000
    df = src.utils.read_csv(test_data, test_chunk)
    return df


def test_dfSize(result_fixture):
    def is_df_big(result_fixture):
        if len(result_fixture) > 300000:
            return True
        else:
            return False
        
    assert is_df_big(result_fixture) is True 
    
    
def test_dfObjecttype(result_fixture):
    assert isinstance(result_fixture, pandas.DataFrame)
