The dryad dataset from the main source did not contain svs files but the compressed png files
which are of no use. Hence, Their names are extracted (from available xml files) and their svs downloaded from tcga database


1. Download gdc_client using the folder "install_gdc[important]"
2. Run generate_query() in order to get query to enter at https://portal.gdc.cancer.gov/query
3. Download the manifest file for the query from that website
4. Use download_files(manifest) to get those files. This function will create a folder in its path and store files
