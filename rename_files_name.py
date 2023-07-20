import os

# Specify the directory path
directory = 'crop_original'

# Get a list of all files in the directory
files = os.listdir(directory)

# Sort the files in ascending order
files.sort()

# Set the starting value for the counter
starting_number = 9

# Iterate over the files and rename them
for i, file in enumerate(files, starting_number):
    # Split the file name and extension
    name, extension = os.path.splitext(file)
    
    # Create the new file name using the counter
    new_name = f'CAMIS_{i:05d}{extension}'
    
    # Construct the full paths of the old and new names
    old_path = os.path.join(directory, file)
    new_path = os.path.join(directory, new_name)
    
    # Rename the file
    os.rename(old_path, new_path)





















# import os
# import glob

# def rename_files(directory):
#     # Get a list of all files in the directory
#     files = glob.glob(os.path.join(directory, '*.jpg'))
    
#     # Sort the files in ascending order based on their names
#     files.sort()
    
#     # Determine the padding required for the new names
#     num_files = len(files)
#     padding = len(str(num_files))
    
#     # Prefix for the new names
#     prefix = "FANCY_000"
    
#     # Rename the files in ascending order
#     for idx, file_path in enumerate(files, start=1):
#         # Get the file extension
#         _, ext = os.path.splitext(file_path)
        
#         # Create the new name with the appropriate padding
#         new_name = f"{prefix}{str(idx).zfill(padding)}{ext}"
        
#         # Rename the file
#         new_path = os.path.join(directory, new_name)
#         os.rename(file_path, new_path)
#         print(f"Renamed: {file_path} --> {new_path}")

# if __name__ == "__main__":
#     # Replace 'your_directory_path' with the actual path of the directory containing the files
#     directory_path = 'mask'
#     rename_files(directory_path)


# import os

# # Specify the directory path
# directory = 'original'

# # Get a list of all files in the directory
# files = os.listdir(directory)

# # Sort the files in ascending order
# files.sort()

# # Initialize a counter for the new file names
# counter = 1

# # Iterate over the files and rename them
# for file in files:
#     # Split the file name and extension
#     name, extension = os.path.splitext(file)
    
#     # Create the new file name using the counter
#     new_name = f'FANCY_{counter:05d}{extension}'
    
#     # Construct the full paths of the old and new names
#     old_path = os.path.join(directory, file)
#     new_path = os.path.join(directory, new_name)
    
#     # Rename the file
#     os.rename(old_path, new_path)
    
#     # Increment the counter
#     counter += 1

