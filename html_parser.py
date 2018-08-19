poems =[]
import urllib.request
import re
x = '<font face="幼圆"'.encode("gb2312")
print(x)
i=1
while (i<900):
    try:
        for j in range(1,900):
            print(str(i)+" "+str(j))
            fp = urllib.request.urlopen("http://www16.zzu.edu.cn/qtss/zzjpoem1.dll/viewoneshi?js="+'{:03}'.format(i)+"&ns="+'{:03}'.format(j))
            #print("http://www16.zzu.edu.cn/qtss/zzjpoem1.dll/viewoneshi?js="+'{:03}'.format(i)+"&ns="+'{:03}'.format(j))
            mybytes = fp.read()
            fp.close()
            #print(mybytes)
            k = mybytes.find(x)
            if k==-1:
                break
            k2=mybytes.find( '<br>'.encode("gb2312"),k)
            #print(k2)
            current_poem=[]
            wuyan=True
            while (k2!=-1):
                #print(k2)
                try:
                    s = mybytes[k:k2].decode("gb2312")
                except (Exception):
                    break
                k3 = s.find("&nbsp")
                s=s[k3+18:]
                s = re.split("，|。",s)
                for k4 in range(len(s)-1):
                    if len(s[k4])!=5:
                        wuyan=False
                        break
                    current_poem.append(s[k4])
                if not wuyan: break
                k=k2+1
                k2 = mybytes.find('<br>'.encode("gb2312"), k)
            if wuyan:
                poems.append(current_poem)
        #print(poems)
        print("Number of poems: " + str(len(poems)))
    except:
        print(len(poems))
    i+=1
import pickle
pickle.dump(poems,open("poems.pickle",'wb'))