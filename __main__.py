i=0
target=input('target is: ')
import ipadress, requests, time
t=time.time()
while True:
	try:
		if requests.post(targer):
			pass
		else:
			i=i+1
	except:
    	try:
			ipadress.ip_adress(target)
 			i=i+1
		except:
			print('wrong target eror!')
			break
	print('request #'+str(i))
print(time.time()-t)
