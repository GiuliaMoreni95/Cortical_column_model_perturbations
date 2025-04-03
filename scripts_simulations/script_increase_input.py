import subprocess

param1_values = [0, 30, 60, 80, 110, 140, 170, 200, 230, 230, 260, 280, 310, 340, 370, 400]  # INPUT TO LAYER 4

def run_program(param1):
    print(f"Running program with parameters: ff_input={param1}")
    print(f"Running program with parameters: fb_input={param1}")
    
    try:
        subprocess.run(f"python MAIN_CODE1_fixed_weights_ff_increase.py {param1}", shell=True, check=True)
        subprocess.run(f"python MAIN_CODE1_fixed_weights_fb_increase.py {param1}", shell=True, check=True)
        subprocess.run(f"python MAIN_CODE1_fixed_weights_fb_increase_ff_fixed.py {param1}", shell=True, check=True)
        subprocess.run(f"python MAIN_CODE1_fixed_weights_ff_increase_fb_fixed.py {param1}", shell=True, check=True)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the program: {e}")

# Iterate over the values
for index in range(len(param1_values)):
    param1 = param1_values[index]
    
    print(f"EXECUTION OF PROGRAM NUMBER: {index + 1}")  # Tells which simulation we are at

    run_program(param1)