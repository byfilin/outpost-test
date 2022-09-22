import csv
import re
import sys

if len(sys.argv) == 1:
    sys.stdout.write("Usage: %s <access.log> <accesslog.csv>\n"%sys.argv[0])
    sys.exit(0)

log_file_name = sys.argv[1]
csv_file_name = sys.argv[2]

pattern = re.compile(r"""(?P<ipaddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<dateandtime>\d{2}\/[a-z]{3}\/\d{4}:\d{2}:\d{2}:\d{2} (\+|\-)\d{4})\] ((\"(GET|POST) )(?P<url>.+)(http\/1\.1")) (?P<statuscode>\d{3}) (?P<bytessent>\d+) (["](?P<refferer>(\-)|(.+))["]) (["](?P<useragent>.+)["])""", re.IGNORECASE)

file = open(log_file_name)

with open(csv_file_name, 'w') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['host', 'ident', 'user', 'time', 'verb', 'url', 'httpver', 'status', 'size', 'referer', 'useragent'])

    for line in file:
        m = pattern.match(line)
        result = m.groups()
        csv_out.writerow(result)