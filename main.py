import datetime
import time

class Myopen:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def __enter__(self):
        self.file = open(self.file_path, 'r+')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

if __name__ == "__main__":
    with Myopen('file.txt') as file:
        print(file.read())
        file.write(file.read() + '\nopen ' + str(datetime.datetime.now()))
        time.sleep(5)
        file.write(file.read() + '\nclose ' + str(datetime.datetime.now()))
