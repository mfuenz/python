#!/usr/bin/python

debug = 1;

import pprint

#Math example
if debug == 0:
 
  a = 3;
  b = 4;
  c = 7;
  print "\nMarcelo Test";
  print "\n--------------\n testing new line";



  print "Printing a plus b variables\n";
  print "a = 3\n";
  print "b = 4\n";
  print "c = 7\n";

  print "So a + b = ",(a + b);


#Grabbing data from a URL, data within elements, and printing
if debug == 1:
  from mechanize import Browser
  from BeautifulSoup import BeautifulSoup
  #from links_array import *


  mech = Browser()
  url = "http://hosted.ap.org/lineups/FOOTBALLHEADS.rss?SITE=AP&SECTION=HOME"
  page = mech.open(url)
  html = page.read()

  import re
  title = re.findall(r'<title>(.*?)</title>', html, re.DOTALL)
  description = re.findall(r'<description>(.*?)</description>', html, re.DOTALL)
  links = re.findall(r'<link>(.*?)</link>', html, re.DOTALL)

  #print links
  #pprint.pprint(links)
  i = 0
  for each in title:
    
    print i,".","Title: ",(title[i])
    print "    Description: ",(description[i])
    print "    URL: ",(links[i])
    print ""
    i += 1
    
    
#Dumping an array
if debug == 0:
  from array import *
  import pprint
  #arrayIdentifierName = array(typecode, [Initializers]
  my_array = array('i',[1,2,3,4,5])
  for i in my_array:
    print(i)
  print "==============="
  print my_array[1]
  print "==============="
  print "After appending 6th element"
  my_array.append(6)
  for i in my_array:
    print (i)
    pprint.pprint(my_array)
  print "================="
  my_array.insert(0,0)
  print "my_array: ",my_array
  print "================="
  
  
  pprint.pprint(my_array)
  