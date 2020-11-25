""" Different files extension handler.
"""
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


def fHandler(filename):
    """Read DataFrame based on the file extension. 
    Various file types are supported (.csv, .txt, .json, .jsonl,.xls, .xlsx, .hdf, .h5, .pkl, .pickle)
    Args:
        filename: the file to read
    Returns:
        DataFrame
    """
    import os.path
    extension = os.path.splitext(filename)[1]
    if extension == '.json':
        df = pd.read_json(str(filename))
    elif extension == '.jsonl':
        df = pd.read_json(str(filename), lines=True)
    elif extension in [".xls", ".xlsx"]:
        df = pd.read_excel(str(filename))
    elif extension in [".hdf", ".h5"]:
        df = pd.read_hdf(str(filename))
    elif extension in [".pkl", ".pickle"]:
        df = pd.read_pickle(str(filename))
    else:
        if extension != ".csv" and ".txt":
            warn_read(extension)
            
        df = pd.read_csv(filename, sep=';', encoding="ISO-8859-1", header=None)
    return df
