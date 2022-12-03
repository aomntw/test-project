import csv

import uuid
import datetime

from api.services import datapath


fields = ["id", "name", "category", "date"]


def readall():
    result = []
    with open(datapath, "r", encoding="utf8") as file:
        reader = csv.reader(file)
        for row in reader:
            result.append(row)
    file.close()
    return result


def search(name):
    data = []
    with open(datapath, "r", encoding="utf8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == name:
                data.append(row)
    file.close()

    if data:
        return {
            "count": str(len(data)),
            "data": data.insert(0, fields),
        }

    else:
        return {
            "count": str(len(data)),
            "data": "not found",
        }


def create(name, category):
    data = [str(uuid.uuid4()), name, category, str(datetime.datetime.now())]

    if readall():
        with open(datapath, "a", newline="", encoding="utf8") as file:
            writer = csv.writer(file)
            # writer.writerow(fields)
            writer.writerow(data)
        file.close()

    else:
        with open(datapath, "a", newline="", encoding="utf8") as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerow(data)
        file.close()

    return readall()


def update(id, name):
    result = []

    with open(datapath, "r", encoding="utf8") as file:
        reader = csv.reader(file)
        for row in reader:
            result.append(row)
            if row[0] == id:
                row[1] = name
    file.close()

    with open(datapath, "w", newline="", encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(result)
    file.close()

    return readall()


def delete(id):
    result = []

    with open(datapath, "r", encoding="utf8") as file:
        reader = csv.reader(file)
        for row in reader:
            result.append(row)
            if row[0] == id:
                result.remove(row)
    file.close()

    with open(datapath, "w", newline="", encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerows(result)
    file.close()

    return readall()
