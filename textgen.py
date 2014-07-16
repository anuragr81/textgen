import sys

def gen(file):
   for line in open(file).readlines():
     print line
  
file=sys.argv[1]
gen(file)
