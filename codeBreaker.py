import copy;


def makeOther(pwd,index):
    pwd=copy.deepcopy(pwd);
    index=copy.deepcopy(index);
    childList=[];
    childList.append((pwd,index+1));
    if(ord(pwd[index])>=65 and ord(pwd[index])<=90):   #capital letter
        #make small
        tempPwd=copy.deepcopy(pwd)
        tempPwd[index]=chr(32+ord(tempPwd[index]))

        childList.append((tempPwd,index+1))
    if(ord(pwd[index])>=97 and ord(pwd[index])<=122):   #small letter
        #make capital
        tempPwd=copy.deepcopy(pwd)
        tempPwd[index] = chr(ord(tempPwd[index])-32)

        childList.append((tempPwd,index+1))
    if(ord(pwd[index])==105 or ord(pwd[index])==73):   #i ,then add I
        #donot increment index for it.
        tempPwd=copy.deepcopy(pwd)
        tempPwd[index] = chr(76)
        childList.append((tempPwd,index+1))
        tempPwd=copy.deepcopy(pwd)
        tempPwd[index] = chr(108)
        childList.append((tempPwd,index+1))
    elif(ord(pwd[index]) == 76 or ord(pwd[index]) == 108):  #l then add L
        #donot increment index for it.
        tempPwd=copy.deepcopy(pwd)
        tempPwd[index] = chr(73)
        childList.append((tempPwd,index+1))
        tempPwd=copy.deepcopy(pwd);
        tempPwd[index] = chr(105)
        childList.append((tempPwd, index + 1))
    return childList;


def codeBreaker(pwd):
    pwdLen=len(pwd)
    if(pwdLen==0):
         return;
    index=0;
    runQ=[];
    runQ.append((pwd,index))
    visitedQ=[];

    while( not(len(runQ)==0) ):
        temp,index=runQ.pop();  #pop
        if(index==pwdLen):
            visitedQ.append(temp);
        else:
            curList=makeOther(temp,index);
            runQ=runQ+curList;

    tempo=len(visitedQ);
    while( not(len(visitedQ)==0) ):
        temp=visitedQ.pop();
        print(temp);
    print("\nLength of visitedQ:", tempo);

def main():
    codeToBreak =['K', 'z', 'l', 'b', '4', 'a', '1']
    codeBreaker(codeToBreak);


main();
#codeBreaker
#Task you are given a password.
#variations can be done in alphabet (i.e interconversion of small and capital)
#and most imp i and l (are the two variables that can be interchanged since in machine display both appear to be same)