# your code goes here
t=int(input())
for i in range (t):
	string=input()
count_a=0
count_b=0
count_c=0
d={}
d[count_a,count_b,count_c]=1
for i in string:
	if (i=="a"):
		count_a+=1
	elif(i=="b"):
		count_b+=1
	elif(i=="c"):
		count_c+=1
	k=min(count_a,count_b,count_c)
	count_a-=k
	count_b-=k
	count_c-=k
	if (count_a,count_b,count_c) not in d :
		d[count_a,count_b,count_c]=1
	else:
		d[count_a,count_b,count_c]+=1
sum=0
for i in d.values():
	sum+=(i*(i-1))//2
print(sum)

		

