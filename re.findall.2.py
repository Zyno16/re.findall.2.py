import re 
x = "From: using the : character "
y = re.findall("^F.+?:",x)
print("y is ",y)
# y = will print from:   ? is mean no greedy
z = re.findall("^F.+:",x)
print("z is ",z)
w=re.findall("^F.:",x)
print("w is ",x)

emal = "From stephen.marquard@uct.ac.za 
Sat Jan 5 0:14:15 2008"

r=re.findall("\S+@\s+",emal)
print("r is ",r)

