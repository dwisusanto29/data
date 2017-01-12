import sys
import pandas as pd

namefile = sys.argv[1];
outfile = "output.csv";
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')
data = pd.read_csv(namefile, index_col=0,date_parser=dateparse)
hasil = data.groupby(pd.Grouper(level=0))

hasil.to_csv(outfile)

