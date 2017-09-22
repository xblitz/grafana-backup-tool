import json, sys, re, argparse
from dashboardApi import *

parser = argparse.ArgumentParser()
parser.add_argument('path',  help='File path of datasource JSON')
args = parser.parse_args()

file_path = args.path

with open(file_path, 'r') as f:
    file_data = json.load(f)

print("create datasource: {}".format(file_data['name']))
create_datasource(file_data)
