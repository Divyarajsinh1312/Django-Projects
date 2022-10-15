s=[1,3,0,5,3,5,6,8,8,2,12]
f=[4,5,6,7,8,9,10,11,12,13,14]
selectedActivity=["Act1"]
j=1
for i in range(2,len(s)):
    if s[i]>=f[j]:
        a="Act"+str(i+1)
        selectedActivity.append(a)
        j=i
print(selectedActivity)