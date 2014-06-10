f1 = open('mhr1.txt')
f2 = open('mhr2.txt')
a1 = []
a2 = []
for l in f1:
	a1.append(l.decode('utf-8'))
for l in f2:
	a2.append(l.decode('utf-8'))
for l in a2:
	if not l in a1:
		print l.encode('utf-8')
