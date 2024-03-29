"""Common part to all others modules : Profiler main class
"""

from src.config import filepath, outfile
from src.fhandler import fHandler
from src.groupby import gbOne, gbOnebyOne, gbTwo, gbTwobyTwo

from src.plot_helpers import (
    bar, filter_eight, filter_five, filter_ten, hist, plotSimplecorr)

from src.utils import (cat, correlor, duplicates, enCoder, gbyExcel, log_num,
                       num, processed_df, read_csv, read_sql, sampling,
                       simple_corr, stats, summary, toExcel)

import fire



class Profiler:
    def __init__(self):
        print('Profilage de donnees v0.02 Alpha')
        self.read_file = fHandler(filepath)
        self.clean_df = processed_df(self.read_file)
            
    def build_report(self):
        

        
    def build_report(self, file):
        read_file = fHandler(file)
        clean_df = processed_df(read_file)
        is_summary = summary(clean_df, num(clean_df), cat(clean_df))
        is_stats = stats(clean_df)
        is_dup = duplicates(clean_df)
        is_samp = sampling(clean_df, self.sample_size)
        is_dum = enCoder(is_samp)
        is_corr = correlor(is_dum, self.col, self.n_highest).loc[:, self.col]
        scorr = simple_corr(is_samp)
        toExcel(is_summary, is_stats, is_dup, scorr, is_corr, outfile)

    def print_graphs(self):
        return filter_ten(cat(self.clean_df), outfile), hist(num(self.clean_df), outfile)
    
    def f_five(self):
        return filter_five(cat(self.clean_df), outfile)
   
    def f_eight(self):
        return filter_eight(cat(self.clean_df), outfile)
             
    def print_all(self):
        return hist(num(self.clean_df), outfile), bar(cat(self.clean_df), outfile), plotSimplecorr(is_corr, outfile)
        
    def corr_viz(self):
        scorr = simple_corr(self.clean_df)
        return plotSimplecorr(scorr, outfile)
        
    def log(self):   
        log_ = log_num(num(self.clean_df))
        return hist(log_, outfile)
    
    def gb(self, i):
        analysis = gbOne(self.clean_df, i)
        return gbyExcel(analysis, outfile)
    
    def gbtwo(self, x, y):
        analysis = gbTwo(self.clean_df, x, y)
        return gbyExcel(analysis, outfile)
        
    def gbonebyone(self, x, y):
        analysis = gbOnebyOne(self.clean_df, x, y)
        return gbyExcel(analysis, outfile)
        
    def gbtwobytwo(self, v, x, y, z):
        analysis = gbTwobyTwo(self.clean_df, v, x, y, z)
        return gbyExcel(analysis, outfile)
    

def main():
    fire.Fire(Profiler)
 

if __name__ == '__main__':

