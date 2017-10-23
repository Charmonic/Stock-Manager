import uuid 
import random

def generateId():
    return str(uuid.uuid1())

def generateUPC():
    upc = ""
    i = 0
    while i < 12:
        upc += str(random.randint(0,9))
        i += 1
    return upc

def generateNameProduct():
    names = ["Asparagus","Broccoli", "Carrots", "Corn", "Potatoes", "Spinach", "Zucchini"]
    return names[random.randint(0,len(names)-1)]

def generateStockandStockLimit():
    stock = random.randint(50,200)
    stock_limit = int(stock/2-20)
    return [stock,stock_limit]

def generatePrice():
    return round(random.uniform(1,10),2)

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
def isCorrectUPC(upc):
    if isNumber(upc) == True and len(upc) == 12:
        return True
    else:
        return False
    
