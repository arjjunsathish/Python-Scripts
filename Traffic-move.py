import requests
import json
import subprocess
import pandas as pd

media = ['355821', '356006']
ip = ['202.73.37.0', '219.75.22.42', '111.65.77.0', '175.156.109.0', '116.87.197.87']
#ip = ['202.73.37.0', '219.75.22.42']
url_gpc = "https://rest-sgs1.ott.kaltura.com/api_v3/service/asset/action/getPlaybackContext"
headers_gpc = {'Content-Type': 'application/json'}
padding = ['content-type', 'content-length', 'date', 'last-modified', 'expires', 'cache-control', 'etag', 'x-vod-me', 'x-vod-session', 'access-control-allow-headers', 'access-control-expose-headers', 'access-control-allow-methods', 'access-control-allow-origin', 'timing-allow-origin', 'accept-ranges','x-proxy-me', 'x-proxy-session', 'server', 'via', 'x-amz-cf-pop', 'x-cache', 'x-amz-cf-pop', 'x-amz-cf-id']
Result = []

for x in range(len(media)):
	payload = '''{
    "apiVersion": "5.3.5","ks": "","service": "asset","action": "getPlaybackContext","assetId": "'''+media[x]+'''","assetType": "MEDIA","contextDataParams": {"objectType": "KalturaPlaybackContextOptions","context": "PLAYBACK"}}'''
	response = requests.request("POST", url_gpc, headers=headers_gpc, data=payload)
	gpc_headers = response.headers
	gpc_resp = json.loads(response.text)
	gpc_urls = gpc_resp["result"]["sources"]
	for z in range(len(ip)):
		for y in range(len(gpc_urls)):
			Headers = {}
			rest_url = gpc_urls[y]["url"]
			curl_cmd = "curl -siL "+rest_url+" --header "+ip[z]
			Headers["IP"] = ip[z]
			Headers["URL"] = rest_url
			Headers["Curl_Cmd"] = curl_cmd
			Headers["File_Type"] = gpc_resp["result"]["sources"][y]["type"]
			#print (ip[z])
			f = open('/Users/arjjunsathish/MEWATCHEXT-1264.txt', 'wb')
			curl_cmd = "curl -siL "+rest_url+" --header "+ip[z]
			subprocess.call(['curl', '-siL', 'GET', rest_url, '--header', ip[z]], stdout=f)
			f = open('/Users/arjjunsathish/MEWATCHEXT-1264.txt', 'rt', errors='replace')
			lines = f.readlines()
			print ("===================================")
			print (lines)
			print ("===================================")
			lines1 = lines[0:60]
			c = 0
			for x in lines1:
				if x.find('HTTP/') != -1 and x.find('302') != -1:
					c = c + 1
			if c > 1:
				if lines.count('HTTP/2 302 \n') > 1:
					rest_as = lines1[0:17]
					cdnapi = lines1[18:35]
					cloud_fr =  lines1[36:60]	
					gpc_headers_str_list = str(gpc_headers).split(',')
					for p in range(len(gpc_headers_str_list)):
						Headers[gpc_headers_str_list[p].split(':')[0].upper()+"_GPC"] = gpc_headers_str_list[p].split(':')[1]
					for q in range(len(rest_as)):
						t1 = rest_as[q]
						if t1.find('location') != -1 or t1.find('Location') != -1: 
							k1 = t1[0:t1.find('n: ')+1]
							Headers[k1.upper()+"_rest_as"] = t1[t1.find(': h')+2: -1]
						elif t1.find('date') != -1:
							k1 = t1[0:t1.find('e:')+1]
							Headers[k1.upper()+"_rest_as"] = t1[t1.find(': ')+1:-1]
						elif t1.find(':') != -1:
							Headers[t1.split(':')[0].upper()+"_rest_as"] = t1.split(':')[1]
					for r in range(len(cdnapi)):
						t2 = cdnapi[r]
						if t2.find('location') != -1 or t2.find('Location') != -1: 
							k2 = t2[0:t2.find('n: ')+1]
							Headers[k2.upper()+"_cdnapi"] = t2[t2.find(': h')+2: -1]
						elif t2.find('date') != -1:
							k2 = t2[0:t2.find('e:')+1]
							Headers[k2.upper()+"_cdnapi"] = t2[t2.find(': ')+1:-1]
						elif t2.find('expires') != -1:
							k2 = t2[0:t2.find('s:')+1]
							Headers[k2.upper()+"_cdnapi"] = t2[t2.find(':')+2:-1]
						elif t2.find(':') != -1:
							Headers[t2.split(':')[0].upper()+"_cdnapi"] = t2.split(':')[1]
					for s in range(len(cloud_fr)):
						t3 = cloud_fr[s]
						if t3.find(':') != -1:
							Headers[t3.split(':')[0].upper()+"_cloud_fr"] = t3.split(':')[1]
							print (t3.split(':')[0].upper()+"_cloud_fr"+":"+t3.split(':')[1])
					Result.append(Headers)
			else:
				rest_as = lines1[0:17]
				cdnapi = lines1[18:41]
				gpc_headers_str_list = str(gpc_headers).split(',')
				for p in range(len(gpc_headers_str_list)):
					Headers[gpc_headers_str_list[p].split(':')[0].upper()+"_GPC"] = gpc_headers_str_list[p].split(':')[1]
				for q in range(len(rest_as)):
					t1 = rest_as[q]
					if t1.find('location') != -1 or t1.find('Location') != -1: 
						k1 = t1[0:t1.find('n: ')+1]
						Headers[k1.upper()+"_rest_as"] = t1[t1.find(': h')+2: -1]
					elif t1.find('date') != -1:
						k1 = t1[0:t1.find('e:')+1]
						Headers[k1.upper()+"_rest_as"] = t1[t1.find(': ')+1:-1]
					elif t1.find(':') != -1:
						Headers[t1.split(':')[0].upper()+"_rest_as"] = t1.split(':')[1]
				for r in range(len(cdnapi)):
					t2 = cdnapi[r]
					if t2.find('URI') != -1 or t2.find('uri') != -1:
						t3 = t2[t2.find('URI'):-1]
						Headers["LOCATION_cdnapi"] = t3.split('=')[1]
						print (t3.split('=')[1])
					elif t2.find('date') != -1:
						k2 = t2[0:t2.find('e:')+1]
						Headers[k2.upper()+"_cdnapi"] = t2[t2.find(': ')+1:-1]
					elif t2.find('expires') != -1:
						k2 = t2[0:t2.find('s:')+1]
						Headers[k2.upper()+"_cdnapi"] = t2[t2.find(':')+2:-1]
					elif t2.find(':') != -1:
						Headers[t2.split(':')[0].upper()+"_cdnapi"] = t2.split(':')[1]
				for s in range(len(padding)):
					Headers[padding[s].upper()+"_cloud_fr"] = "No Value"
					print (t2.split(':')[0].upper()+"_cloud_fr"+":"+"No Value")
				#print (Headers)
				Result.append(Headers)

df = pd.DataFrame(Result)
df.to_csv(r"/Users/arjjunsathish/17thAprilReport-STG.csv", index=False, header=True)
