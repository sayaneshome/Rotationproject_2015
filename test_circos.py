import csv
import random


with open('karyotype.zeamays1.txt', 'r') as f:
    reader = csv.reader(f,delimiter='\t')
    see=open('output.txt','w')
    colors=open("colours_bar.txt","r")
    lines=colors.read().split() 
    for row in reader:
        color_me=random.choice(lines)
        row.append(color_me)
        lines.remove(color_me)
        row = [x.strip('') for x in row]
        see.write("%s\n" %'\t'.join(row))
    see.close()
    
  
    



