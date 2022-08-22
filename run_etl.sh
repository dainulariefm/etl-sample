#!/bin/bash

file_list=("toS3Landing.py" "toStagingDB.py" "toDatawarehouse.py" "toDatamartSales.py")

for py_file in "${file_list[@]}"
do
    python3 ${py_file}
done