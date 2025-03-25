import sys
import random
# Randomly subsamples 1000 trees from a posterior sample of trees in a BEAST nexus tree file this can be changed, change integer at line 21
# to do -> add burnin perecentange and remove the input % as an arg

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Find the first occurrence of "tree STATE"
    start_index = next(i for i, line in enumerate(lines) if "tree STATE" in line)

    # Find the first occurrence of "End;" after "tree STATE"
    end_index = next(i for i, line in enumerate(lines[start_index:], start=start_index) if "End;" in line)

    # Save everything before "tree STATE"
    before_tree_state = lines[:start_index]

    # Subsample 1000 lines from between "tree STATE" and "End;"
    lines_between = lines[start_index:end_index]
    subsampled_lines = random.sample(lines_between, min(1000, len(lines_between)))

    # Write to the output file
    with open(output_file, 'w') as file:
        file.writelines(before_tree_state)
        file.writelines(subsampled_lines)
        file.write("End;")

if __name__ == "__main__":
    # Input and output file paths from arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Process the file
    process_file(input_file, output_file)
