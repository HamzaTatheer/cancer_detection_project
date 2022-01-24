import os
import pandas as pd
import py_wsi
import numpy as np
import shutil


def retrieve_tile_dimensions(file_name, patch_size=0, overlap=0, tile_size=0):
    # Locates the file and retrieves tile information.
    return level_count, level_tiles, level_dims
def create_patches(svs_path, patches_path, xml_dir):


  dirss = os.listdir(svs_path)
  dirss = np.array(dirss)


  if len(dirss) > 1:
    dirss = dirss[dirss!='.ipynb_checkpoints']
  if len(dirss) > 1:
    dirss = dirss[dirss!='logs']

  if len(dirss) > 1:
    dirss = dirss[dirss!='.DS_Store']
 
  pure_dir = dirss[0]
  file_dir = svs_path
  db_location = patches_path
  xml_dir = xml_dir


  patch_size = 256
  level = 16
  db_name = "patch_db"
  overlap = 0
  # All possible labels mapped to integer ids in order of increasing severity.
  label_map = {'Normal': 0,
              '' : -1
              }


  turtle = py_wsi.Turtle(file_dir, db_location, db_name, xml_dir=xml_dir, label_map=label_map, storage_type='disk')
  print("Total WSI images:    " + str(turtle.num_files))
  print("LMDB name:           " + str(turtle.db_name))
  print("File names:          " + str(turtle.files))
  print("XML files found:     " + str(turtle.get_xml_files()))

  level_count, level_tiles, level_dims = turtle.retrieve_tile_dimensions(pure_dir, patch_size=256);
  #print(dirss);
  #print(pure_dir);

  print("Level count:         " + str(level_count))
  print("Level tiles:         " + str(level_tiles))
  print("Level dimensions:    " + str(level_dims))
 
  try:
    turtle.sample_and_store_patches(patch_size, level, overlap, load_xml=True, limit_bounds=True)
    return True
  except Exception:
    print("Error: ")
    print(Exception);
    return False



def generate_patches_csv(dir_path):
    files = os.listdir(dir_path)
    files = pd.DataFrame(data=files, columns=['filename'])

    x = files["filename"].str.split("_", n = 4, expand = True)
    y = x[x.columns[-1]].str.split(".", n = 1, expand = True)
    y=y[y.columns[0]]


    files["SVS_NO"] = x[x.columns[-4]]
    files["ROW"] = x[x.columns[-3]]
    files["COL"] = x[x.columns[-2]]
    files["ROW"] = files["ROW"].astype('int')
    files["COL"] = files["COL"].astype('int')


    files["Class_Name"] = y;
    files["Class_Name"] = files["Class_Name"].astype('int');
    files['filename'] = 'patches_temp/' + files['filename'];
    files['Class_Name'] = files['Class_Name'].apply(lambda x : 1 if x < 0 else 0)
    files['Class_Name'] = files['Class_Name'].astype('int')
    
    return files;

try:
	os.mkdir('../patches_temp');
except:
	print("File already exists");


#svs_dir = '../../pmnet_dataset/bach/WSI/';
#xml_dir = '../../pmnet_dataset/bach/XML/';

svs_dir = '../../pmnet_dataset/dryad/WSI/';
xml_dir = '../../pmnet_dataset/dryad/XML/';


print('START');

create_patches(svs_dir, "../patches_temp/",xml_dir);

print('DONE');
