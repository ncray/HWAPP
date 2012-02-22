import os

# array to store all the homework objects
hws = []

# extract homework object from each .py file in directory
for filename in os.listdir('/home/ncray/hwapp/homework'):
    if filename[-3:]=='.py' and filename!='__init__.py':
        module = filename[:-3]
        try:
            exec('from ' + module + ' import homework')
            hws.append(homework)
        except ImportError:
            continue # ignore modules that do not have a homework object
