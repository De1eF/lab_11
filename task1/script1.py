import csv

filename = "task1/dns.csv"
ips = dict()

with open(filename, "r") as fd:
    reader = csv.reader(fd, delimiter="\t")
    for row in reader:
        rowSplit = row[0].split(",")
        ips[rowSplit[0]] = ips.get(rowSplit[0], rowSplit[1])

ipToFind = input("Enter IP address: ")
print("URL for ip is: ", ips[ipToFind])
