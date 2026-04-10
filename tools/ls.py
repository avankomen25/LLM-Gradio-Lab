#Step1: create function with right number of args, write docstring 
#step2: create the doctests for the function 
#Step3: get the function to pass the doctests
#may have to modify doctests to get them to pass 

import glob
def ls(folder=None):
    '''
    This function behaves just like the ls program in the shell.
    >>> ls()
    'chat.py htmlcov __pycache__ requirements.txt tools venv'

    >>> ls('tools')
    'ls.py'
    '''
    if folder:
        result = ''
        #folder + '/*/==> tools/*
        # glob is nondeterministic (no guarentee of glbo results, convert it to deterministic
        #in a llm we did that by determining temperature, best way to make a list deterministic is to sort it)
        for path in sorted(glob.glob(folder + '/*')):
            result += path + ' '
        return result
    else:
        result = ''
        for path in sorted(glob.glob('*')):
            result += path + ' '
        return result.strip()
    #handle this case 
   
 
  