#!/usr/bin/python
#Checks for the Namepsace Bucket TSO enabled or not using REST API
#TODO
#1.Check THE TSO enabled or not using the Dt query
#2.Check for the TSO triggered on the system using RESt API
#3.Check for TSO state of the System using Dt query
#4.Add error handling
#5 Take the input from user.
import sys
import os
import commands
import xml
import xml.etree.ElementTree as ET

tok_url = 'curl -iks https://`hostname -i`:4443/login -u emcmonitor:ChangeMe | grep X-SDS-AUTH-TOKEN'
status,tok = commands.getstatusoutput(tok_url)
ns_cmd = 'curl -ks -H "%s"  https://`hostname -i`:4443/object/namespaces | xmllint --format -' % (tok)
ns_cmd, ns_raw = commands.getstatusoutput(ns_cmd)
url='https://`hostname -i`:4443/object/namespaces/namespace'
bkt_url='https://`hostname -i`:4443/object/bucket?namespace='
root = ET.fromstring(ns_raw)
for id1 in root.iter('id'):
 namespace_id = id1.text
 cmd = 'curl -ks  -H "%s" %s/%s' % (tok, url,  namespace_id)
 ns_detail = os.popen(cmd)
 ns_read = ns_detail.read()
 ns = ET.fromstring(ns_read)
 for child in ns:
      if (child.tag == "is_stale_allowed") : print 'TSO Enabled for NameSpace--->' ,child.text
      if (child.tag == "id"):
                 print "\n----Checking for  Namespace id---->", child.text
                 ns1=child.text
                 cmd1 ='curl -ks -H "%s" %s%s' % (tok, bkt_url, ns1)
                 bkt = os.popen(cmd1)
                 bkt1 = bkt.read()
                 bkt_detail= ET.fromstring(bkt1)
                 for bkt2 in bkt_detail:
                        for bkt3 in bkt2:
                                if ( bkt3.text == ' ' ) : print 'No Bucket'
                                if (bkt3.tag == "name"):
                                        print "Bukcet Name---->",bkt3.text
                                if (bkt3.tag == "is_stale_allowed"): print "Bucket TSO enabled--->" ,bkt3.text
sys.exit(0)
