import os
import sys

# Define the values for each parameter
param1_values = ['e23_1', 'e23_2', 'e23_3', 'e23_4', 'e23_5', 'e23_6','e23_7','e23_8','e23_9','e23_10'] #name of the folder


# Iterate over the values
for index in range(len(param1_values)):
    param1 = param1_values[index]
    param2 = 0
    param3 = 0
    param4 = 150
    param5 = 0
    param6 = 0
    param7 = 0

    print(f"Running program with parameters: simulation_n={param1} ")
    os.system(f"python MAIN_CODE_TIMING.py {param1} {param2} {param3} {param4} {param5} {param6} {param7} ")
