#!/usr/bin/python
#COMPLETED CODE ON AUG, 26 2017. APROX. 5:45 A.M.
	#Maybe attempt the range method of counting the IP addr. for now listing all numbers will have to do.
#python3.5
#Have to download some modules such as; ipaddress and setuptools.

import socket,sys,time,datetime,argparse,os,subprocess

ans=True
while ans:
	print ("""
	1. Scan All hosts.
	2. Scan Ports of One Host.
	""")
	ans=input("Choose and option ")
	if ans=="1":
		line = "+" * 40
		banner = line+'''\nNetwork Map\n'''+line+"\n"
		print (banner)
		ip = input("Input a Network I.E. 10.1.1.\n " )
		nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,
101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,
176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,
250,251,252,253,254,255]
		for num in nums:
				
			result = subprocess.Popen(["ping", "-c", "1", "-W", "1", ip + str(num)]).wait()
				
			if result:         
				print ( "inactive")
					
			else:
				print ( " ACTIVE HOST! \n  ACTIVE HOST! \n  ACTIVE HOST! \n ")
				 
			
	elif ans=="2":		
				host = input("Enter Host IP & HIT ENTER TWICE:")		
				os.system('')
				line = "+" * 80
				desc = line+'''\nA Simple port scanner\n'''+line+"\n"


open_ports = []
flag = 1
common_ports = {

	'21': 'FTP',
	'22': 'SSH',
	'23': 'TELNET',
	'25': 'SMTP',
	'53': 'DNS',
	'69': 'TFTP',
	'80': 'HTTP',
	'109': 'POP2',
	'110': 'POP3',
	'115': 'Simple File Transfer Protocol',
	'123': 'NTP',
	'137': 'NETBIOS-NS',
	'138': 'NETBIOS-DGM',
	'139': 'NETBIOS-SSN',
	'143': 'IMAP',
	'156': 'SQL-SERVER',
	'161': 'Simple network protocol mngmt',
	'162': 'Simple network protocol mngmt trap',
	'389': 'LDAP',
	'443': 'HTTPS',
	'445': 'SMB',
	'464': 'Kerbos Change/set PASS',
	'512': 'Remote Process Execution',
	'513': 'Who',
	'514': 'syslog',
	'543': 'Kerbos login',
	'547': 'Kerbos shell',
	'546': 'DHCP-CLIENT',
	'547': 'DHCP-SERVER',
	'636': 'LDAP over SSL',
	'995': 'POP3-SSL',
	'993': 'IMAP-SSL',
	'1524': 'ingreslock,ingres',
	'2049': 'Network File system NFS',
	'2086': 'WHM/CPANEL',
	'2087': 'WHM/CPANEL',
	'3306': 'MYSQL',
	'5900': 'Remote frame buffer protocol/ VNC',
	'6000': 'X11',
	'8005': 'tomcat remote shutdown',
	'8080': 'Apache Tomcat',
	'8180': 'server monitoring',
	'8443': 'PLESK',
	'10000': 'VIRTUALMIN/WEBMIN'
}

starting_time = time.time()
print ("+" * 40)
print ("\tSimple Port Scanner!")
print ("+" * 40)

if (flag):
	print ("Scanning for most common ports on %s" % (host))
else:
	print ("Scanning %s from port %s - %s: " % (host, start_port, end_port))
print ("Scanning Started at %s " % (time.strftime("%I:%M:%S %p")))

def check_port(host, port, result = 1):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		r = sock.connect_ex((host,port))
		if r == 0: 
			result = r
		sock.close()
	except Exception as e:
		pass

	return result
def get_service(port):
	port = str(port)
	if port in common_ports:
		return common_ports[port]
	else:
		return 0

try:
	print ("Scanning in progress...")
	print ("Connecting to port: ",)

	if flag:
		for p in sorted(common_ports):
			sys.stdout.flush()
			p = int(p)
			print (p),
			response = check_port(host, p)
			if response == 0:
				open_ports.append(p)
				sys.stdout.write('\b' * len(str(p)))
	else:

		for p in range(start_port, end_port+1):
			sys.stdout.flush()
			print (p),
			response = check_port(host, p)
			if response == 0:
				open_ports.append(p)
			if not p == end_port:
				sys.stdout.write('\b' * len(str(p)))

	print ("\nScanning completed at %s" %(time.strftime("%I:%M:%S %p")))
	ending_time = time.time()
	total_time = ending_time - starting_time
	print ("=" * 40)
	print ("\tScan Report: %s" %(host))
	print ("=" * 40)
	if total_time:
		total_time = str(round(total_time, 2))
		print ("scan took %s seconds" %(total_time))
	else:
		total_time = total_time / 60
		print ("Scan took %s minutes" %(total_time))

	if open_ports:
		print ("open ports: ")
		for i in sorted(open_ports):
			service = get_service(i)
			if not service:
				service = "Unknown service"
			print ("\t%s %s: Open" % (i, service))
	else:
		print ("Sorry, no open ports found!")

except KeyboardInterrupt:
	print ("You pressed Ctrl+C. Exiting ")
	sys.exit(1)

