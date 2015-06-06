import os, subprocess

listoffiles = ["/Users/john/Dropbox/CherryCredits/",
"/Users/john/Dropbox/CherryCredits/#JOHN/",
"/Users/john/Dropbox/CherryCredits/#JOHN/Database-MSSQL/",
"/Users/john/Dropbox/CherryCredits/#JOHN/Network-arista/",
"/Users/john/Dropbox/CherryCredits/#JOHN/rack/",
"/Users/john/Dropbox/Dell/",
"/Users/john/Dropbox/HLE2014/",
"/Users/john/Dropbox/HLE2014/S7971665J-PersonalBankStatement/",
"/Users/john/Dropbox/HOUSE/",
"/Users/john/Dropbox/Puppet/",
"/Users/john/Dropbox/Switches/",
"/Users/john/Dropbox/brendangregg/",
"/Users/john/Dropbox/ffayth/",
"/Users/john/Dropbox/ffayth/KISSmetrics_gift-worth-11326-retweets/",
"/Users/john/Dropbox/firewall/",
"/Users/john/Dropbox/hitbsecconf2012kul/",
"/Users/john/Dropbox/reading_materials/",
"/Users/john/Dropbox/stuff/",
"/Users/john/Dropbox/swiftserve/hardware.presetup/",
"/Users/john/Dropbox/wedding/",
"/Users/john/Dropbox/wedding/alltheic/",
"/Users/john/Dropbox/wedding/hdb/"]

def getcontents(a):
    return os.listdir(a)

def printcontents(a):
    for i in a:
        print(getcontents(i))

printcontents(listoffiles)