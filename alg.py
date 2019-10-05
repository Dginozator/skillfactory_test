import requests
import json
import re

import pymysql.cursors

Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='lucy',
    password='12345',
    db='test_database',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

def loadStructCourse():
    url = 'http://analytics.skillfactory.ru:5000/api/v1.0/get_structure_course/'
    r = requests.post(url, data = {})
    answer = (json.loads(r.text))['blocks']

    outputList = []
    outputTxt = ''

    index = 0

    for key in answer:
        # if (answer[key]['type'] != 'chapter'):
            # continue

        if (getIndex (answer[key]['display_name']) is None):
            continue

        outputList.append({'display_name': answer[key]['display_name'], 'block_id': answer[key]['block_id']})
        index+=1

    outputList = sortBlocks(outputList)

    for block in outputList:
        outputTxt += block['display_name'] + ';' + block['block_id'] + '\n'

    print(outputTxt)
    print(index)

    with open('struct.txt', 'w') as dfile:
        dfile.write(outputTxt)

def sortBlocks(blocksList):
    sortedList = []

    insertFlag = 0

    for i in blocksList:
        if len(sortedList) == 0:
            sortedList.append(i)
            continue
        insertFlag = 0
        for j in sortedList:
            if (aEarlier(i['display_name'], j['display_name']) == 1):
                sortedList.insert(sortedList.index(j), i)
                insertFlag = 1
                break
        if insertFlag == 0:
            sortedList.append(i)

    return sortedList

def getIndex (name):
    result = None

    # for test 1649
    # if (re.match(r'(Модуль )?[A-Z]\d*(\.\d+)*\.?\s', name) is None):
    result = re.match(r'(Модуль )?[A-Z]\d*(\.\d+)*\.?\s', name)
    if not result is None:
        result = result.group(0)
        result = re.search (r'[A-Z]\d*(\.\d+)*', result)
        result = result.group(0)

    return (result)

# 0 - 'a' not earlier, 1 - 'a' earlier
def aEarlier (a, b):
    result = None
    aList = parseIndex(getIndex (a))
    bList = parseIndex(getIndex (b))

    posMax = min([len(aList), len(bList)])

    for pos in range(posMax):
        if (aList[pos] < bList[pos]):
            result = 1
            break
        elif (aList[pos] > bList[pos]):
            result = 0
            break

    if result is None:
        if len(aList) < len(bList):
            result = 1
        else:
            result = 0

    return (result)

def parseIndex (index):
    subindexes = re.findall(r'([A-Z]|\d+)', index)
    result = []

    for i in subindexes:
        try:
            result.append(int(i))
        except:
            result.append(i)

    return (result)

def createTable():
    try:
        with connection.cursor() as cursor:
            sql = "DROP TABLE IF EXISTS `Modules`;"
            sql += "CREATE TABLE `Modules` ( \
                id INT NOT NULL AUTO_INCREMENT,\
                name TEXT,\
                block_id TEXT,\
                update_time TIMESTAMP,\
                PRIMARY KEY (id)\
            );"
            cursor.execute(sql)
        connection.commit()
    except:
        pass
    finally:
        connection.close()

def example():
    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(sql, ('webmaster@python.org',))
            result = cursor.fetchone()
            print(result)
    finally:
        connection.close()

createTable()
# loadStructCourse()
