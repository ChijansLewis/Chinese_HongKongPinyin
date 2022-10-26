import csv
def trans(ch):
    

    file=open("Pinyin.csv","r",encoding='utf-8')

    reader=csv.reader(file)

    py_ch=[]
    for line in reader:
        pych={}
        pych["py"],pych["ch"]=line[0],line[1]
        py_ch.append(pych)
    for pych in py_ch:
        if pych['ch']==ch:
            print(ch,"->",pych['py'])

if __name__=="__main__":
    ch=input("What's the Hanzi(simplified)?\n")
    trans(ch)
