class FileObject:
    def __init__(self,file_name="sample.txt"):
        self.file=open(file_name,"r")

    def __del__(self):
        self.file.close()
        del self.file
        
