n=int(input());l=5526
for i in input().split(): 
    t=int(i) 
    if abs(t)==abs(l)and l<0:l=t
    elif abs(t)<abs(l):l=t 
if n!=0:print(l)
else:print(0)
