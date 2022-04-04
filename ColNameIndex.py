#Python program to list the index number of an excel column name. Example: A=1,Z=26,AA=27,BA=53...
#Dictionary with alphabet key-value pairs
alphatable = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
charlist=[] #Placeholder to convert the input string to a list
#Function to derive the index value of a column name
def indexvalue(colname,listlength):
    k=1
    power=0
    sum=0
    for i in charlist:
        power=length-k
        sum=sum+alphatable[i]*26**power
        k=k+1
    return(sum)

#User input and validation
colname=input("Please enter the column name: ")
if colname.isalpha():
    length=len(colname)
    charlist=list(colname.upper())
    colindex=indexvalue(charlist,length)
    print("Index for",colname.upper(),"is:",colindex)
else:
    print("Invalid input! Please enter only letters (A - Z)")
