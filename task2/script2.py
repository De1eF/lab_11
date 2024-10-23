import json

elementsArr = ()
requestedElement = input("Enter element name: ")
fileName = "task2/elements.json"
with open(fileName, "r") as elements:
    elementsArr = json.load(elements)["elements"]
    elementsDict = {el["name"]: el["mass"] for el in elementsArr}
    if (not requestedElement in elementsDict):
        print("No ", requestedElement, " in database")
        exit()
    print("Mass of ", requestedElement, " is: ", elementsDict[requestedElement])
