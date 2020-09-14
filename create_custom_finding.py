import requests
import argparse
import datetime

def create_finding(api_key, base_url, test_id):
	date = datetime.datetime.now()
	headers = {
		'Authorization' : 'Token '+api_key
	}
	data = {
		'date' : date.strftime("%Y-%m-%d"),
		'test' : test_id, #you must create a test or use a previously created test and get test_id 
		'found_by' : 1, #id from users table (1=admin)
		'severity' : 'Medium', #Info-Low-Medium-High-Critical
		'description' : 'A desviation has been found', #a finding description
		'title' : 'Finding Found', #a finding title
		'impact' : 'Moderated', #a description about impact
		'mitigation' : 'Fix it!', #a description about mitigation
		'numerical_severity': 3, #1-4
		'active' : 'true',
		'verified' : 'true',
		'scan_type' : 'Ansible Playbook' #scan type could be native or customized (you must to create previously)
	}
	r = requests.post(url = base_url+"/api/v2/findings/", headers=headers,data=data)
	print(r)
	print(r.text)

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--base_url', metavar='base_url', type=str, help='Base url for DefectDojo server (example: http://10.20.30.40:8080)')
parser.add_argument('-k', '--api_key', metavar='api_key', type=str, help='Token from DefectDojo')
parser.add_argument('-ti', '--test_id', metavar='test_id', type=int, help='Currently existing or custom test id you created for engagement')
args = parser.parse_args()

if __name__ == "__main__":
	create_finding(args.api_key,args.base_url,args.test_id)
