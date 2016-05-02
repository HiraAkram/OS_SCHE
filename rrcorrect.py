import time
if __name__ == "__main__": 
	c=0
	j=0
	s=0
	n=0
	i=0
	time=0
	m=0
	flag=0
	dict=[]
	time_quantum=5 
	wait_time=0
	wta=4
	wtf=4
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
	m=0  
	time=0
	c=0
	while m<>n: 
		if int(dict[c]["rt"])<=time_quantum and int(dict[c]["rt"])>0: 
      			time=time+int(dict[c]["rt"]) 
      			dict[c]["rt"]=0 
      			flag=1
    		elif int(dict[c]["rt"])>0:
			dict[c]["rt"]=int(dict[c]["rt"])-time_quantum 
			time=time+time_quantum 
		if int(dict[c]["rt"]<=time_quantum and int(dict[c]["rt"])>0 and int(dict[c]["bt"]-dict[c]["rt"])==wta:
			print "process waiting"
			time=time+wtf
			wta=wta*2
		elif int(dict[c]["rt"])>0 and int(dict[c]["bt"]-dict[c]["rt"])==wta:
			print "process waiting"
			time=time+wtf
			wta=wta*2
    		if int(dict[c]["rt"])==0 and flag==1: 
      			m=m+1
			print "process",dict[c]["pn"]
			print "executed"
      			print "process:",c+1
			print "turnaround time:",time-int(dict[c]["at"])
			print "waiting time:",time-int(dict[c]["at"])-int(dict[c]["bt"]) 
			flag=0
		if c==n-1: 
      			c=0 
    		elif int(dict[c+1]["at"])<=time: 
      			c=c+1 
		else: 
      			c=0 
	exit()
