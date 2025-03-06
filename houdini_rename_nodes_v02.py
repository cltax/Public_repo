import hou
nodeSel = hou.selectedNodes()

nodeNumber = 1

inputCheck = "env"
newName = "newName"
nameSplitList = []
cleanNameList = []

#get the name of each node and return a list
def getNodeName(nodeSel):
    namesList = [node.name() for node in nodeSel]
    return namesList
    
#get the list of names and return a clean, updated one
def createCleanNames(namesList):
    for eachName in namesList:
        if inputCheck in eachName:
            replacedName = eachName.replace(inputCheck,newName)
            #remove the any number from the name
            tempName = ["".join(char for char in replacedName if not char.isdigit())]
            #strip "_"
            cleanName = tempName[0].strip("_")
            #add the cleaned name to the list
            cleanNameList.append(cleanName)        
        else:
            print(f"No match for {inputCheck}")
    return cleanNameList
    
#set the new name for each node 
def setNodeName(nodeSel,nodeNumber):
    listIndex = 0
    for node in nodeSel:
        newName = cleanNameList[listIndex] + "_" + str(nodeNumber)
        #node.setName(newName)
        print(newName)
        nodeNumber += 1
        listIndex += 1
    return nodeNumber 

'''
#get the list of names split and remove "_" and numbers
def cleanNames(nameSplitList):
    for eachList in nameSplitList:
        cleanNameList = ["".join(char for char in item if not char.isdigit() and char != '_') for item in eachList]
  '''   

####
namesList = getNodeName(nodeSel)
cleanNameList = createCleanNames(namesList)
setNodeName(nodeSel,nodeNumber)
print(nodeNumber)


    

