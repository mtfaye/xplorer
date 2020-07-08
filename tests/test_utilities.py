import unittest

from src.utils import (_corr, _encoder, cat, df, duplicates, log_num, num,
                       processed_df, read_sql, sampling, simple_corr, stats,
                       summary, toExcel)


class TestUtils(unittest.TestCase):
    """ Class for executing unittest test cases """
    def __init__(self):
        self.file = "C:\Users\MouhamethFaye\Documents\demo_package\demo_package\data\Transaction_EN_Final.csv"

    def setUp(self):
        """ Your setUp """
        TEST_INPUT_DIR = self.file
        try:
            data = pd.read_csv(INPUT_DIR, sep = '|')
        except IOError:
            print 'cannot open file'
        self.fixture = data

    def test_dataFrame_constructedAsExpected(self):
        """ Test that the dataframe read in equals what you expect"""
        df = pd.DataFrame()
        assert_frame_equal(self.fixture, df)
           
    def test_catdf(self):
        pass    
    def test_numdf(self):
        pass
    def test_duplicateDf(self):
        pass 
    def test_encoderofDf(self):
        pass
    
if __name__ == "__main__":
    unittest.main()
    
    
    
    
        