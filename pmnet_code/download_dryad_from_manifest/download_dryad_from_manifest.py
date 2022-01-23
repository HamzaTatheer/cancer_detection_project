"""Usage: convert_dryad_manifest_wget_file.py -f FILE -d DIR

-f    manifest_file_location
-d    directory to save files


"""

import os
from docopt import docopt

def download_dryad(manifest_file,directory):

    print('Downloading files of',os.path.abspath(manifest_file),'to',os.path.abspath(directory));
   
    f = open(manifest_file,'r')
    f.readline();#skip first line i.e header

    for line in f:

        end = line.find('\t')
        uuid = line[0:end]
        download_link = 'https://api.gdc.cancer.gov/data/'+uuid;
        print('downloading ',uuid)
        #print(download_link)
        #use when in gpu
        os.system('wget -c '+download_link+' -P ' + directory);


    f.close();

    
if __name__ == "__main__":
    args = docopt(__doc__);
    download_dryad(args['FILE'],args['DIR']);
