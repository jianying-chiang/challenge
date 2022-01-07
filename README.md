# Backend Application (with CSV Export Feature)

Welcome to my application. This contains the ability to add, edit, and delete items. Additionally, it has the ability to get a list of items, as well as export it to a local CSV file. Below are the set-up guides.

# Guide (Windows)
How to Install Python
1.  Open Command Prompt
2.  Enter 'python3'. This will open Microsoft Store. Click 'Get' to download/install Python 3.9
3.  To verify that Python 3.9 has been installed, enter ```python3```
4.  To exit python environment, enter ```exit()```

How to set up application from Command Prompt
1. Download and cd to the my application (for me it is located at Downloads\GitHub\challenge-main\challenge-main)
2. Run ```python3 -m venv .venv``` to create virtual environment
3. Run ```.venv\Scripts\activate``` to activate environment
4. Run ```pip3 install -r requirements.txt```
5. Feel free to run ```python3 -m pytest tests``` to execute tests here
6. Run ```.venv\Scripts\deactivate``` to exit
7. Run ```python3 application.py``` to start server
8. Open up view.html (for me it was located at Documents\GitHub\challenge\view.html) in a browser and have fun!

How to run E2E and unit tests from Command Prompt:
1. cd  to the my application (for me it is located at Downloads\GitHub\challenge-main\challenge-main)
2. Run ```.venv\Scripts\activate```
3. Run ```python3 -m pytest tests```

Notes:
There are some instances where Command Prompt or the server may be unresponsive/stuck. Use CTRL-C to refresh and/or re-execute the command in the command prompt.

# Guide (Mac)
How to Install Python
1.  Open Terminal
2.  Run the following for downloading/running tests/starting server: 
``` 
$ sudo apt-get install git python3-virtualenv python3-pip  
$ git clone https://github.com/jianying-chiang/challenge.git  
$ cd ./challenge  
$ virtualenv --python=/usr/bin/python3 venv  
$ source ./venv/bin/activate  
$ pip3 install -r requirements.txt  
$ python3 -m pytest tests  
$ python3 application.py  
```
3. Open up view.html in a browser and have fun
