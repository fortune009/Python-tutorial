#while<condition>:
# -statement
'''while True:
    print('This is a loop')'''
'''i = 0
while i<=100:
    print(i)
    i=i+1 #or i+=1'''
'''i = 0
while i<=20:
    print(i)
    i=i+2 #or i+=1'''
un_verified = ['lord123', 'star12', 'ade4','john', 'christable01']
verified = []
while un_verified:
    user = un_verified.pop(0) 
    verified.append(user) 
    print(f'{user} has been verifed')
print('\n')
print('Verified users are:', verified)
print('unverified users are:', un_verified)