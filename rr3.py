import time
if __name__ == "__main__": 
	count=0
	j=0
	s=0
	n=0
	i=0
	time=0
	remain=0
	flag=0
	dict=[]
	time_quantum=5 
	wait_time=0
	turnaround_time=0
	infile=open('f2','r')
        data=infile.readline().split()
        while data:
		n=n+1
		d={}
		d[data[-6]]=data[-5]
		d[data[-4]]=data[-3]
		d[data[-2]]=data[-1]
		dict.append(d)
		data=infile.readline().split()
	while i<n:
		dict[i]["rt"]=dict[i]["bt"]
		i=i+1
	remain=n  
	time=0
	count=0
	while remain<>0: 
		if int(dict[count]["rt"])<=time_quantum and int(dict[count]["rt"])>0: 
      			time=time+int(dict[count]["rt"]) 
      			dict[count]["rt"]=0 
      			flag=1
    		elif int(dict[count]["rt"])>0:
			dict[count]["rt"]=int(dict[count]["rt"])-time_quantum 
			time=time+time_quantum 
    		if int(dict[count]["rt"])==0 and flag==1: 
      			remain=remain-1
			print "process",dict[count]["pn"]
			print "executed"
      			print "process:",count+1
			print "turnaround time:",time-int(dict[count]["at"])
			print "waiting time:",time-int(dict[count]["at"])-int(dict[count]["bt"]) 
			flag=0
		if count==n-1: 
      			count=0 
    		elif int(dict[count+1]["at"])<=time: 
      			count=count+1 
		else: 
      			count=0 
	exit()
