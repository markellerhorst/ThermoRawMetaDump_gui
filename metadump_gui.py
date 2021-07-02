# Python script with GUI file selection for simple lcms metadata extraction
# from Thermo Fisher .raw files via ProteoWizard's ThermoRawMetaDump.exe
# author Ellerhorst, Mark 2021
# tested on python 3.9.5, exe built under 3.8.2 as 3.9 has no win 7 support

import os
import tkinter as tk
from tkinter import filedialog

# delete root tk window
root = tk.Tk().withdraw()

# user select input svg to convert
path_in = filedialog.askopenfilename(title = "Select .raw file", filetypes=[('RAW Files', '.raw')])

# handel canceled file selection
if(len(path_in) == 0):
	exit()

# path for output directory
dir_out = filedialog.askdirectory(title = "Select output directory for metadata file")

# handel canceled file selection
if(len(dir_out) == 0):
	exit()

# file name and path for out
file_out = os.path.basename(dir_out) + "_metadata_instrument.txt"
path_out = os.path.normpath(os.path.join(dir_out, file_out))

# run ThermoRawMetaDump on selected raw file
os.system(rf'ThermoRawMetaDump "{path_in}" >> "{path_out}"')
