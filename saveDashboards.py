import argparse
import json
from dashboardApi import *
from commons import *

parser = argparse.ArgumentParser()
parser.add_argument('path',  help='folder path to save dashboards')
args = parser.parse_args()

folder_path = args.path

def get_all_dashboards_in_grafana():
    dashboards = search_dashboard()
    print "There are {0} dashboards:".format(len(dashboards))
    for board in dashboards:
        print board['title']
    return dashboards

def save_dashboard_setting(file_name, board_data):
    file_path = folder_path + '/' + file_name + '.dashboard'
    with open(file_path , 'w') as f:
        json.dump(board_data, f)
    print "dashboard:{0} are saved to {1}".format(file_name, file_path)

def get_indivisual_dashboard_setting_and_save(dashboards):
    for board in dashboards:
        status_code, board_data = get_dashboard(board['uri'])
        if status_code == 200:
            #print(board_data)
            save_dashboard_setting(board_data['meta']['slug'], board_data)

dashboards = get_all_dashboards_in_grafana()
print_horizontal_line()
get_indivisual_dashboard_setting_and_save(dashboards)
print_horizontal_line()
