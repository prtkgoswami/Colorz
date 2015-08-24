#
#	_________________________________________________
#	|_______________CODE CONVERTER____________|O|-|X|
#	|			 ________________	____________	|
#	|	HEX CODE |______________|	|__CONVERT__|	|
#	|			 ________________	____________	|
#	|	RGB CODE |______________|	|__CONVERT__|	|
#	|_______________________________________________|
#	

from Tkinter import *
root = Tk()

# VARIABLES
d1 = StringVar()
d2 = StringVar()

# FUNCTIONS
def hexify(n):
	hexa=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
	s=""
	while (n>1):
		s+=hexa[n%16]
		n/=16
	return s

def rgbToHex():
	s=e2.get()
	s=[int(i) for i in s.rstrip(')').lstrip('(').split(',')]
	strg="#"
	for e in s:
		strg+=hexify(e)
	d1.set(strg)

def hexToRgb():
	hexa=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
	s=e1.get()
	s=s.lstrip('#')
	s=[s[:2],s[2:4],s[4:6]]
	s=[list(e) for e in s]
	strg="("
	count=0
	for e in s:
		count+=1
		t=hexa.index(e[0])*16+hexa.index(e[1])
		if count<3:
			strg+=str(t)+","
		elif count==3:
			strg+=str(t)+")"
	d2.set(strg)

def reset():
	d1.set("#")
	d2.set("(")


d1.set("#")
d2.set("(")
root.title("COLOR CODE CONVERTER")
root.configure(background="#2f2f2f")

hexframe = Frame(root)
hexframe.pack(side=TOP)
hexframe.configure(background="#2f2f2f")
rgbframe = Frame(root)
rgbframe.pack(side=TOP)
rgbframe.configure(background="#2f2f2f")
cframe = Frame(root)
cframe.pack(side=BOTTOM)
cframe.configure(background="#2f2f2f")

l1=Label(hexframe,font="Helvetica 18",fg="#f5f5f5",bg="#2f2f2f",text=" Hex Code")
l1.pack(side=LEFT)
e1=Entry(hexframe,font="Helvetica 20",fg="#2f2f2f",bg="#1de9b6",justify="left",textvariable=d1)
e1.pack(side=LEFT)
b1=Button(hexframe,command=hexToRgb,font="Helvetica 18",fg="#f5f5f5",bg="#212121",text="Convert to RGB")
b1.pack(side=RIGHT)
l2=Label(rgbframe,font="Helvetica 18",fg="#f5f5f5",bg="#2f2f2f",text="RGB Code")
l2.pack(side=LEFT)
e2=Entry(rgbframe,font="Helvetica 20",fg="#2f2f2f",bg="#1de9b6",justify="left",textvariable=d2)
e2.pack(side=LEFT)
b2=Button(rgbframe,command=rgbToHex,font="Helvetica 18",fg="#f5f5f5",bg="#212121",text=" Convert to Hex ")
b2.pack(side=RIGHT)
reset=Button(cframe,command=reset,font="Helvetica 20",fg="#f5f5f5",bg="#b71c1c",text="Reset",width="20")
reset.pack()

root.mainloop()