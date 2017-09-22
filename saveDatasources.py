import argparse
import json
from dashboardApi import *
from commons import *

parser = argparse.ArgumentParser()
parser.add_argument('path',  help='folder path to save datasources')
args = parser.parse_args()

folder_path = args.path

def save_datasource(file_name, datasource_setting):
    file_path = folder_path + '/' + file_name + '.datasource'
    with open(file_path, 'w') as f:
        json.dump(datasource_setting, f)
        print "datasource:{0} is saved to {1}".format(file_name, file_path)

def get_all_datasources_and_save():
    datasources = search_datasource()
    print "There are {0} datasources:".format(len(datasources))
    for datasource in datasources:
        #print datasource['name']
        filename = "{}-{}".format(datasource['id'],"".join(x for x in datasource['name'] if x.isalnum()))
        save_datasource(filename, datasource)


get_all_datasources_and_save()
print_horizontal_line()
