#put me in folder containing dryad with wsis with filename as ids

import pandas as pd
import os

df = pd.read_csv('../manifest.csv')

for file in os.listdir():
    #print(file)

    
    row = df[df['id']+'.svs' == file].values;

    if(len(row)!= 0):
        row = row[0]

        uuid = row[0];
        filename =row[1]
        print(uuid)
        print(filename)
        os.rename(file,filename)
        
