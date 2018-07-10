
import csv

f = open('log_b.txt',mode='r')
new_log = open('log_a.csv','a')
writer = csv.writer(new_log)
writer.writerow(['Ip','Time','Request_Type','Serverside_Status','num_of_bytes','URL'])
for line in f:

    info = line.split('"')
    i = info[1]

    ip = i.split(' ')
    final_ip = ip[0]
    time = ip[3]

    codes = info[5]
    code_split = codes.split(' ')

    request_type = info[3]
    serverside_status = code_split[1]
    num_of_bytes= code_split[2]
    url = info[7]

    collate = [final_ip,time,request_type,serverside_status,num_of_bytes,url]
    writer.writerow(collate)
