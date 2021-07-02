# Python script with GUI file selection for simple lcms metadata extraction
# from Thermo Fisher .raw files via ProteoWizard's ThermoRawMetaDump.exe
# author Ellerhorst, Mark 2021
# tested on python 3.9.5

import os
import tkinter as tk
from tkinter import filedialog

# delete root tk window
root = tk.Tk().withdraw()

# user select input svg to convert
path_in = filedialog.askopenfilename(title = "Select .raw file", filetypes=[('RAW Files', '.raw')])

# path for output directory
dir_out = filedialog.askdirectory(title = "Select output directory for metadata file")
file_out = os.path.basename(dir_out) + "_metadata_instrument.txt"
path_out = os.path.normpath(os.path.join(dir_out, file_out))

# run ThermoRawMetaDump on selected raw file
os.system(f'"ThermoRawMetaDump {path_in} >> {path_out}"')
