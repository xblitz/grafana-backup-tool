#!/bin/bash

DATE=`date +%Y_%m_%d_%H%M`
BACKUP_FOLDER=/tmp/grafana

mkdir -p $BACKUP_FOLDER/tmp/dashboards
mkdir -p $BACKUP_FOLDER/tmp/datasouces

python saveDashboards.py $BACKUP_FOLDER/tmp/dashboards
python saveDatasources.py $BACKUP_FOLDER/tmp/datasouces

tar -zcvf $BACKUP_FOLDER/grafana_$DATE.tar.gz $BACKUP_FOLDER/tmp

rm -r $BACKUP_FOLDER/tmp
