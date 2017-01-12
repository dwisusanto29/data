from more_itertools import unique_everseen
with open('data_20161227.csv','r') as f, open('dataclean-20161227.csv','w') as out_file:
    out_file.writelines(unique_everseen(f))
