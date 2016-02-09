#!/usr/bin/env python3

#Prints list of Unique Ids in JSON Array file that were not found in CSV file
#Usage (Bash): ./missing-records.py csvFile.csv jsonArrayFile.csv csvUniqueValuesColumnName jsonUniqueValuesFieldName

import csv
import json
import sys

columnIndex = 0
csvColumnList = []
jsonFieldList = []

with open(sys.argv[1], 'r', encoding='utf-8') as csvFile:
	csvData = csv.reader(csvFile)
	headers = next(csvData)
	columnIndex = headers.index(sys.argv[3])
	csvColumnList = [str(row[columnIndex]) for row in csvData]
	csvFile.close()

with open(sys.argv[2], 'r', encoding='utf-8') as jsonArrayFile:
	jsonArrayData = json.loads(jsonArrayFile.read())
	jsonFieldList = [str(jsonSet[sys.argv[4]]) for jsonSet in jsonArrayData]
	jsonArrayFile.close()


print(','.join(set(jsonFieldList)-set(csvColumnList)))
