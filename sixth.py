print("Enter your choice : \n 1. display the containt os single file \n 2. display the containt pf multiple file \n 3. cat -n command \n 4. cat -e command")

c=input()
if c=='1':
    fname=input("enter file :")
    f=open(fname,"r")
    print(f.read())
    f.close()
elif c=='2':
    fno=int(input("Enter no. of files "))
    fname=[]
    print("enter name of files : ")
    for i in range(1,fno+1):
        name=input()
        fname.append(name)

    for i in range(1,fno+1):
        f=open(fname[i],'r')
        print(f.read())
elif c=='3': 
    fname=input('Name of file :')
    f=open(fname,'r') 
    data = f.read()
    a=data.split('\n')
	
    n=1
    for i in a:
        print(str(n)+' ' +i)
        n=n+1

elif c == '4':
	fname=input('Name of file :')
	f=open(fname,'r')
	data=f.read()
	a=data.split('\n')
	for i in a:
         print(i+'$')

else: print("wrong")


