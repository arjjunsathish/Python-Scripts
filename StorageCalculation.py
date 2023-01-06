To Provide the monthly storage:

import requests
import json
import xml.etree.ElementTree as ET
import pandas as pd
import csv
import xlrd
import openpyxl


url = 'https://www.kaltura.com/api_v3/service/flavorAsset/action/getByEntryId'
header = {'Content-Type': 'application/json'}

[{Period('2020', 'A-DEC'): {Period('2020-01', 'M'): 7541786, Period('2020-02', 'M'): 7568818, Period('2020-03', 'M'): 7595959, Period('2020-04', 'M'): 7623774, Period('2020-05', 'M'): 15227977, Period('2020-06', 'M'): 15254445, Period('2020-07', 'M'): 15285977, Period('2020-08', 'M'): 15329969, Period('2020-09', 'M'): 15358790, Period('2020-10', 'M'): 15388477, Period('2020-11', 'M'): 15419252, Period('2020-12', 'M'): 15472219}}, {Period('2021', 'A-DEC'): {Period('2021-01', 'M'): 6135684, Period('2021-03', 'M'): 7756086, Period('2021-05', 'M'): 9865790, Period('2021-07', 'M'): 9884728, Period('2021-08', 'M'): 13896717, Period('2021-09', 'M'): 16211578, Period('2021-10', 'M'): 18683527, Period('2021-11', 'M'): 25084282, Period('2021-12', 'M'): 27461262}}]


Year_list = []
df = pd.read_csv("/Users/arjjunsathish/Documents/V18-storage-voot-kids-Aug1.csv")
df = pd.read_csv("/Users/arjjunsathish/Documents/Test.csv")
df['CreateDate'] = pd.to_datetime(df['CreateDate'])
p = pd.DatetimeIndex(df.CreateDate).to_period("Y")
g = df.groupby(p)
for k, i in g:
	#print (g.get_group(k)
	b1 = {}
	a = g.get_group(k)
	p1 = pd.DatetimeIndex(a.CreateDate).to_period("M")
	g1 = a.groupby(p1)
	s = 0
	b2 = {}
	for k1, i1 in g1:
		#print (g1.get_group(k1))
		#s = 0
		a1 = g1.get_group(k1)
		entries1 = list(a1['EntryId'])
		for x in range(len(entries1)):
			if len(entries1[0]) > 0:
				data = '''{"ks" : "","entryId" : "'''+entries1[x]+'''"}'''
				r = requests.request("POST", url, headers = header, data=data)
				root = ET.fromstring(r.text)
				if root[0][0].tag != 'error':
				#if len(root[0].findall('error')) == 0 or len(root[0].findall('item')) > 0:
					#l1 = []
					l2 = []
					for y in range(len(root[0].findall('item'))):
						#l1.append(root[0][y].find('id').text)
						l2.append(int(root[0][y].find('size').text))
					for y1 in range(len(l2)):
						s = s + int(l2[y1])
		b2[str(k1)] = s
		#print (b2)
	b1[str(k)] = b2
	Year_list.append(b1)
	
