import requests
import argparse
import datetime

def create_test(api_key, engagement_id, test_type, base_url):
        date_start = datetime.datetime.now()
        date_end = datetime.datetime.now() + datetime.timedelta(days=30) #this add 30 days from now
	headers = {
		'Authorization' : 'Token '+api_key
	}
	data = {
		'target_start' : date_start,
		'target_end' : date_end,
		'test_type' : test_type, #must be native or created by you
		'engagement' : engagement_id, #must be exist or created by you
	}
	r = requests.post(url = base_url+"/api/v2/tests/", headers=headers, data=data)
	print(r)
	print(r.text)

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--base_url', metavar='base_url', type=str, help='Base url for DefectDojo server (example: http://10.20.30.40:8080)')
parser.add_argument('-k', '--api_key', metavar='api_key', type=str, help='Token from DefectDojo')
parser.add_argument('-e', '--engagement_id', metavar='engagement_id', type=int, help='Engagement number from DefectDojo')
parser.add_argument('-t', '--test_type', metavar='test_type', type=str, help='Test type name from DefectDojo')
args = parser.parse_args()

if __name__ == "__main__":
	create_test(args.api_key, args.engagement_id, args.test_type, args.base_url)

