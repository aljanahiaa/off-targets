import csv
import sys

d={}
empty=['','','']

headder=[ 'name', 'chrom', 'strt', 'end', 'side', 'seq',  'distance']
   
for i, item in enumerate(sys.argv):
    #print sys.argv
    if i>0:
        reader=csv.reader(open(item), delimiter='\t')
        monkey=sys.argv[i].split('.')[0]
        headder.append(monkey+"readCount")
        headder.append(monkey+"readRank")
        headder.append(monkey+"scoreRank")       
        sys.argv[i]={}
        for line in reader:
            if line[0].startswith("Chr"):
                continue
                
            else:
                name=line[3]
                chrom=line[0]
                if line[23] != "":
                    strt=int(line[23])
                else:
                    strt=int(line[1])
                if line[24] != "":
                    end=int(line[2])
                else:
                    end=int(line[2])
                if line[22] != "":
                    side=line[22]
                else:
                    side=line[6]
                if line[16] != "":
                    seq=''.join(line[16].split('-'))
                else:
                    seq=line[11]
                readcount=line[35]
                distance=line[36]
                rank=line[38]
                readrank=line[39]

                #print monkey, name, chrom, strt, end, side, seq, readcount, distance, rank, readrank


                if name in d:
                   sys.argv[i][name]=[readcount, readrank, rank]
                   
                else:
                    d[name]=[name, chrom, strt, end, side, seq, distance]
                    sys.argv[i][name]=[readcount, readrank, rank]

print '\t'.join(headder)
for item in d:
        foo=d[item]
        for i in range(1,len(sys.argv)):         
            try:
                foo = foo + sys.argv[i][item]
 #               foo.append(str(sys.argv[i][item]))
            except KeyError:
                foo = foo + empty
 #              foo.append(empty)
        print '\t'.join(map(str, foo))
                        

#print d["11:16366413-16366434"]

#for i, item in enumerate(sys.argv):
#    if i>0:
#        print sys.argv[i]["11:16366413-16366434"]

#            print sys.argv[1]['6:171124961-171124982']
#            try:
#                print sys.argv[i][item]
#            except IndexError:
#                print "index"
#                sys.argv[i][item]=['','']
