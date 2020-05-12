# --------------
#Code starts here
def palindrome(num):
    while(True):
        c=0
        r=0
        nn=0
        n=num+1
        temp=n
        while(n!=0):
            r=n%10
            n=int(n/10)
            nn=nn*10+r

        if(nn==temp):
            c+=1
            if(c==1):
                return nn
                break
        else:
            num+=1
            continue


res=palindrome(8)
print(res)



# --------------
#Code starts here

def a_scramble(str_1,str_2):
    lst1=[letter for letter in str_1.upper()]
    lst2=[letter for letter in str_2.upper()]
  
    c=0

    for l2 in lst2:
        if l2 in lst1:
            lst1.remove(l2)
            c+=1

        else:
            continue

    if(c==len(lst2)):
        return True
    else :
        return False

a_scramble("baby shower","shows")




# --------------
#Code starts here
def check_fib(num):
    a=1
    b=1
    while(True):
        c=a+b
        a=b
        b=c
        if(c==num):
            return True
            break
        
        elif(c<num):
            continue
        
        else:
            return False
            break
    

check_fib(145)



# --------------
#Code starts here
def compress(word):
    res = ""
    word=word.lower()
    count = 1

    #Add in first character
    res += word[0]

    #Iterate through loop, skipping last one
    for i in range(len(word)-1):
        if(word[i] == word[i+1]):
            count+=1
        else:
            if(count > 1):
                #Ignore if no repeats
                res += str(count)
            elif count==1:
                res+=str(count)
            res += word[i+1]
            count = 1
    #print last one
    if(count > 1):
        res += str(count)
    elif count==1:
        res+=str(count)
    return res

compress("xxcccdex")


# --------------
#Code starts here
def k_distinct(string,k):
    lst1=[letter for letter in string.upper()]
    lst2=[]
    for i in range(0,len(lst1)):
        for j in range(i+1,len(lst1)):
            if lst1[i]==lst1[j]:
                lst2.append(lst1[i])
                break
    print(lst2)
    
    if(len(lst1)-len(lst2)==k):
        return True
    else:
        return False


k_distinct('Messoptamia',8)


