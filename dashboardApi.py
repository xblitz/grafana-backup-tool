import requests
from grafanaSettings import *

def search_dashboard():
    print "search dashboard in grafana:"
    r = send_grafana_get(grafana_url + '/api/search/')
    return r.json()

def get_dashboard(board_uri):
    r = send_grafana_get(grafana_url + "/api/dashboards/{0}".format(board_uri))
    print "query dashboard:{0}, status:{1}".format(board_uri, r.status_code)
    return (r.status_code, r.json())

def update_or_create_dashboard(payload):
    r = send_grafana_post(grafana_url + '/api/dashboards/db', payload)
    print "status: {0}".format(r.status_code)
    print "msg: {0}".format(r.content)
    return int(r.status_code)

def search_datasource():
    r = send_grafana_get(grafana_url + '/api/datasources')
    print "search datasources in grafana:"
    return r.json()

def create_datasource(payload):
    r = send_grafana_post(grafana_url + '/api/datasources', payload)
    status_code = r.status_code
    print "status: {0}".format(status_code)
    print "msg: {0}".format(r.content)
    return int(status_code)

def send_grafana_get(url):
    return requests.get(url, headers=http_get_headers)

def send_grafana_post(url, payload):
    return requests.post(url, headers=http_post_headers, json=payload)
