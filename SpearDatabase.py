import os
import json

def InitData():
    if not os.path.isfile('SpearData.ini'):
        f = open('SpearData.ini','w')
        f.write(str("{}"))
        f.close()

def ReplaceData(tag, value):
    f = open('SpearData.ini', 'r')
    a = json.loads(f.read())
    a[tag] = value
    f.close()

    f = open('SpearData.ini', 'w')
    f.write(json.dumps(a))
    f.close()

def AppendData(tag, appendValue):
    f = open('SpearData.ini', 'r')
    a = json.loads(f.read())
    try:
        if type(a[tag]) == list:
            a[tag].append(appendValue)
    except:
        a[tag] = []
        a[tag].append(appendValue)

        
    f.close()

    f = open('SpearData.ini', 'w')
    f.write(json.dumps(a))
    f.close()


def DeleteData(tag, deleteValue):
    f = open('SpearData.ini', 'r')
    a = json.loads(f.read())
    try:
        if type(a[tag]) == list:
            a[tag].remove(deleteValue)
    except:
        return
    f.close()

    f = open('SpearData.ini', 'w')
    f.write(json.dumps(a))
    f.close()

def ReadData(tag):
    f = open('SpearData.ini', 'r')
    a = json.loads(f.read())
    f.close()

    try:
        send = a[tag]
    except:
        send = []

    return send