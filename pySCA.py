import functions_SCA
from functions_SCA import NumpyArrayEncoder
from argparse import ArgumentParser
import argparse
import matplotlib.pyplot as plt
import pickle
import json
from json import JSONEncoder


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", type = str, dest = "input_file", help = "SCA calculations as .db file")
parser.add_argument("-t", "--title", type = str, dest = "plot_title", help =  "Title for the plot (group 1/2/3)")
parser.add_argument("-d", "--di", type = str, dest = "output_file", help = "output name for first order statistics saved as .json file")
parser.add_argument("-p", "--plot", type = str, dest = "output_plot", help = "output name for first order statistics plot saved as .png")
args = parser.parse_args()
input_file, plot_title, output_file, output_plot = args.input_file, args.plot_title, args.output_file, args.output_plot

# load pickle file 
db = pickle.load(open(input_file,'rb'))
Dseq = db['sequence']  
Dsca = db['sca'] 

#  di values saved as dictionary
out_file = {"Di": Dsca['Di']}

print("After processing, the alignment size is %i sequences and %i positions" % \
      (Dseq['Nseq'], Dseq['Npos']))
print("With sequence weights, there are %i effective sequences" % (Dseq['effseqs']))

# plot di scores (conservation plot)
plot_di = plot_first_order_statistics(Dsca, plot_title)
plot_di.savefig(output_plot, dpi = 100)

# save the di values as json file
json_object = json.dumps(out_file, cls = NumpyArrayEncoder)
with open(output_file, "w") as outfile:
    outfile.write(json_object)

