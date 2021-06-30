import requests
import argparse
from datetime import datetime,timedelta
from dataclasses import dataclass
import json
import sys
import string

@dataclass
class Finding(object):
    date: str
    test: int
    found_by: int
    severity: str
    description: str
    title: str = None
    impact: str = None
    mitigation: str = None
    numerical_severity: int = 1
    active: bool = True
    verified: bool = True
    scan_type: str = 'Static Check'

def severity_mapping(severity):
    if severity == 'LOW':
        return 4
    if severity == 'MEDIUM':
        return 3
    if severity == 'HIGH':
        return 2
    if severity == 'CRITICAL':
        return 1

def import_findings(input_file, test_id):
    finding = Finding
    output = []
    json_array = json.load(input_file)
    findings_list = json_array['results']['violations']
    date = datetime.now()
    for f in findings_list:
       finding.date = date.strftime("%Y-%m-%d")
       finding.test = test_id
       finding.found_by = 1
       finding.severity = string.capwords(f['severity'])
       finding.description = f['description']
       finding.title = f['resource_name']+" vulnerability related to "+f['rule_name']
       finding.numerical_severity = severity_mapping(f['severity'])
       output.append(finding)
    return output
       
def create_finding(api_key, base_url, engagement_id, findings):
    headers = {
        'Authorization' : 'Token '+api_key
    }
    for finding in findings:
        data = {
            'date' : finding.date,
            'test' : finding.test,
            'found_by' : finding.found_by,
            'severity' : finding.severity,
            'description' : finding.description,
            'title' : finding.title,
            'impact' : finding.impact,
            'mitigation' : finding.mitigation,
            'numerical_severity' : finding.numerical_severity,
            'active' : finding.active,
            'verified' : finding.verified,
            'scan_type' : finding.scan_type
        }
        r = requests.post(url = base_url+"/api/v2/findings/", headers=headers,data=data)
        print(r.text)

def create_test(api_key, base_url, engagement_id):
    date = datetime.now()
    date_end =  datetime.now()+timedelta(days=30)
    data = {
        'target_start': date.isoformat(),
        'target_end': date_end.isoformat(),
        'test_type': 2,
        'engagement': engagement_id
    }
    headers = {
        'Authorization' : 'Token '+api_key
    }
    r = requests.post(url = base_url+"/api/v2/tests/", headers=headers,data=data)
    js = json.loads(r.text)
    return(js['id'])

parser = argparse.ArgumentParser()
parser.add_argument('-b', '--base_url', metavar='base_url', type=str, help='Base url for DefectDojo server (example: http://10.20.30.40:8080)')
parser.add_argument('-k', '--api_key', metavar='api_key', type=str, help='Token from DefectDojo')
parser.add_argument('-e', '--engagement_id', metavar='engagement_id', type=int, help='Engagement number from DefectDojo')
parser.add_argument('-f', '--input_file', metavar='input_file', type=argparse.FileType('r'), default=sys.stdin, help='Terrascan JSON output')

args = parser.parse_args()

if __name__ == "__main__":
    test_id = create_test(args.api_key,args.base_url,args.engagement_id)
    create_finding(args.api_key,
                   args.base_url,
                   args.engagement_id,
                   import_findings(args.input_file, test_id)
                   )