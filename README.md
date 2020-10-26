# Python SIMPLE  Template for CLI projects 

TODO:

This template was created by David Gutierrez (https://github.com/david68cu).


## We should use a template we know for our projects
TODO:


## Where to find some help if issues arise using this template ?


There is a repo for more adavanced template when you need testing and intermodule interactions
The advanced repo is located at [0.1]

This repo is for simples cli projects , usually when you do not interaction between multiple modules so 
importing is not a big deal. the repo is in [0]


## Running the CLI application
  
  - Install a pipenv
  - Make your file structure similar to the following tree:

  - Running the application
      - python sample/core.py (from outside sample dir)
      - python core.py (from sample dir)
  -Testing the application
      - python -m unittest tests/test_basic.py
      - python -m unittest tests/test_advanced.py
      
  - To understand more about the file composition , please read the GitHUb repo 
 
 
## Use of Linters, Static Code tools and Complexity check for code analysis
 
 We use the tools described in "Python Professional Code Recomedations" in [2]...
 
-Use of Lynters , Static Code tools for Code Quality [2]

    -I use black frecuently for code formatting or stilistic [2.4]
    -I use bandit frecuently that analyzes security errors [2.3]
    -I use pyflakes for Logical errors that Analyzes programs and detects various errors [2.2]
    -For complexity checker I use McCabe [2.1]

## What is that README.rst and why it is added to this repo

Python project could need a web documentation. Usually we use Sphinx . We are just  noticing where the Sphins 
Readme.rst file should go in the Python file structure


## Continuos Integration

TODO:


  
### References
 
 - [0] [David Gutierrez Python CLI template simple](https://github.com/david68cu/python_cli_template_simple)
 - [0.1] [David Gutierrez Python CLI template advanced](https://github.com/david68cu/python_cli_template_advanced)
 - [1] [Solving Import Problems by Creating a correct Python CLI project struture ]( https://github.com/david68cu/python_import_issues_project_structure.git)
 - [2] [How to Create Professional Python Code](https://github.com/david68cu/python_professional_code_recomendations)
    - Python Code Quality: Tools & Best Practices
        - [2.1] [McCabe complexity checker](https://github.com/PyCQA/mccabe)
        - [2.2] [PyFlakes for python logical errors ](https://github.com/PyCQA/pyflakes)
        - [2.3] [Python Bandit static code security ](https://github.com/PyCQA/bandit)
        - [2.4] [Black the uncompromised formatter](https://github.com/ambv/black)
 
 
