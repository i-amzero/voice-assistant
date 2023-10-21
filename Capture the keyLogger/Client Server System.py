import requests
working_ip_list = []
not_working = []
try:
    with open('proxies.txt','r') as f:
        for x in f.readlines():
            res = requests.get('https://httpbin.org/ip',proxies=x)
            if res.status_code == 200:
                working_ip_list.append(x)
            not_working.append(x)
except:
    print("Something went wrong")




