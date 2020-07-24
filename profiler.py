"""Common part to all others modules : Profiler main class
"""

from scripts.fhandler import fHandler
from src.config import filepath, outfile
from src.plot_helpers import (
    bar, filter_eight, filter_five, filter_ten, hist, plotSimplecorr)
from src.utils import (
    cat, correlor, duplicates, enCoder, log_num, num, processed_df, read_csv,
    read_sql, sampling, simple_corr, stats, summary, toExcel, gbyExcel)
from scripts.groupby import gbyone, gbytwo, gbyselectnum
import fire

class Profiler:
    
    def __init__(self):
        print('Profilage de donnees v0.02 Alpha')
        self.sample_size = 1000
        self.n_highest = 30
        self.col = 'Amount'
        self.i = None
        self.v = None
        self.x = None
        self.y = None
        self.z = None
        
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
        
    def print_graphs(file):
        read_file = fHandler(file)
        clean_df = processed_df(read_file)
        hist(num(clean_df), outfile)
        filter_ten(cat(clean_df), outfile)
    
    def f_five(file):
        read_file = fHandler(file)
        clean_df = processed_df(read_file)
        filter_five(cat(clean_df), outfile)
   
    def f_eight(self, file):
        read_file = fHandler(file, self.chunksize)
        clean_df = processed_df(read_file)      
        filter_eight(cat(clean_df), outfile)
             
    def print_all(self, file):
        read_file = fHandler(file)
        clean_df = processed_df(read_file)
        is_samp = sampling(clean_df, self.sample_size)
        is_dum = enCoder(is_samp)
        is_corr = correlor(is_dum, self.col, self.n_highest)
        hist(num(clean_df), outfile)
        bar(cat(clean_df), outfile)
        plotSimplecorr(is_corr, outfile)
        
    def corr_viz(self, file):
        read_file = fHandler(file)
        clean_df = processed_df(read_file)
        is_samp = sampling(clean_df, self.sample_size)
        is_dum = enCoder(is_samp)
        scorr = simple_corr(is_samp)
        plotSimplecorr(scorr, outfile)
        
    def log(file):
        read_file = fHandler(file)
        clean_df = processed_df(read_file)      
        log_ = log_num(num(clean_df))
        hist(log_, outfile)
    
    def groupbyone(self, file):
        read_file = fHandler(file)
        clean_df = processed_df(read_file)
        analysis = gbyone(clean_df, self.i)
        gbyExcel(analysis, outfile)
    
    def groupbytwo(self, file, v, x):
        read_file = fHandler(file)
        clean_df = processed_df(read_file)
        analysis = gbytwo(clean_df, self.v, self.x)
        gbyExcel(analysis, outfile)
    
    def groupbyselect(self, file, y, z):
        read_file = fHandler(file)
        clean_df = processed_df(read_file)
        analysis = gbyselectnum(clean_df, self.y, self.z)
        gbyExcel(analysis, outfile)
        
        
def main():
    Profiler().build_report(file)
    Profiler().print_graphs(file)
    Profiler().f_five(file)
    Profiler().f_eight(file)
    Profiler().print_all(file)
    Profiler().log(file)   
    Profiler().corr_viz(file)
    Profiler().groupbyone(file)
    Profiler().groupbytwo(file)
    Profiler().groupbyselect(file)
        
        
if __name__ == '__main__':
    fire.Fire(main)
        