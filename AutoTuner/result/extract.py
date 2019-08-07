# -*- coding: utf-8 -*-
"""
Extract data from log
"""
import re
import sys

log_path = sys.argv[1]

with open(log_path, 'r') as log_file, open('data.csv', 'w') as data_file:
    data_file.write("Episode, Step, TPS, LAT, QPS, Reward, Score\n")
    for line in log_file.readlines():
        if 'Reward' in line:
            #raw_data = re.findall('(-\d+\.\d+|\d+\.\d+|\d+)', line)
            raw_data = re.findall(r'-?\d+\.?\d*e?-?\d*', line)
            raw_data = [float(x) for x in raw_data]
            for item in raw_data[:-1]:
                data_file.write("%f, " % item)
            data_file.write("%f\n" % raw_data[-1])

