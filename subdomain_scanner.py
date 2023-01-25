import os, requests, time
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as nino
from colorama import Fore, init

init()

g = Fore.GREEN
r = Fore.RED
reset = Fore.RESET

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
	}

res_file = "subdomain_scan.txt"

version = 1.0

banner = f"""
   ____     __      __                _        ____                          
{g}  / __/_ __/ /  ___/ /__  __ _  ___ _(_)__    / __/______ ____  ___  ___ ____
{reset} _\ \/ // / _ \/ _  / _ \/  ' \/ _ `/ / _ \  _\ \/ __/ _ `/ _ \/ _ \/ -_) __/
{g}/___/\_,_/_.__/\_,_/\___/_/_/_/\_,_/_/_//_/ /___/\__/\_,_/_//_/_//_/\__/_/ {reset}V {r}{version}{reset}
-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}- github.com/fooster1337 {r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}-{r}-{reset}
Req Tools? contact : {r}nfex.def@protonmail.com{reset}
Format Domain : site.com (no http/https/www)
"""
def gas_subdo(domain):
	try:
		subdo_scan = "http://v1.exploits.my.id/?tools=subdomain"
		payload = {"url": f"{domain}", "subdoaktif": "on", "go": "Scan+Subdo"}
		req = requests.post(subdo_scan, data=payload, headers=headers, timeout=10).text
		soup = BeautifulSoup(req, 'html.parser')
		get_domain = soup.find('textarea').get_text()
		#get_domain_extrack = soup.a.decompose()
		filter_subdo = get_domain.replace('www.', '').replace('*.', '').replace('webmail.', '').replace('cpanel.', '').replace('images.', '').replace('ftp.', '').replace('ssl.', '').replace('cpcalendars.', '').replace('email.', '').replace('mail.', '').replace('cpcontacts.', '')
		#print(filter_subdo)
		print(f"[{g}{domain}{reset}] -> [{g}{len(str(filter_subdo))} Domain{reset}]")
		with open(res_file, 'a+') as s:
			s.write(filter_subdo)
		s.close()
		#print(domain)
	except KeyboardInterrupt:
		print("\n[ Thx for using this tools:) ]")
		exit()
	except Exception as e:
		pass

def main():
	try:
		if os.name == "nt":
			os.system("cls")
		elif os.name == "posix":
			os.system("clear")
		else:
			pass
		print(banner)
		get_list = input("Domain List > ")
		get_thread = int(input("Thread > "))
		get_domain = open(get_list).read().splitlines()#.replace("http://", '').replace("www.", '').replace("https://", '').replace("https://www.", '')
		#print(get_domain)
		with nino(max_workers=get_thread) as gas:
			for x in get_domain:
				gas.submit(gas_subdo(x))

		#for x in get_domain:
		#	print(x)
	except FileNotFoundError:
		print("file not found, try again")
		time.sleep(1)
		main()
	except KeyboardInterrupt:
		print("\n[ Thx for using this tools:) ]")
		exit()
	except Exception as e:
		print(e)
		pass

if __name__ == '__main__':
	main()
	
