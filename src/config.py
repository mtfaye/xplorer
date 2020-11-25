"""Path and files management."""

from pathlib import Path, PureWindowsPath

parent_dir = Path(__file__).resolve().parents[1]

# directory to save report and graphs images 
dir_path = parent_dir/"outfile"
outfile = PureWindowsPath(dir_path)

# credentials for a remote sql server access
server = '#################' 
database = '################' 
username = '#################' 
password = '##################'
tablename = '##################'

# You can initialize the csv file path from here
filepath = r"C:\Users\MouhamethFaye\Desktop\tesst.TXT"