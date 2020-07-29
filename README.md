# Profiler tool 
v 0.01 alpha.

This alpha version of the app reads only CSV files with "|" seperator and headers. 
The lack of a standardized source file makes it annoying to build a sophisticated module that process CSV files of any types. Still, while the delimiters and quoting characters vary, the overall format is similar enough that it is possible to write a single module which can efficiently manipulate such data. 
If the user of this application is comfortable enough with the source code, he can go into the src directory on the utils python file and hard code the delimiter under the read_csv function.


## Package content 

	
		├── docs # Documentations
		│
		├── examples # Examples on how to setup and run the app
		│  
		├── outfile   # Contains report files
		│  
		├── src   # source code
		│  
		├── tests   # For unittesting      
		│  
		├── .gitignore   # List of undesired built-in files
		│   
		├── dev-requirements.txt  # dependencies for development and testing
		│   
		├── profiler.py   # Main module of the profiler  
		│   
		├── README.md   
		│  
		├── requirements.txt   # Bucket of all dependencies
		│ 
		├── setup.py   # pip installer module



## Prerequisites 

Make sure to have the latest [pip](https://pip.pypa.io/en/stable/), [Git](https://git-scm.com/downloads) and [Python3+](https://www.python.org/downloads/) installed in your VM. 


## Setup 


From command line :

1. Clone the repo :  ``` $ git clone https://ResolutionDevops@dev.azure.com/ResolutionDevops/Profiler/_git/Profiler```

2. Go into the working directory : ``` $ cd Profiler ```

3. Create a virtual environment venv :  ``` $ py -m venv venv ```

4. Activate it :  ``` $ venv\scripts\activate ```

5. Install now the necessary dependencies : ``` $ (venv) pip install -r requirements.txt ```
		
	     
## Run it 

- First : 
			Go on the config.py file (src/config.py) and assign a variable to your filepath

			filepath = r"C:User/Documents/filename.csv" 

- Now try these following scripts to run your analysis: 

			Build the excel report
			profiler.py build_report

			Print histograms and bars
		    profiler.py print_graphs

			NB: By default if no filter is applied for bars, only the 10 subcategories with the highest values will be shown.
			Now to filter the number of bars use one of the following functions accordingly: 
			
			For eight highest values  
			profiler.py f_eight

			For five highest values 
			profiler.py f_five

			To show all  
			profiler.py print_all 
			
			To apply a log tranformation of numerical columns
			profiler.py log

			To run a correlation analysis: Print a heatmap
			Call the function corr_viz()  
			profiler.py corr_viz


- To run a groupby analysis

			For groupby function of one given categorical column with all the numerical columns of the dataframe.
			profiler.py gb 'Direction'

			For groupby function of two given categorical columns with all the numerical columns of the dataframe.
			profiler.py gbtwo 'Direction' 'Market'

			For groupby function of one given categorical column and one given numerical column.
			profiler.py gbonebyone 'Market' 'Amount'

			For groupby function of two given categorical column and two given numerical columns.
			profiler.py gbtwobytwo 'Direction' 'Market' 'Amount' 'IdTrx'



## Contributing Documentation Changes

Documentation improvements are always welcome! The documentation files live in the docs/ directory of the codebase. They’re written using Microsoft Word but it can be written in any type of text file, Markdown and Microsoft Word are the preferred one though.


## Contributing Code Changes

When contributing code, you’ll want to follow this checklist :
- 1. Fork the project repository at [master branch Repos](https://ResolutionDevops@dev.azure.com/ResolutionDevops/Profiler/_git/Profiler)if you haven't already.
- 2. Clone your fork in your Virtual Machine.
- 3. Create a new branch (Best Practices : never work on the master branch).
- 4. After writing your codes, push commits to the branch created (Always use  the file dev-requirements.txt when developing or running a test).
- 5. Consider whether documentation or tests need to be added or updated as part of the change, and add them as needed.
- 6. Send a pull request to the main repository’s [master branch](https://ResolutionDevops@dev.azure.com/ResolutionDevops/Profiler/_git/Profiler.) (Only in special cases would the Pull Request be opened against other branches.)

## Bug Reports

Bug reports are hugely important! Before you raise one, though, please verify if the same bug hasn’t been reported before.
Now to report bugs create a work item  Issue on the current Sprint. Describe the bug by writing a user story on the description area.
Use the template below to report a bug :

- ### Scenario: 
Explain the context of the bug by listing the steps taken that raised the bug. 
- ### Current Behavior: 
Explain the bug and provide the error message if possible.
- ### Expected Behavior:
Explain what you were trying to accomplish or what you were expecting to see as a result. 


## Coding Style
The codebase of this project was built using the style guide for Python code PEP-8. To ensure an uniformity of code for the project, please try to follow the same coding style as much as possible. 
For more about PEP-8 see  [Link](https://www.python.org/dev/peps/pep-0008/).



## Enjoy ! 


Contact maintainer @mouhameth.faye@resolutioninc.ca