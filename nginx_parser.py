#!/usr/bin/env python
import sys
import re
import csv
import subprocess


# 1. Get params - log file, output csv file, commit log
log_file_name = sys.argv[1]
csv_file_name = sys.argv[2]
try:
    commit_message = sys.argv[3]
except:
    commit_message = "Add nginx csv log"

# 2. Parse file with regexp
pattern = re.compile(r'(?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<datetime>\d{2}\/[A-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})\] ((?P<getpost>\"(GET|POST) )(?P<url>.+)\") (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>.+)["]) (["](?P<useragent>.+)["]) (?P<num1>\d+) (?P<num2>\d+.\d+) \[(?P<user>.+)\] (?P<brack>\[\]) (?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,4}) (?P<num3>\d+) (?P<num4>\d+.\d+) (?P<code>\d+) (?P<id>.+)')

csv_header = ['host', 'datetime', 'getpost', 'url', 'statuscode', 'bytessent', 'refferer', 'useragent', 'num1', 'num2', 'user', 'brack', 'ip', 'num3', 'num4', 'code', 'id']

file = open(log_file_name)

# 3. Save outout to file
with open(csv_file_name, 'w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(csv_header)
    for line in file.readlines():
        m = re.search(pattern, line)
        if m:
            result = [m.group('host'), m.group('datetime'), m.group('getpost'), m.group('url'), m.group('statuscode'), m.group('bytessent'), \
                      m.group('refferer'), m.group('useragent'), m.group('num1'), m.group('num2'), m.group('user'), m.group('brack'), m.group('ip'), \
                      m.group('num3'), m.group('num4'), m.group('code'), m.group('id') ]
            csv_out.writerow(result)

file.close()

# 4. Add file to git
subprocess.run(["git", "add", f"{csv_file_name}"])
subprocess.run(["git", "commit", "-am", f"{commit_message}"])

