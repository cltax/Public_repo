import hou
nodeSel = hou.selectedNodes()

counter = 1

inputCheck = "env"
newName = "newName"
nameSplitList = []
cleanNameList = []

#get the name of each node and return a list
def getNodeName(nodeSel):
    namesList = [node.name() for node in nodeSel]
    return namesList
    
#get the list of node names and split each name into components, return a list of lists
def replaceNodeNames(namesList):
    for eachName in namesList:
        if inputCheck in eachName:
            eachName.replace(inputCheck,newName)
            #remove the any number from the name
            cleanName = ["".join(char for char in eachName if not char.isdigit())]

            
                     
            #nameSplitList.append(eachName.split(inputCheck))          
        else:
            print(f"No match for {inputCheck}")
    return nameSplitList
'''
#get the list of names split and remove "_" and numbers
def cleanNames(nameSplitList):
    for eachList in nameSplitList:
        cleanNameList = ["".join(char for char in item if not char.isdigit() and char != '_') for item in eachList]
  '''   

#remove the number from       

    

