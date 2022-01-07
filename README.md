# Shopify Backend Application (with CSV Export Feature)

Welcome to my application. This contains the ability to add, edit, and delete items. Additionally, it has the ability to get a list of items, as well as export it to a local CSV file. Below are the set-up guides.

# Guide (Windows)
How to Install Python
1.  Open Command Prompt
2.  Enter 'python3'. This will open Microsoft Store. Click 'Get' to download/install Python 3.9
3.  To verify that Python 3.9 has been installed, enter 'python3'
4.  To exit python environment, enter 'exit()'

How to set up application from Command Prompt
1. Go to the my application (for me it is located at Documents\GitHub\shopify)
2. Run 'python3 -m venv .venv' to create virtual environment
3. Run '.venv\Scripts\activate' to activate environment
4. Run 'pip3 install -r requirements.txt'
5. Run 'deactivate' to exit
6. Run 'python3 application.py' to start server
7. Open up view.html (for me it was located at Documents\GitHub\shopify\view.html) in a browser and have fun!

How to run E2E and unit tests from Command Prompt:
1. cd  to the my application (for me it is located at Documents\GitHub\shopify)
2. Run '.venv\Scripts\activate'
2. Run 'python3 -m pytest tests'
