#! /usr/bin/env python

import re
matchchar = re.compile(
	r"""\b(red|green)
	(\s+
		pepper
		(?!corn)
		(?=.*salad))""",
re.IGNORECASE | 
re.DOTALL | 
re.VERBOSE)

#matchchar = re.compile(r"""\b(red|green)(/s+pepper(?!corn)(?=.*salad))""", re.IGNORECASE | re.DOTALL | re.VERBOSE)

f = open('chunkofwords', 'rw')

for para in f.readlines():
	fixed_para = matchchar.sub(r'bell\2', para)
	print fixed_para+'\n'