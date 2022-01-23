import os


def generate_query():
    files = os.listdir('./XML/');


    #files = files[1:4];

    for i in range(len(files)):
        files[i] = files[i][:-4] + ".svs";


    str = "";


    cliche = 'files.file_name = "'


    n = len(files);
    for i in range(n):
        	str += cliche + files[i] + '"'
	
        	if(i != n-1):
	        	str += ' OR ';
	
	
    f = open("gdc_query.txt", "w")
    f.write(str)
    f.close()




def download_svs(UUID):
    os.system("gdc-client download " + str(UUID))  
    return str(UUID) + "/"

def download_files(manifest_path):
    print('assuning virtual enviorment is activated for gdc client. Otherwise, might not work');
    os.system('mkdir WSI');
    os.system('cd ./WSI');
    print('Okay downloading');
    
    uuids = []
    f = open(manifest_path, "r")
    lines = f.readlines()

    n = len(lines);
    for i in range(1,n):
        	parts = lines[i].split('\t');
        	uuids.append(parts[0]);


    n = len(uuids);
    print("N:");
    print(n);
    #for i in range(n):
    #    print(uuids[i]);
    #    download_svs(uuids[i]);

    
    
    os.system('cd ..');


download_files('./manifest_1_173.txt')

#generate_query();



