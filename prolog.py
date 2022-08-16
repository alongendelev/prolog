import sys
import os
#basic concept:
#the progrems creates a list of all warnings to fillter by
#it checks whether the input is by file or dir, and goes throgh the files
#for each file it goes throgh the lines and
#for each line it checks if needs to filtterd and if not prints or writes it
#I designed it like that because i found it to be best in terms of simplisity and memory usege
def main ():
    args = sys.argv
    if(len(args)>1):
        outPutArg = args[1]
        inPutArg = args[2]
        if (getArgument(outPutArg) == 'write_to'): #if no matching logs - create empty file
            if not (getLocation(outPutArg).endswith(".prolog")):
                sys.exit("not valid output file")
            newFile = open(getLocation(outPutArg), "a")
            newFile.close()
        filltersList = makeFillteresList (args)
        if (getArgument(inPutArg) == 'from_dir'):
            for oneFile in os.listdir(getLocation(inPutArg)):
                if not (oneFile[0] == "."):  # does't go over hidden folders
                    outPutFile(getLocation(inPutArg)+"/"+oneFile, filltersList, outPutArg)
        elif (getArgument(inPutArg) == 'from_file'):
            outPutFile(getLocation(inPutArg),filltersList,outPutArg)
        else:
            sys.exit('you have an eror in input argument')
    else:
        sys.exit('you have an eror in arguments number')
#gets name of the file, a list of all warning fillters, the output argument
#outputs the file as needed
def outPutFile (fileName,filltersList,outPutArg):
    if not(fileName.endswith(".txt") or fileName.endswith(".log")):
        sys.exit("not vaild input file")
    readbleFile = open(fileName, "r")
    for line in readbleFile.readlines():
        outPutLine(line, filltersList, outPutArg)
    readbleFile.close()
#gets a line, a list of warning fillters, the output argumant
#checks if line needs to be filltered and if not outputs it by the output argument
def outPutLine (line,filltersList,outPutArg):
    if(notFilltered(line,filltersList)):
        if (getArgument(outPutArg) == 'write_to'):
            newFile = open(getLocation(outPutArg),"a")
            newFile.write(line)
            newFile.close()
        elif (outPutArg == 'print'):
            print (line)
        else:
            sys.exit('you have an eror in output argument')
#gets the entire argument and returns only the type of it (write_to,from_filr etc)
def getArgument(string):
    x = string.find("(")
    return string[0:x]
#gets the entire argument and returns only the parameter inside the ( )
def getLocation(string):
    start = string.find("(")
    end = string.find(")")
    return string[start + 1:end]
#gets the arguments list and return a list with all the warnings that need to be filltered
def makeFillteresList (args):
    argCount = 3
    allFilltersList = []
    while(argCount<len(args)):
        fillterArg = args[argCount]
        if(getArgument(fillterArg)=='byLevel'):
            allFilltersList.extend(getLocation(fillterArg).split(","))
        else:
            sys.exit('you have an eror in fillters arguments')
        argCount=argCount+1
    return allFilltersList
#gets a line and the fillters list, return true if does not needs to fillterd and false if does
def notFilltered (line,filltersList):
    if(len(filltersList)>0):
        if(len(line)<5):#delete empty lines
            return False
        elif(isIn(getErorType(line),filltersList)):
            return True
    else:
        return True
#gets an eror type and the fillters list, returns true if the eror type is un the list
def isIn(erorType,FilltersList):
    for fillter in FilltersList:
        if(fillter==erorType):
            return True
    return False
#gets a line returns the eror type of it
def getErorType (line):
        letter_count = 30
        erorType = line[letter_count - 1]
        while (line[letter_count] != ":"):
            erorType += line[letter_count]
            letter_count = letter_count + 1
        return erorType
if __name__ == '__main__':
    main()

