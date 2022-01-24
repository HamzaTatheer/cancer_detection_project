import os
import pandas as pd 
import numpy as np

def not_common(lst1, lst2):
    lst3 = [value for value in lst1 if value not in lst2]
    return lst3



# create the series 
lst1 = os.listdir('./XML');
lst2 = os.listdir('./WSI');

lst1 = [x[:-4] for x in lst1]
lst2 = [x[:-4] for x in lst2]


res1 = not_common(lst1,lst2);
res2 = not_common(lst2,lst1);

print('Deleting not needed files from xml');
print(len(res1))
print(res1)

print('Deleting not needed files from svs');
print(len(res2))
print(res2)

for i in range(len(res1)):
    os.remove('./XML/'+res1[i] + '.xml');i


for i in range(len(res2)):
    os.remove('./WSI/'+res2[i] + '.svs');

print('Done');





