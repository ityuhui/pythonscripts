#! env python

import urllib2
import time
import sys

def print_max_or_min(pri,ChengBen,hold):
	print pri,(pri - ChengBen )* hold, "%.2f%%" % ((pri / ChengBen - 1)*100) 
	sys.stdout.flush()
	
yhold = 6000
yChengBen = 1.671
yURL='http://hq.sinajs.cn/list=sh510050'

def init_print(url,chengBen,hold):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	the_page = response.read()
	usarr = the_page.split(',')

	print_max_or_min(float(usarr[5]),chengBen,hold)
	print_max_or_min(float(usarr[4]),chengBen,hold)


def get_now(url,chengBen,hold):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	the_page = response.read()
	usarr = the_page.split(',')
	unowa = float(usarr[3])
	shouyi = ( unowa - chengBen ) * yhold
	rat = ( unowa - chengBen ) / chengBen * 100.0 
	print unowa, shouyi, "%.2f%%" % rat
	sys.stdout.flush()


init_print(yURL,yChengBen,yhold)

while True:
	get_now(yURL,yChengBen,yhold)
	time.sleep(60)
	

