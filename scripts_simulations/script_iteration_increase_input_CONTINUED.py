import os

# Define the values for each parameter
param1_values = ['e4', 'pv4', 'sst4', 'vip4', 'e5', 'pv5', 'sst5', 'vip5', 'e6', 'pv6', 'sst6', 'vip6'] #name of the folder
param2_values = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]  # layer
param3_values = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]  # cell_type
#THE FF input and the FB input 
param4_values=[0,30,60,80,110,140,170,200,230,230,260,280,310,340,370,400]  # Default FF input is 0 if not provided


def run_program(param1, param2, param3, param4):
    print(f"Running program ff increase with parameters: perturbing={param1}, layer={param2}, cell={param3}, ff_input={param4}")
    os.system(f"python MAIN_CODE_iterate_ff_increasing.py {param1} {param2} {param3} {param4}")

    print(f"Running program fb increase with parameters: perturbing={param1}, layer={param2}, cell={param3}, fb_input={param4}")
    os.system(f"python MAIN_CODE_iterate_fb_increasing.py {param1} {param2} {param3} {param4}")

    print(f"Running program ff increase fb fixed with parameters: perturbing={param1}, layer={param2}, cell={param3}, ff_input={param4}")
    os.system(f"python MAIN_CODE_iterate_ff_increasing_fb_fixed.py {param1} {param2} {param3} {param4}")

    print(f"Running program fb increase ff fixed with parameters: perturbing={param1}, layer={param2}, cell={param3}, fb_input={param4}")
    os.system(f"python MAIN_CODE_iterate_fb_increasing_ff_fixed.py {param1} {param2} {param3} {param4}")

# Iterate over the values
for index in range(len(param1_values)):
    param1 = param1_values[index]
    param2 = param2_values[index]
    param3 = param3_values[index]
    
    print(f"EXECUTION OF PROGRAM NUMBER: {index + 1}")  # Tells which simulation we are at

    for param4 in param4_values: # I want the same simulations but with different values of the ff input.
        run_program(param1, param2, param3, param4)
