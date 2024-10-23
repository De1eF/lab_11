import json

elementsArr = ()
selectedOperation = input("Select operation, (m) - find mass by name, (n) - find data by first letter of name: ")
fileName = "task2/elements.json"

def selectOperation(elDic):
    if (selectedOperation == "m"):
        findByMassFromDic(elDic)
    elif (selectedOperation == "n"):
        getDataOfElementsStartingWith(elDic)
    else:
        print("Unknown action")
        
def getDataOfElementsStartingWith(elDic):
    symbol = input("Letter: ")
    elDicc = dict(elDic)
    for el in elDicc.items():
        if str(el[0][0]).lower() == symbol.lower():
            print("Mass of ", el[0], " is: ", el[1])

def findByMassFromDic(elDic):
    requestedElement = input("Enter element name: ")
    if (not requestedElement in elDic):
        print("No ", requestedElement, " in database")
        exit()
    print("Mass of ", requestedElement, " is: ", elDic[requestedElement])
        
with open(fileName, "r") as elements:
    elementsArr = json.load(elements)["elements"]
    elementsDict = {el["name"]: el["mass"] for el in elementsArr}
    selectOperation(elementsDict)