
#Trouve les nombres de premier inferieur a n avec la methode du crible d eratostene
def eratos(n):
	print "test"
	tab =[i for i in range(1,n+1)]
	for j in range(2,n+1):
		for i in range(n):
			if tab[i]%j == 0 and tab[i]!=j and tab[i]!=0:
				tab[i]=0
	
	
	i=0
	while i<len(tab):
		if tab[i]==0 or tab[i]==1:
			tab.pop(i)
			i=i-1
		i+=1
	print tab
	return tab

#Calcule la decomposition primaire de N
def decomp_primaire(n):
	m=n
	tab=eratos(n)
	resultat=[]
	tempo=0
	for i in tab:
			while n%i==0:
				n=n/i
				tempo+=1
			if tempo!=0:
				resultat.append(i)
				resultat.append(tempo)
				tempo=0
	test=[]
	for i in range(len(resultat)):
		if i%2==0:
			test.append(resultat[i])
			test.append("^")
		else:
			test.append(resultat[i])
			if i!=(len(resultat)-1):
				test.append("*")
	print "Decomposition primaire de ",m,":"
	print ''.join(map(str,test))
	return resultat

# Calcule l'indice d'euler de N
def indice_euler(n):
	if n==1:
		return 1
	tab=decomp_primaire(n)
	phi=1
	for i in range(len(tab)):
		if i%2==0:
			phi=phi*((tab[i]**tab[i+1])-(tab[i]**(tab[i+1]-1)))
	print "indice d euler =", phi
	return phi





#theoreme de bachet bezout
def divEuc(a,b,u1=1,v1=0,u2=0,v2=1):
	r1=a*u1+b*v1
	r2=a*u2+b*v2
	while r2!=0:
		q= r1//r2
		(r1,u1,v1,r2,u2,v2)=(r2,u2,v2,r1-q*r2,u1-q*u2,v1-q*v2)
	s=str(r1)+"="+str(a)+"*"+str(u1)+"+"+str(b)+"*"+str(v1)
	return s


#Calcule le reste de n^p modulo m
def modulopuissance(n=input(),p=input(),m=input()):

	liste=[1]
	debut=n%m
	liste.append(debut)
	courant=(debut*n)%m
	while (courant not in liste):
		liste.append(courant)
		courant=(courant*n)%m
		if courant==0:
			liste.append(courant)
			print liste
			print (n**p)%m
			return 0
		if (len(liste)) == p:
			liste.append(courant)
			print liste
			print (n**p)%m
			return courant
		
	liste.append(courant)
	print liste
	a=len(liste)-1
	reste=p%a
	print (n**p)%m
	return liste[reste]

n=101*103
print n
print indice_euler(n)

