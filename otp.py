a=input()
op=''
#n= [int(x) for x in input_str.split()]
for i in range(1,len(a),2):
    op+=str(int(a[i])**2)
print(op[:4])