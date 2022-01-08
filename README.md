# Backend Application (with CSV Export Feature)

Welcome to my application. This contains the ability to add, edit, and delete items. Additionally, it has the ability to get a list of items, as well as export it to a local CSV file. Below are the backend structure and set-up guides.

# Backend Structure:
challenge-main
│   application.py (App entry point)
│   config.py (configuration for the app, i.e. db link)
│
└───application (main folder)
│   │  
│   └───api (Handles all incoming API requests)
│   └───service (Handles all business/service logic)
│   └───dao (Handles all DB-related operations/interactions)
│   └───model (contains table schema, i.e. Item)
│   └───util (Utility/Helper functions)
└───tests
│   │  
│   └───e2e (End to End tests. Calls APIs with different params/JSONs)
│   └───service (Unit tests. Checks that all utility/helper functions are working as expected)

# Guide (Windows/Mac)

Pre-requisites:
1. Feel free to clone/download the project as a ZIP and extract it. (For cloning, run ```git clone https://github.com/jianying-chiang/challenge.git``` for Mac as it comes with git)  
2. Open up Command Prompt (CMD)  
3. Navigate to project using ```cd``` command (i.e. ```cd Downloads\challenge-main```)  

How to Install Python from Command Prompt (make sure you have ```cd``` to project folder)  
1.  Enter ```python3```. This will open Microsoft Store. Click 'Get' to download/install Python 3.9  
2.  To verify that Python 3.9 (other versions are valid as well) has been installed, enter ```python3```  
3.  To exit python environment, enter ```exit()```  

How to set up application from Command Prompt (make sure you have ```cd``` to project folder)  
1. Enter ```pip3 install -r requirements.txt```  
2. Feel free to run ```python3 -m pytest tests``` to execute tests here  
3. Run ```python3 application.py``` to start server  
4. Open up view.html (for me it was located at Downloads\challenge-main\view.html) in a browser and have fun!  

How to run E2E and unit tests from Command Prompt (make sure you have ```cd``` to project folder)
1. Run ```python3 -m pytest tests```

Notes:
There are some instances where Command Prompt or the server may be unresponsive/stuck. Use CTRL-C to refresh and/or re-execute the command in the command prompt.
Additionally, the set-up commands assume you dont have any alias
