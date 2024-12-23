# URL shortener
Simple web app for shortening your URLs. Run it, enter your URL in the input field, get a shortened one.  
One can use it later to navigate to the original one. The goal of this application was purely educational.  
It uses `sqlite3` as the database and `md5` hashing algorithm as a generator of short url.

## Prerequisites
- Python 3.12
- uv

## How to run
At first, install dependencies using `uv sync`.  
After that you can run the application using `flask run`.  
Make sure that the virtual environment is activated.
