'''
This tool pick a selected geo node and create a tree in the /stage area.
To work the children of the geo node must be separate nodes
Check test scene in D:\Claudio\Documents\HoudiniProjects\work2024\tool_create_sop_tree_v01
'''

import hou
import os

#select the geo node you wato to work on, return the path and name
def selectGeoNode():
    selectedNodePath = hou.ui.selectNode()
    selectedNodeName = selectedNodePath.split("/").pop(-1)
    return selectedNodePath

#takes the geo node path and name and create the sop import and set the soppath
def createSopImport(geoPath):
    geoName = geoPath.split("/").pop(-1)
    sopName = geoName + "_sopImport"
    sopPath = "/stage/" + sopName
    hou.node("/stage").createNode("sopimport").setName(sopName)
    hou.node(sopPath).parm("soppath").set(geoPath)
    return sopPath


#create a material library and connect to the sop import
def createMaterialLib(sopImportPath,geoPath):
    rootPath = "/stage"
    geoName = geoPath.split("/").pop(-1)
    matLibName = geoName + "_ml"
    matLibPath = rootPath + "/" + matLibName
    sopImportNode = hou.node(sopImportPath)
    hou.node(rootPath).createNode("materiallibrary").setName(matLibName)
    hou.node(matLibPath).setInput(0,sopImportNode,0)
    return matLibPath

#create an arnold shader for each mesh  
def createArnoldShader(geoNodePath,matLibPath):
    #fetch the list of meshes in the geo node
    meshList = []
    for child in hou.node(geoNodePath).children():
        if child.type().name() == "platonic":
            meshList.append(child.name())
    #create a shader for each in the list 
    geoNodeName = geoNodePath.split("/").pop(-1)    
    matLibNode = hou.node(matLibPath)
    for mesh in  meshList:
        #create shader
        arnoldNodeName = mesh + "_mtl"
        arnoldNodePath = matLibPath + arnoldNodeName
        matLibNode.createNode("mtlxstandard_surface",node_name=arnoldNodeName)
        #check in the texture folder and create nodes
        texturesRootPath = assetsPath + "\\" + geoNodeName + "\\textures"
        for file in os.listdir(texturesRootPath):
            if "diffuse" in file:
                diffuseNodeName = mesh + "_diffuse" + "_txt"
                diffuseNodePath = matLibPath + "/" + diffuseNodeName
                matLibNode.createNode("mtlximage",node_name=diffuseNodeName)
                #set the texture file 
                filePath = texturesRootPath + file
                hou.node(diffuseNodePath).parm("file").set(filePath)
            elif "roughness" in file:
                roughnessNodeName = mesh + "_roughness"+"_txt"
                roughnessNodePath = matLibPath + "/" + roughnessNodeName
                matLibNode.createNode("mtlximage",node_name=roughnessNodeName)
                #set the texture file
                filePath = texturesRootPath + file
                hou.node(roughnessNodePath).parm("file").set(filePath)                
            elif "normal" in file:
                normalNodeName = mesh + "_normal"+"_txt"
                normalNodePath = matLibPath + "/" + normalNodeName
                matLibNode.createNode("mtlximage",node_name=normalNodeName)
                filePath = texturesRootPath + file
                hou.node(normalNodePath).parm("file").set(filePath)         



##################################################

assetsPath = r"D:\Claudio\Documents\Projects\Environment_2024\assets"

selectedGeoPath = selectGeoNode()

sopPath = createSopImport(selectedGeoPath)

matLibPath = createMaterialLib(sopPath,selectedGeoPath)

createArnoldShader(selectedGeoPath,matLibPath)