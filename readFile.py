

import csv

f= open("student.csv","r",newline="")
with open ("C:\Users\hp\OneDrive\Desktop\CRT Phase1\student.csv","r",newline="") as file:
    read=csv.DictReader(file)
    for row in read:
        