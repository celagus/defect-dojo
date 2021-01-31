
# This script was written by @agustincelano to be used as an integration between a Jenkins pipeline job and DefectDojo, please check args needed!

import requests
import argparse
from datetime import datetime, timedelta
import re

def create_engagement(base_url, api_key):
	date_start = datetime.today()
	date_end = datetime.today() + timedelta(30) 
	headers = {
		'Authorization' : 'Token '+api_key
	}
	data = {
		'prod_type': 1,
		'name' : 'Github Actions CI',
		'description' : 'Just for test purposes'
	}
	r = requests.post( url = base_url+"/api/v2/products/", headers=headers, data=data, verify=False )

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--base_url', metavar='base_url', type=str, help='Base url for DefectDojo server (example: http://10.20.30.40:8080)')
parser.add_argument('-k', '--api_key', metavar='api_key', type=str, help='Token from DefectDojo')
args = parser.parse_args()

if __name__ == "__main__":
	create_engagement(args.base_url, args.api_key)
