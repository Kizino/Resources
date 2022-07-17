import subprocess
import re

def get_nslookup_info(url, flag):
    # Flag: "Address", "Name"
    process = subprocess.Popen(
        ["nslookup", url], stdout=subprocess.PIPE)
    output = str(process.communicate()[0]).split('\\n')

    ip_arr = []
    for data in output:
        if flag in data:
            ip_arr.append(re.sub(f'{flag}: |{flag}:\\\\','',data))
    ip_arr.pop(0)

    return (url, ip_arr)

if __name__ == "__main__":
    hostname, ip_address = get_nslookup_info('www.realtor.com', 'Address')
    print(f'{hostname}\'s IP Address: {ip_address}')
    
    hostname, name = get_nslookup_info('www.realtor.com', 'Name')
    print(f'{hostname}\'s name: {name}')