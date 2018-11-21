import requests
import random
import blog.pymysql_
from bs4 import BeautifulSoup

def get_ip_list(url, headers):
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        dict={}
        dict['ip']=tds[1].text
        dict['port']=tds[2].text
        ip_list.append(dict)
    return ip_list


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


#调用

url = 'http://www.xicidaili.com/nn/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
ip_list = get_ip_list(url, headers=headers)
print(ip_list)
blog.pymysql_.insert(ip_list)
#proxies = get_random_ip(ip_list)
# 这个 proxies  就是要填入的代理IP
# requests.get(url1, proxies=proxies, headers=headers)
