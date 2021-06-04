from os import remove, path


class File:

    @staticmethod
    def delete_file(filename: str):
        remove(filename)

    @staticmethod
    def read_file(filename: str):
        file = open(filename, 'r')
        return file.readlines()

    @staticmethod
    def file_exists(filename: str):
        return path.exists(filename)


file1 = File.file_exists('test.txt')
file2 = File.read_file('test.txt')
print(file1)
print(file2)

for line in file2:
    print(line.split('\n'))
