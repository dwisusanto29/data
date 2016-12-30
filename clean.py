from more_itertools import unique_everseen
with open('data_2016-12.csv','r') as f, open('dataclean-2016-12.csv','w') as out_file:
    out_file.writelines(unique_everseen(f))
