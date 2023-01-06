To run this program you can get the access key and secret key after connection to the AWS CLI and from the path 
cat ~/.aws/credentials


import boto3
import os
from boto3.session import Session
Import gzip

session = Session(aws_access_key_id = 'ASIAZ5D5XWFRGIU6TANF', aws_secret_access_key = 'GGOXRwVw0LRK3RxM95NrY3YVWJTNOfj0sr2wE5O5', region_name = 'ap-southeast-1', profile_name= 'okta')
session = boto3.Session(profile_name='okta')
s3 = session.resource('s3')
bucket = s3.Bucket('sgp2-ott-app-logs')
for obj in bucket.objects.filter(Prefix = 'logs/ott-nginx/2022/03/13/'):
	#print (obj.key)
	f = gzip.GzipFile(fileobj=obj.get()["Body"])
	content = f.read()
	print (len(content.split()))  
	A = obj.key
	B = A.split('/')
	C = B[len(B) - 1]
	D = '/Users/arjjunsathish/Documents/AWSCLI/Test'+C
	bucket.download_file(obj.key, D)
	
To Download selected files from S3:

F1 = ''' ''' # prepare selected file list
F2 = f1.split() # selected file list
for x in range(len(f2)):
	a = f2[x]
	b = a.split('/')
	c = b[len(b)-1]
	d = '/Volumes/KalturaHDD/Emeritus-Data/Phoenix/debug/'+c
	bucket.download_file(f2[x], d)
	
