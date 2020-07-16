"""Common part to all others modules : Profiler main class"""

from src.config import outfile, file
from src.plot_helpers import bar, filter_eight, filter_five, filter_ten, hist, plot_corr
from src.utils import (cat, df, duplicates, log_num, num, processed_df,
                       read_sql, stats, summary, toExcel, sampling, simple_corr, _corr, _encoder)
import scripts.fhandler


class Profiler:
    
    def __init__(self):
        print('Profilage de donnees v0.01 Alpha')
        self.sample_size = 1000
        self.n_highest = 30
        self.col = "Amount"
            
    def build_report(self, file):
        read_file = _fHandler(file)
        clean_df = processed_df(read_file)
        is_summary = summary(clean_df, num(clean_df), cat(clean_df))
        is_stats = stats(clean_df)
        is_dup = duplicates(clean_df)
        is_samp = sampling(clean_df, self.sample_size)
        is_dum = _encoder(is_samp)
        is_corr = _corr(is_dum, self.col, self.n_highest).loc[:, self.col]
        scorr = simple_corr(is_samp)
        toExcel(is_summary, is_stats, is_dup, scorr, is_corr, outfile)
        
    def print_graphs(self, file):
        read_file = _fHandler(file)
        clean_df = processed_df(read_file)
        hist(num(clean_df), outfile)
        filter_ten(cat(clean_df), outfile)
    
    def f_five(self, file):
        read_file = _fHandler(file)
        clean_df = processed_df(read_file)
        filter_five(cat(clean_df), outfile)
   
    def f_eight(self, file):
        read_file = df(file, self.chunksize)
        clean_df = processed_df(read_file)      
        filter_eight(cat(clean_df), outfile)
             
    def print_all(self, file):
        read_file = _fHandler(file)
        clean_df = processed_df(read_file)
        is_samp = sampling(clean_df, self.sample_size)
        is_dum = _encoder(is_samp)
        is_corr = _corr(is_dum, self.col, self.n_highest)
        hist(num(clean_df), outfile)
        bar(cat(clean_df), outfile)
        plot_corr(is_corr, outfile)
        
    def corr_viz(self, file):
        read_file = _fHandler(file)
        clean_df = processed_df(read_file)
        is_samp = sampling(clean_df, self.sample_size)
        is_dum = _encoder(is_samp)
        is_corr = _corr(is_dum, self.col, self.n_highest)
        plot_corr(is_corr, outfile)

    def log(self, file):
        read_file = _fHandler(file)
        clean_df = processed_df(read_file)      
        log_ = log_num(num(clean_df))
        hist(log_, outfile)
        
             
if __name__ == "__main__":
    Profiler().build_report(file)
    Profiler().print_graphs(file)
    Profiler().f_five(file)
    Profiler().f_eight(file)
    Profiler().print_all(file)
    Profiler().log(file)   
    Profiler().corr_viz(file)