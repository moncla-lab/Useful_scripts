import os
import sys
import random

# Processes all .trees files in an input folder and creates subsampled tree sets after removing burn-in.
# Randomly subsamples 1000 trees (can modify this number) from a posterior sample of trees.
# Added burnin percentage to remove a portion of the trees before subsampling.
#usage: python script.py input.folder output.folder 10 
#10 == burnin percentage


def process_file(input_file, output_file, burnin_percentage):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Find the first occurrence of "tree STATE"
    start_index = next((i for i, line in enumerate(lines) if "tree STATE" in line), None)

    if start_index is None:
        print(f"Warning: No 'tree STATE' found in {input_file}, skipping.")
        return

    # Find the first occurrence of "End;" after "tree STATE"
    end_index = next((i for i, line in enumerate(lines[start_index:], start=start_index) if "End;" in line), None)

    if end_index is None:
        print(f"Warning: No 'End;' found after 'tree STATE' in {input_file}, skipping.")
        return

    # Save everything before "tree STATE"
    before_tree_state = lines[:start_index]

    # Get lines between "tree STATE" and "End;"
    lines_between = lines[start_index:end_index]

    # Calculate number of trees to discard as burn-in
    burnin_count = int(len(lines_between) * (burnin_percentage / 100.0))

    # Remove burn-in trees
    lines_after_burnin = lines_between[burnin_count:]

    # Subsample 1000 lines after removing burn-in
    subsampled_lines = random.sample(lines_after_burnin, min(1000, len(lines_after_burnin)))

    # Write to the output file
    with open(output_file, 'w') as file:
        file.writelines(before_tree_state)
        file.writelines(subsampled_lines)
        file.write("End;")
    
    print(f"Processed and saved: {output_file}")


def process_folder(input_folder, output_folder, burnin_percentage):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".trees"):  # Process only .trees files
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{filename}")
            process_file(input_path, output_path, burnin_percentage)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_folder> <output_folder> [burnin_percentage]")
        sys.exit(1)
    
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    # Burnin percentage (default to 0 if not provided)
    burnin_percentage = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0

    process_folder(input_folder, output_folder, burnin_percentage)
