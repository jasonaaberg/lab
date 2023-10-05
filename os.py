import os
import datetime

# Variables
date = datetime.datetime.now()
file1 = open("logz.txt", "w")
# End Variables

file1.write(str(date))
file1.close()