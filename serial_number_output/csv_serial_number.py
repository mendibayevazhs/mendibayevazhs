import csv
import re
from pprint import pprint
with open("serial_number.txt") as src, open("serial_number.csv", 'a', newline='') as dst:
    for line in src:
        line_list = line.split()
        if "hostname" in line:
            host_name =  line.split()[-1]
        elif "IP ADDRESS: " in line:
            IP_ADDRESS = line.split()[-1]
        elif "System serial number" in line or "System Serial Number" in line:
            serial_number = line.split()[-1]
            output = [host_name, IP_ADDRESS, serial_number]
            print(output)
            devwriter = csv.writer(dst)
            devwriter.writerow(output)
