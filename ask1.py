
# coding: utf-8

# In[ ]:



def sumIntervals(l, sort = True):
    if sort:
        sl = sorted(tuple(sorted(i)) for i in l)
    else:
        sl = l
    if len(sl) > 1:
        if sl[0][1] >= sl[1][0]:
            sl[0] = (sl[0][0], sl[1][1])
            del sl[1]
            if len(sl) < len(l):
                return sumIntervals(sl, False)
    list=[]
    list=[x for xs in sl for x in xs]  
      
    check_list=[]
    output=0
    i=0
    first=None
    second=None
    boolean=True
    while i<len(list):
        first=None
        c=0
        while c<len(check_list):
            if check_list[c]>=list[i]:
                first=check_list[c]
            if check_list[c]>=list[i+1]:
                second=check_list[c]
            c+=1
        if first==None and second==None:
            output+=(list[i+1]-list[i])
        elif first!=None and second==None:
            output+=(list[i+1]-first)
        elif first==None and second!=None:
            output+=(second-list[i])
        elif first!=None and second!=None:
            output+=(second-first)
            
        check_list.append(list[i])
        check_list.append(list[i+1])
        
        i+=2
        
    return output
#print(sumIntervals( [[1,2], [6, 10], [11, 15] ] ))
##print(sumIntervals( [[1,4], [7, 10], [3, 5] ] ) )
#print(sumIntervals( [[1,5], [10, 20], [1, 6], [16, 19], [5, 11]] ))
list=input("Enter List Only=")
print sumIntervals(list )
