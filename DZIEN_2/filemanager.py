class FileManager:
    def __init__(self,filename,mode,encod):
        self.encod = encod
        self.mode = mode
        self.filename = filename
        self.file = None

    # def __repr__(self):
    #     return "tworzymy dostęp do opercacji na plikach..."

    def __enter__(self):
        self.file = open(self.filename,self.mode,encoding=self.encod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager('test.txt','w','utf-8') as f:
    f.write('to jest pierwsza linia tektu')
    print(type(f))
    #print(f)


print(f.closed)

p = FileManager('test.txt','r','utf-8')
print(type(p))

with FileManager('test.txt','r','utf-8') as f:
    print(f.read())

print(f.closed)

