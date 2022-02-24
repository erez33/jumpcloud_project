## Install any dependencies
You may use homebrew to install python 3.7(since python 3.7 was used for this project):<br>
brew install python@3.7 <br>
https://formulae.brew.sh/formula/python@3.7 <br>
Further instruction can be found here^^^ 


Once python has been installed, <br>
Install the requests module
by opening a terminal and running the following command:<br>

    pip3 install requests 
https://pypi.org/project/requests/ <br>
This is needed to send requests to the endpoints

Note:
The only other modules used are 
random and unittest. Both happen to 
builtin modules

## Steps to run the tests
1. In your terminal, CD into the 'broken-hashserve' directory
2. Start the server by entering the command 'broken-hashserve'
3. CD back out to the root folder
4. To execute tests:
    
        python3 -m unittest -v  tests.py

Further details on the unittest framework can be found here:<br>
https://docs.python.org/3/library/unittest.html


## Accompanying documents
These following documents will be found in the /documents directory
1. Tests cases
2. Defects, Improvements and other Observations
3. Notes