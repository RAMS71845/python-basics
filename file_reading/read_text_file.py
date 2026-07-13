from pathlib import Path
SAMPLE=Path(__file__).resolve().parent /"hello.txt"
print(SAMPLE)

def read_whole_file()->str:
    with open(SAMPLE,"r",encoding="utf-8") as f:
        return f.read()
print(read_whole_file())
def read_as_line()->list:
    with open (SAMPLE,"r",encoding="utf-8")as f:
        return f.readlines()
print(read_as_line())
def read_line_by_line()->None:
    with open(SAMPLE,"r",encoding="utf-8") as f:
        for number,line in enumerate (f,start=1):
            print(f"line{number}: {line}")
print(read_line_by_line())

def write_sample()->None:
    with open(SAMPLE,"w",encoding="utf-8")as f:
        f.write("Line 1: Ram is a good boy!!\n")
        f.write("Line 2: Sikha is a bad girl!!")
    
write_sample()
print(read_whole_file())