from os import system, name

def clear():
	if name == 'nt':
		_ = system('cls')

	else: # for mac and linux(here, os.name is 'posix')
		_ = system('clear')
clear
import os    
import time    
second = 0    
minute = 0    
hours = 0    
while(True):    
    
    print('\t\t\t\t  %d : %d : %d '%(hours,minute,second))    
    print('\t\t\t\t-------------')    
    time.sleep(1)    
    second+=1    
    if(second == 60):    
        second = 0    
        minute+=1    
    if(minute == 60):    
        minute = 0    
        hours+=1;    

    clear()  
