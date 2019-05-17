#!/usr/bin/python
import sys
import time as t 
from PIL import Image
import collections
import matplotlib.pyplot as plt
from datetime import date
from datetime import time
from datetime import datetime

def customreportgen():
	ips={}
	gps={}
	hps={}
#path = '/opt/trafficserver/var/log/trafficserver/custom_ats_2.log*'
#files = glob.glob(path)   
	logs = open("/tmp/custom_ats_2.log-20190110", "r").readlines()
#for logs in files:
	for line in logs:
		ip = line.split(" ")[2]
		exact = ip.split("=")[1]
		if 6 < len(exact) <= 15:
			ips[exact] = ips.get(exact, 0) + 1
#	print(ips)
	#temp = datetime.time(datetime.now())
	#save_stdout = sys.stdout
	#fh = open("client","w")
	#sys.stdout = fh
	#ipadr = ips.split(" ")[2]
		data = tuple(ips.items())
	#print data
	
	x_val = [x[0] for x in data]
	y_val = [x[1] for x in data]

	print x_val
	print y_val
	plt.plot(x_val,y_val, label = 'Requets')
	plt.plot(x_val,y_val)
	plt.plot(x_val,y_val,'or', color='green', linestyle='dashed', linewidth = 3, 
         	marker='o', markerfacecolor='blue', markersize=12)
	plt.title('ATS Res/Req(IP vs No of Req) Report')
	plt.xlabel('Client IP-s')
#plt.plot(y_val, label = 'Requets')
	plt.ylabel('No of requets')
	plt.savefig('reqs.png')
	t.sleep(5)
	im = Image.open("reqs.png")
	rgb_im = im.convert('RGB')
	rgb_im.save('reqs.jpg')
	#ipps = dict(ipps)
        #Data = collections.namedtuple('data', 'IP count')
	#data = list(Data(*item) for item in ips.items())
	
	#for var in range(len(ipps)):
        #        print(ipps[var])
	#sys.stdout = save_stdout
	#fh.close()
	#t.sleep(5)
	plt.close('all')

def errorreportgen():
        #ips={}
	gps={}
	#logs = open("/tmp/error.old", "r").readlines()
	for line in open('/tmp/error.old'):
		if "RESPONSE" in line :
	#	for line in logs:
                	#code = line.split(" ")[5]
               		 ip = line.split(" ")[3]
               	 	 if 6 < len(ip) <= 15:
                         	gps[ip] = gps.get(ip, 0) + 1

	data = tuple(gps.items())
	x_val = [x[0] for x in data]
        y_val = [x[1] for x in data]

        print x_val
        print y_val
        plt.plot(x_val,y_val, label = 'no of errors')
        plt.plot(x_val,y_val)
        plt.plot(x_val,y_val,'or', color='green', linestyle='dashed', linewidth = 3,
		marker='o', markerfacecolor='blue', markersize=12)
        plt.title('ATS Error Report (IP vs No of times)')
        plt.xlabel('Client IP-s')
	plt.ylabel('No of times')
        plt.savefig('error.png')
	t.sleep(5)
        im = Image.open("error.png")
        rgb_im = im.convert('RGB')
        rgb_im.save('error.jpg')
	plt.close('all')

def errorreportgenreq():
        #ips={}
	hps={}
        #logs = open("/tmp/error.old", "r").readlines()
        for line in open('/tmp/error.old'):
                if "RESPONSE" in line :
        #       for line in logs:
                        code = line.split(" ")[5]
			hps[code] = hps.get(code, 0) + 1
                        #ip = line.split(" ")[3]
                        #if 6 < len(ip) <= 15:
                                #ips[ip] = ips.get(ip, 0) + 1
				#hps[code] = hps.get(code, 0) + 1
        data = tuple(hps.items())
	#dat = list(ips)
	#x_val = list(ips)
	#y_val = np.array(code)
        x_val = [x[0] for x in data]
        y_val = [x[1] for x in data]

        print x_val
        print y_val
        plt.plot(x_val,y_val, label = 'no of errors')
        plt.plot(x_val,y_val)
        plt.plot(x_val,y_val,'or', color='green', linestyle='dashed', linewidth = 3,
                marker='o', markerfacecolor='blue', markersize=12)
        plt.title('ATS Error Report (Response code vs No of times)')
        plt.xlabel('Response Code')
        plt.ylabel('No of times')
        plt.savefig('error2.png')
	#with PdfPages('error2.pdf') as pdf:
	    #pdf.savefig('error2.png')
        im = Image.open("error2.png")
        rgb_im = im.convert('RGB')
        rgb_im.save('error2.jpg')
#	t.sleep(5)
	plt.close('all')
