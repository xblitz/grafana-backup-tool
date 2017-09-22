import json, sys, re, argparse
from dashboardApi import *

parser = argparse.ArgumentParser()
parser.add_argument('path',  help='File path of dashboard JSON')
args = parser.parse_args()

file_path = args.path

with open(file_path, 'r') as f:
    file_data = json.load(f)

file_data['dashboard']['id'] = None
db = {'dashboard': file_data['dashboard']}
update_or_create_dashboard(db)

