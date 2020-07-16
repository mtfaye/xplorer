""" Different files extension handler.
"""
from pathlib import Path
import pandas as pd
import warnings


def warn_read(extension):
    """Warn the user when an extension is not supported.
    Args:
        extension: The extension that is not supported.
    """
    warnings.warn(
        f"""There was an attempt to read a file with extension {extension}, we assume it to be in CSV format.
To prevent this warning from showing up, please rename the file to any of the extensions supported by pandas
         """)


def _fHandler(file_name):
    """Read DataFrame based on the file extension. 
    Various file types are supported (.csv, .json, .jsonl,.xls, .xlsx, .hdf, .h5, .pkl, .pickle)
    Args:
        file_name: the file to read
    Returns:
        DataFrame
    """
    import os.path
    extension = os.path.splitext(file_name)[1]
    if extension == '.json':
        df = pd.read_json(str(file_name))
    elif extension == '.jsonl':
        df = pd.read_json(str(file_name), lines=True)
    elif extension in [".xls", ".xlsx"]:
        df = pd.read_excel(str(file_name))
    elif extension in [".hdf", ".h5"]:
        df = pd.read_hdf(str(file_name))
    elif extension in [".pkl", ".pickle"]:
        df = pd.read_pickle(str(file_name))
    else:
        if extension != ".csv":
            warn_read(extension)
            
        df = pd.read_csv(file_name, sep='|')
    return df
