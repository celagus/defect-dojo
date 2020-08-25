import requests
import argparse
import datetime

def import_xml_test(api_key, engagement_id, test_type, scan_file, base_url):
	date = datetime.datetime.now()
	headers = {
		'Authorization' : 'Token '+api_key
	}
	data = {
		'scan_date' : date.strftime("%Y-%m-%d"),
		'minimum_severity' : 'Info',
		'active' : 'true',
		'verified' : 'true',
		'scan_type' : test_type,
		'engagement' : engagement_id,
		'close_old_findings' : 'true'	}
	files = { "file": open(scan_file, 'r') }
	r = requests.post(
		url = base_url+"/api/v2/import-scan/", headers=headers,data=data,files=files)
	print(r)
	print(r.text)

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--base_url', metavar='base_url', type=str, help='Url example: http://10.20.30.40:8080')
parser.add_argument('-k', '--api_key', metavar='api_key', type=str, help='Token from DefectDojo')
parser.add_argument('-f', '--file_name', metavar='file_name', type=str, help='File name for XML report')
parser.add_argument('-e', '--engagement_id', metavar='engagement_id', type=int, help='Engagement number from DefectDojo')
parser.add_argument('-t', '--test_type', metavar='test_type', type=str, help='Test type name from DefectDojo')
args = parser.parse_args()

if __name__ == "__main__":
	import_xml_test(args.api_key,args.engagement_id,args.test_type,args.file_name,args.base_url)

