import os

# Define the values for each parameter
#param1_values = [e23, pv23, sst23, vip23, e4, pv4, sst4, vip4, e5, pv5, sst5, vip5, e6, pv6, sst6, vip6] #name of the folder
#param2_values = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]  # layer
#param3_values = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]  # cell_type

param1_values = [0, 150, 0, 0, 0, 0, 0]  # INPUT TO LAYER 4
param2_values = [0, 0, 150, 0, 0, 150, 150]  # INPUT TO LAYER 5
param3_values = [0, 0, 0, 150, 0, 150, 150]  # INPUT TO LAYER 23
param4_values = [0, 0, 0, 0, 150, 0, 150]  # INPUT TO LAYER 6

def run_program(param1, param2, param3, param4):
    print(f"Running program with parameters: ff_input={param1}, fb_5_input={param2}, fb_23_input={param3}, fb_6_input={param4}")
    os.system(f"python MAIN_CODE1_fixed_weights_layers_input.py {param1} {param2} {param3} {param4}")

# Iterate over the values
for index in range(len(param1_values)):
    param1 = param1_values[index]
    param2 = param2_values[index]
    param3 = param3_values[index]
    param4 = param4_values[index]
    
    print(f"EXECUTION OF PROGRAM NUMBER: {index + 1}")  # Tells which simulation we are at

    run_program(param1, param2, param3, param4)
