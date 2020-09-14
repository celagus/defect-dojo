import requests
import argparse
import datetime

def get_tests(api_key, base_url):
	headers = {
		'Authorization' : 'Token '+api_key
	}
	r = requests.get(url = base_url+"/api/v2/tests/", headers=headers)
	print(r)
	print(r.text)

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--base_url', metavar='base_url', type=str, help='Base url for DefectDojo server (example: http://10.20.30.40:8080)')
parser.add_argument('-k', '--api_key', metavar='api_key', type=str, help='Token from DefectDojo')
args = parser.parse_args()

if __name__ == "__main__":
	get_tests(args.api_key,args.base_url)
