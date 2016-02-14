import csv
import random
 
 
with open('karyotype.zeamays1.txt', 'r') as f:
    reader = csv.reader(f,delimiter='\t')
    see=open('output.txt','w')
    for row in reader:
        lines=[]
        colors=open("colours_bar.txt","r")
        lines=colors.read().split()
        color_me=random.choice(lines)
        row.append(color_me)
        see.write("%s\n" % row)
    see.close()
