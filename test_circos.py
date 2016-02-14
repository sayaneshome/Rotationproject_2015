import csv
import random


with open('karyotype.zeamays1.txt', 'r') as f:
    reader = csv.reader(f,delimiter='\t')
    see=open('output1.txt','w')
    for row in reader:
        lines=[]
        colors=open("colours_bar.txt","r")
        lines=colors.read().split()
        color_me=random.choice(lines)
        lines.remove(color_me)
        row.append(color_me)
        row = [x.strip(' ') for x in row]
        see.write("%s" % '\t'.join(row))
    see.close()
    
  
    



