
# This script was written by @agustincelano to be used as an integration between a Jenkins pipeline job and DefectDojo, please check args needed!

import requests
import argparse
from datetime import datetime, timedelta
import re

def create_engagement(base_url, api_key, build_id, job_name):
	date_start = datetime.today()
	date_end = datetime.today() + timedelta(30) 
	headers = {
		'Authorization' : 'Token '+api_key
	}
	data = {
		'target_start' : date_start.strftime("%Y-%m-%d"),
		'target_end' : date_end.strftime("%Y-%m-%d"),
		'active' : 'true',
		'product' : product_id,
		'active' : 'true',
		'build_id' : build_id,
		'name' : 'JenkinsVA'+str(build_id),
		'description' : 'Jenkins job '+job_name+' build: '+str(build_id)
	}
	r = requests.post( url = base_url+"/api/v2/engagements/", headers=headers,data=data )
	#print(r)
	#print(r.text)
	x = re.search("\"id\"\:([0-9]*)", r.text)
	id = x.group()
	print(id[5:])

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--base_url', metavar='base_url', type=str, help='Base url for DefectDojo server (example: http://10.20.30.40:8080)')
parser.add_argument('-k', '--api_key', metavar='api_key', type=str, help='Token from DefectDojo')
parser.add_argument('-p', '--product_id', metavar='product_id', type=int, help='Product ID from DefectDojo (example: 2)')
parser.add_argument('-i', '--build_id', metavar='build_id', type=int, help='Jenkins job build number')
parser.add_argument('-j', '--job_name', metavar='job_name', type=str, help='Jenkins job name')
args = parser.parse_args()

if __name__ == "__main__":
	create_engagement(args.base_url, args.api_key, args.build_id, args.job_name)
