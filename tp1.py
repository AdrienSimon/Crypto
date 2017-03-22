#cle=011
import binascii
 


def cryptageVernam(message,cle):
	messageSplitted=list(message)
	cleSplitted=list(cle)

	for i in range(len(messageSplitted)):
		#print cleSplitted[i%(len(cleSplitted))]
		if cleSplitted[i%(len(cleSplitted))]!=messageSplitted[i]:
			messageSplitted[i]="1"
		else:
			messageSplitted[i]="0"
	#print messageSplitted
	return ''.join(messageSplitted)

message='01111010000'
cle="1100"

print "MESSAGE : "+message

print "CLE : "+cle
print "Cryptage.."
print "MESSAGE : "+cryptageVernam(message,cle)




