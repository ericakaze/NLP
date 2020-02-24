
    import numpy as np
    import copy
    import pandas as pd
    file = "Holiday Schedule Ranking 2019.csv"
    sche = pd.read_csv(file, header=0, index_col=0)
    vald = sche.values
    done =[]
    for i in range (10):
        a, b = cozy(vald)
        done.append(a)
        d,indx = select1(a, b)
        arr1 = np.array(d)
        d1 = (arr1.transpose())
        #print(d1)
        if indx != []:
            donee=[]
            dw=tieclearance(indx,done,d1)
            dx= copy.deepcopy(dw)
            aa, ba = cozy(dx)
            donee.append(a)
            dc, indx = select1(aa, ba)
            #print(dx)
            d1= clean(dx, dc, donee)
            #print(d1)
        else:
            d1=(arr1.transpose())
            if len(done) >= 2:
                d1=clean(d1, d, done)
            #d1,col = cleanup(d1, d, done)

            # if indx != []:
            #     d1=tieclearance(indx,done,d1)
        
            else:
                DFG=0
        
        vald=d1
    print(d1)


def cozy(vald):
    matrix = []
    for i in range(1, 14):
        k = vald[:, (i-1):i]
        y = k.flatten()
        y = list(y)
        matrix.append(y)
    treat = []
    for i in matrix:
        a = sum(i)
        treat.append(a)
    z = treat.index(max(treat))
    return z, matrix


def test(d, c):
    rr=[]
    rr = c[d]
    rrr = []+rr
    for i in rr:
        if i ==0:
            a = rr.index(i)
            del rr[a]
        rr=[]+rr
    
    count = 0
    count2 = 0
    count3 = 0
    # rr.remove[0]
    # try:
    #     rr=ror.remove(0)
    # except ValueError:
    #     rr = c[d]
    #print(rr)
    for i in rr:
        if i == min(rr):
            count += 1
    
        else:
            count += 0
            
    if count < 3:
        rr.remove(min(rr))
        for i in rr:
            if i == min(rr):
                count2 += 1
     
            else:
                count2 += 0
      
    if count + count2 < 3:
        rr.remove(min(rr))
        for i in rr:
            if i == min(rr):
                count3 += 1
   
            else:
                count3 += 0
       
    return rrr, count, count2, count3


def select1(a, b):
    y, x, c, z = test(a, b)
    #print(x,c,z)
    yy = set(y)
    yy.discard(0)
    # print(yy)
    minz = []
    dil = []
    for i in range(3):
        yyy = min(yy)
        minz.append(yyy)
        yy.remove(yyy)
        #print(minz)
    if x==1 and c==1 and z==1:
        for i in y:
            if i == minz[0] or i == minz[1] or i == minz[2]:
                aaaaaa = 2
            else:
                c = y.index(i)
                y[c] = 0
        b[a] = y
        #print('j')
    
    if x==3 and c==0 and z==0:
        for i in y:
            if i ==minz[0]:
               aaaaa=2
            else:
                c=y.index(i)
                y[c]=0
        b[a] =y
        #print('p')

    if (x+c)==3:
        for i in y:
            if i ==minz[0] or i==minz[1]:
                aaa=2
            else:
                c=y.index(i)
                y[c]=0
        b[a] = y   
        #print ('q')    
    if (x+c+z)>3 and z>1:
       
        t=-1
        for i in y:
            t+=1
 
   
            if i==minz[2]:
                dil.append(t)
                 
            if i == minz[0] or i == minz[1] or i == minz[2]:
                aaaaaa = 2
            else:
                c = y.index(i)
                y[c] = 0
        b[a] =y
          
    return b,dil

def cleanup(d1,d,done):
    t = done[0]
    for h in range(1,len(done)):
        t2 = done[h]
        for ii in d[t]:
            if ii != 0:
                a = d[t].index(ii)
                if d[t2][a] != 0:
                    col = [0, 1, 2, 3, 4, 5, 6,
                                   7, 8, 9, 10, 11, 12, 13]
                    for iii in done:
                            col.remove(iii)
                    for j in col:
                        d1[a:a+1, j:j+1] = 0    
    return d1,col


def clean(dx, d, done):
    #print(d1)
    import numpy as np
    gg = []
    index=[]
    for i in done:
        g = d[i]
        gg.append(g)
    arr1 = np.array(gg)
    d2 = (arr1.transpose())
    #print(g)
    for i in g:
        #print (i)
        if i>0:
            #print(i)
            #a=g[19]
            #print(a)
            for j in range (len(g)):
                a=g[j]
                #print(a)
                #print(i)
                if a==i:
                    index.append(j)
  
    #print(index)
    
    item = []
    #js = []
    for i in d2:
        js = []
        #print(i)
        t = 0
        tt=1
        cg=[]
        c=list(i)
        cf=len(c)-1
        #print(c[cf])
        for ii in i:
            #print(i,ii)
            if ii > 0:
                t += 1
            else:
                t += 0
        item.append(t)
    #print(item)
   
    for i in range(len(item)):
        if item[i] > 1:
            js.append(i)
    
    #print(js) ##
    for x in js:
        xx = (d2[x:x+1, :])
        #print(xx)
        for i in xx:
            xxx = []
            cole = []
            s = list(i)
            #print(s)
            for j in s:
                if j > 0:
                    ss = (s.index(j))
                    xxx.append(ss)
            col = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            for der in xxx:
                trd = done[der]
                col.remove(trd)
                cole.append(trd)
            #print(cole)
            #print(d1)
            for j in col:
                #print(j)
                for i in js:
                    dx[i:i+1, j:j+1] = 0
    item.clear()                
    return dx




def tieclearance(indx,done,d1):
    elements = {}
    for i in indx:
        #print(i)
        sum=0
        for k in range(13):
            sum+= d1[i][k]
        elements[i]= sum
        #print(elements)
        sum=0
        ded=[]        
    for key in elements:
        a=elements[key]
        ded.append(a)
    #print(ded)
    ded1=min(ded)
    xc=ded.index(ded1)
    c=indx[xc]
    #print(c)
    ij=len(done)-1
    #print(ij)
    j=done[ij]
    #print(j)
    #print(d1)
    d1[c:c+1,j:j+1]=0 
    #print (d1)    
    return d1                       
main()