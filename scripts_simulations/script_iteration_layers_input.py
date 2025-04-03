import os
import sys

# Define the values for each parameter
param1_values = ['e23', 'pv23', 'sst23', 'vip23', 'e4', 'pv4', 'sst4', 'vip4', 'e5', 'pv5', 'sst5', 'vip5', 'e6', 'pv6', 'sst6', 'vip6'] #name of the folder
param2_values = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]  # layer
param3_values = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]  # cell_type
#THE FF input and the FB input 
#param4=${1:-0}  # Default FF input is 0 if not provided
#param5=${2:-0}  # Default FB5 input is 0 if not provided
#param6=${3:-0}  # Default FF23 input is 0 if not provided
#param7=${4:-0}  # Default FB6 input is 0 if not provided
# The FF input and the FB input
param4 = sys.argv[1] if len(sys.argv) > 1 else '0'  # Default FF input is 0 if not provided
param5 = sys.argv[2] if len(sys.argv) > 2 else '0'  # Default FB5 input is 0 if not provided
param6 = sys.argv[3] if len(sys.argv) > 3 else '0'  # Default FF23 input is 0 if not provided
param7 = sys.argv[4] if len(sys.argv) > 4 else '0'  # Default FB6 input is 0 if not provided

#param4,param5,param6,param7 = sys.argv[1:]

def run_program(param1, param2, param3, param4, param5, param6, param7):
    print(f"Running program with parameters: perturbing={param1}, layer={param2}, cell={param3}, ff_input={param4}, fb5_input={param5}, fb23_input={param6},fb6_input={param7}")
    os.system(f"python MAIN_CODE_iterate_layers_input.py {param1} {param2} {param3} {param4} {param5} {param6} {param7} ")

# Iterate over the values
for index in range(len(param1_values)):
    param1 = param1_values[index]
    param2 = param2_values[index]
    param3 = param3_values[index]
    
    print(f"EXECUTION OF PROGRAM NUMBER: {index + 1}")  # Tells which simulation we are at

    run_program(param1, param2, param3, param4, param5, param6, param7)
