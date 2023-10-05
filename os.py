import os
import datetime

# Variables
date = datetime.datetime.now()
file1 = open("logz.txt", "w")
# End Variables

# file1 plus the .write function allows us to write to the file
# file1.close allows us to close the file
file1.write(str(date))
file1.close()