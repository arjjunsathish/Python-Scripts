import boto3
import os
from boto3.session import Session
import gzip

session = Session(aws_access_key_id = 'ASIAZ5D5XWFRGIU6TANF', aws_secret_access_key = 'GGOXRwVw0LRK3RxM95NrY3YVWJTNOfj0sr2wE5O5', region_name = 'ap-southeast-1', profile_name= 'okta')
session = boto3.Session(profile_name='okta')
s3 = session.resource('s3')
bucket = s3.Bucket('sgp2-ott-app-logs')
path = ['logs/ott-nginx/2022/05/03/',
'logs/ott-nginx/2022/05/05/',
'logs/ott-nginx/2022/05/04/',
'logs/ott-nginx/2022/05/22/',
'logs/ott-nginx/2022/05/27/',
'logs/ott-nginx/2022/05/27/']
for x in range(len(path)):
	for obj in bucket.objects.filter(Prefix = 'logs/ott-nginx/2022/03/13/'):
		#print (obj.key)  
		A = obj.key
		B = A.split('/')
		C = B[len(B) - 1]
		if path[x].find('/05/03') != -1:
			D = '/Volumes/Arjjun5TB/Astro-autologout/Nginx/3rdMay/'+C
			bucket.download_file(obj.key, D)
		if path[x].find('/05/04') != -1:
			D = '/Volumes/Arjjun5TB/Astro-autologout/Nginx/4thMay/'+C
			bucket.download_file(obj.key, D)
		if path[x].find('/05/05') != -1:
			D = '/Volumes/Arjjun5TB/Astro-autologout/Nginx/5thMay/'+C
			bucket.download_file(obj.key, D)
		if path[x].find('/05/22') != -1:
			D = '/Volumes/Arjjun5TB/Astro-autologout/Nginx/22ndMay/'+C
			bucket.download_file(obj.key, D)
		if path[x].find('/05/27') != -1:
			D = '/Volumes/Arjjun5TB/Astro-autologout/Nginx/27thMay/'+C
			bucket.download_file(obj.key, D)
		if path[x].find('/05/29') != -1:
			D = '/Volumes/Arjjun5TB/Astro-autologout/Nginx/29thMay/'+C
			bucket.download_file(obj.key, D)
