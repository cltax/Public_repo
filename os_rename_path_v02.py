# Exercise to open edit and save a text file


import os.path

parent_dir = "D:\\Claudio\Documents\\Programming\\test_files\\"
file_to_read = "text_file.txt"
file_to_write = "text_file_cleaned.txt"
max_line_length = 20  # Maximum allowed line length before splitting

path_to_read = os.path.join(parent_dir, file_to_read)
path_to_write = os.path.join(parent_dir, file_to_write)

if os.path.exists(path_to_read):
    try:
        # Read lines using list comprehension for compactness and filtering
        with open(path_to_read, newline='') as tmp_file_to_read:
            clean_text = [line.strip() for line in tmp_file_to_read.readlines() if line.strip()]

        # Split lines longer than the threshold
        for i in range(len(clean_text)):
            line_to_split = clean_text[i]
            if len(line_to_split) > max_line_length:
                # Split at sentences (using '.' as a delimiter) and replace the original line
                split_lines = line_to_split.split('.')
                clean_text[i:i + 1] = split_lines  # Update original list with split lines

        # Write the modified content to a new file
        with open(path_to_write, "w", newline='') as clean_file:
            for line in clean_text:
                clean_file.write(f"{line}\n")
        print(f"File successfully processed and written to '{path_to_write}'.")
    except (IOError, OSError) as e:
        print(f"Error: An error occurred while processing the file: {e}")
else:
    print(f"Error: File '{path_to_read}' does not exist.")