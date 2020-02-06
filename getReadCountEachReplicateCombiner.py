import csv
import sys

d={}

lines=open(sys.argv[1]).readlines()
#print lines[0].strip()
    
for i, item in enumerate(sys.argv):
    #print sys.argv
    if i>0:
        reader=csv.reader(open(item), delimiter='\t')
        for line in reader:
            if line[0].startswith("Chr"):
                continue
            else:
            
               #print item, line[3], line[5]
               if line[3] in d:
                   d[line[3]][i-1]=line[5]
               else:
                    d[line[3]]=['0','0']
                    d[line[3]][i-1]=line[5]
                    #print d[line[3]]

for item in d:
    #print '\t'.join(d[item][1]), '\t', d[item][0]
    print item,'\t', '\t'.join(d[item])
