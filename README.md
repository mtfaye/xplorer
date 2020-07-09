# Profiler tool 
v 0.01 alpha.


## Package content 

	
		├──.vscode
		│
		├── README.md
		│  
		├── docs   #  Contains documentations
		│  
		├── outfile   # Contains report files
		│  
		├── examples   # Examples on how to setup and run the app 
		│  
		├── src   # Utility functions
		│   
		├── tests   # For unittesting 
		│   
		├──.gitignore   # List of undesired built-in files
		│  
		├── requirements.txt   # Bucket of all dependencies
		│ 
		├── profiler.py   # Main module of the profiler  c
		│ 
		├── setup.py   # Installer module



## Prerequisites 

Make sure to have the latest [pip](https://pip.pypa.io/en/stable/), [Git](https://git-scm.com/downloads) and [Python3+](https://www.python.org/downloads/) installed in your VM. 


## Set up 


From comnand line :

1. Clone the repo :  ``` $ git clone https://ResolutionDevops@dev.azure.com/ResolutionDevops/Profiler/_git/Profiler```

2. Go into the working directory : ``` $ cd Profiler/ ```

3. Create a virtual environment venv :  ``` $ py -m venv venv ```

4. Activate it :  ``` $ venv\scripts\activate ```

5. Install now the necessary dependencies : ``` $ (venv) pip install -r requirements.txt ```
		
	     
## Run it 

1. Open the python interpreter from command line by just typing python : 
                 ``` $ (venv) python  ```

2. Import the profiler module : 
                ```>>> import profiler as pr ```

3. Now try these following scripts to run your analysis: 

			Create a variable name of your dataset
			>>> file = r"..User/Documents/file.csv" 

			Build the excel report
			>>> pr.Profiler().build_report(file) 

			Print histograms and bars
			>>> pr.Profiler().print_graphs(file)

			NB: By default if no filter is applied for bars, only the 10 subcategories with the highest values will be shown.
			Now to filter the number of bars use one of the following functions accordingly: 
			
			For eight highest values  
			>>> pr.Profiler().f_eight(file)

			For five highest values 
			>>> pr.Profiler().f_five(file) 

			To show all  
			>>> pr.Profiler().print_all(file) 
			
			To do a log tranformation 
			>>> pr.Profiler().log(file) 

			To run a correlation analysis: Print a heatmap
			Call the function corr_viz()  
			>>> pr.Profiler().corr_viz(file) 



## Contributions 
For Contributions see the Wiki [Contribution Guidelines]()

## Note

This alpha version of the app only reads CSV files with "|" seperator and headers. 
The lack of a standardized source file makes it annoying to build a sophisticated module that process CSV files of any types. Still, while the delimiters and quoting characters vary, the overall format is similar enough that it is possible to write a single module which can efficiently manipulate such data. If the user is comfortable enough with python, he can for now modify the code accordingly to his needs but in the later version of the app, different file format and delimiter will be handled by the csv reader function. 


## Enjoy ! 

For bugs contact @mouhameth.faye@resolutioninc.ca