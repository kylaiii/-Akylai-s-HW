from file.file_executor.create import create_file
from file.file_executor.delete import delete_file
from file.file_executor.write import write_to_file

print(create_file("Something", 'txt'))
write_to_file("something.txt", "always strive and prosper")
print(delete_file("something.txt"))