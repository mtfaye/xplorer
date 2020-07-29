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


class Profiler:
    def __init__(self):
        print('Profilage de donnees v0.02 Alpha')
            
    def build_report(self, filepath):
        read_file = fHandler(filepath)
        clean_df = processed_df(read_file)
        is_summary = summary(clean_df, num(clean_df), cat(clean_df))
        is_stats = stats(clean_df)
        is_dup = duplicates(clean_df)
        is_corr = simple_corr(clean_df)
        return toExcel(is_summary, is_stats, is_dup, is_corr, outfile)
        
    def print_graphs(filepath):
        read_file = fHandler(filepath)
        clean_df = processed_df(read_file)
        return filter_ten(cat(clean_df), outfile), hist(num(clean_df), outfile)
    
    def f_five(filepath):
        read_file = fHandler(filepath)
        clean_df = processed_df(read_file)
        return filter_five(cat(clean_df), outfile)
   
    def f_eight(self, filepath):
        read_file = fHandler(filepath, self.chunksize)
        clean_df = processed_df(read_file)      
        return filter_eight(cat(clean_df), outfile)
             
    def print_all(self, filepath):
        read_file = fHandler(filepath)
        clean_df = processed_df(read_file)
        return hist(num(clean_df), outfile), bar(cat(clean_df), outfile), plotSimplecorr(is_corr, outfile)
        
    def corr_viz(self, filepath):
        read_file = fHandler(filepath)
        clean_df = processed_df(read_file)
        scorr = simple_corr(clean_df)
        return plotSimplecorr(scorr, outfile)
        
    def log(self, filepath):
        read_file = fHandler(filepath)
        clean_df = processed_df(read_file)      
        log_ = log_num(num(clean_df))
        return hist(log_, outfile)
    
    def gb(sefl, filepath, i):
        read_file = fHandler(filepath)
        clean_df = processed_df(read_file)
        analysis = gbOne(clean_df, i)
        return gbyExcel(analysis, outfile)
    
    def gbtwo(self, filepath, x, y):
        read_file = fHandler(filepath)
        clean_df = processed_df(read_file)
        analysis = gbTwo(clean_df, x, y)
        return gbyExcel(analysis, outfile)
        
    def gbonebyone(self, filepath, x, y):
        read_file = fHandler(filepath)
        clean_df = processed_df(read_file)
        analysis = gbOnebyOne(clean_df, x, y)
        return gbyExcel(analysis, outfile)
        
    def gbtwobytwo(self, filepath, v, x, y, z):
        read_file = fHandler(filepath)
        clean_df = processed_df(read_file)
        analysis = gbTwobyTwo(clean_df, v, x, y, z)
        return gbyExcel(analysis, outfile)
    

if __name__ == '__main__':
    Profiler().build_report(filepath)
    Profiler().print_graphs(filepath)
    Profiler().f_five(filepath)
    Profiler().f_eight(filepath)
    Profiler().print_all(filepath)
    Profiler().log(filepath)   
    Profiler().corr_viz(filepath)
    Profiler().gb(filepath, i)
    Profiler().gbtwo(filepath, x, y)
    Profiler().gponebyone(filepath, x, y)
    Profiler().gptwobytwo(filepath, v, x, y, z)
    
 
