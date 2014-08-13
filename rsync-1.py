#! /usr/bin/env python

#translation of a bash script used previously.

import os, subprocess

useraccount = "user1"
source_path = "/source_path/"
destination_path = "/destination_path/"
destination_ip = ["127.0.0.1","127.0.0.1","127.0.0.1","127.0.0.1"]
exclude_element = "dir1"

#check if source path is available
def _check_paths_(useraccount, source_path, destination_path, destination_ip, exclude_element):
	sp = os.path.exists(source_path)
	if sp == True:
		_syncthemall_(useraccount, source_path, destination_path, destination_ip, exclude_element)
	else:
		return "\"%s\" cannot be found." % source_path

#rsync process begins here, "except OSError doesn't work, gotta work on it"
def _syncthemall_(useraccount, source_path, destination_path, destination_ip, exclude_element):
	for d_ip in destination_ip:
		print "############ transferring to %s ############" % d_ip
		rsync_args = ["/usr/bin/rsync", "--exclude="+exclude_element, "-ave", "ssh", source_path, useraccount+"@"+d_ip+":"+destination_path]
		print "executing " + " ".join(rsync_args)
		try:
			subprocess.call(rsync_args)
		except OSError as (errno, strerror):
			print "%d, %s" % (errno, strerror)

_check_paths_(useraccount, source_path, destination_path, destination_ip, exclude_element)