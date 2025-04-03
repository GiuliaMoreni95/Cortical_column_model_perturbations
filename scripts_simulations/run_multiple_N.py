import os
import sys

# Define the values for each parameter
# param1_values = ['5k', '10k', '15k', '20k', '25k', '30k'] #name of the folder
# param2_values = [5000, 10000, 15000, 20000, 25000, 30000]  # NUMBER OF NEURONS

# param1_values = ['35k', '40k', '45k', '50k','80k'] #name of the folder
# param2_values = [35000, 40000, 45000, 50000, 80000]  # NUMBER OF NEURONS

param1_values = ['60k', '70k'] #name of the folder
param2_values = [60000, 70000]  # NUMBER OF NEURONS



def run_program(param1, param2):
    print(f"Running program with parameters: numberNeuron={param1} ")
    os.system(f"python MAIN_CODE_numberN.py {param1} {param2} ")

# Iterate over the values
for index in range(len(param1_values)):
    param1 = param1_values[index]
    param2 = param2_values[index]
    
    run_program(param1, param2)
