import os

# Create a new directory
os.mkdir('test_dir')
print('Directory created.')

# List files and directories in the current directory
print('List of files/directories:')
print(os.listdir('.'))

# Join path components for the new file in the created directory
file_path = os.path.join('test_dir', 'test_file.txt')
print(f'Constructed file path: {file_path}')

# Create a new file in the created directory
with open(file_path, 'w') as file:
    file.write('Hello, World!')

# List files and directories in the created directory
print('List of files/directories in test_dir:')
print(os.listdir('test_dir'))

# Split the file path into root and extension
root, ext = os.path.splitext(file_path)
print(f'Root of the file path: {root}')
print(f'Extension of the file path: {ext}')
