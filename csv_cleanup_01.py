
####### This code import a csv file and clean the keys from unwanted characters

import os.path
import csv

def getParentDir(lvl=3):
    thisFile = os.path.abspath(__file__)
    pathSplit = thisFile.split("\\") 
    count = 0
    while count < int(lvl):
        pathSplit.pop(-1)
        count += 1
    parentDir = "\\".join(pathSplit)
    return parentDir

def newFilePath(fileFolder,fileName):
    folderPath = getParentDir() + "\\" + fileFolder
    filePath = folderPath + "\\" + fileName
    if os.path.exists(filePath):
        return filePath
    else:
        return "There is no file named {fN} in {fP}".format(fN=fileName,fP=folderPath)
    
def clean_key(key):
  """
  This function removes non-alphanumeric characters and underscores (_) from a key.
  You can customize the cleaning logic based on your specific requirements.
  """
  cleaned_key = ''.join(c for c in key if c.isalnum() and c != 'ï' or c == '_')
  return cleaned_key
       
filePath = newFilePath("test_files","color_srgb.csv")

with open(filePath,newline="") as csvFile:
    dictA = csv.DictReader(csvFile)

    # Clean the fieldnames (column names)
    cleaned_fieldnames = [clean_key(key) for key in dictA.fieldnames]
    
    # Iterate through the rows using the cleaned fieldnames
    for row in dictA:
        # Create a new dictionary with cleaned keys and corresponding values
        dictB = {cleaned_fieldnames[i]: row[dictA.fieldnames[i]] for i in range(len(dictA.fieldnames))}
        print(dictB)


##########################################################################################################

