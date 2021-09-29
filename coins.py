# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #hoeveel je moet betalen * 100 
paid = int(float(input('Paid amount: ')) * 100) # hoeveel je hebt betaald * 100
change = paid - toPay #Hoeveel change je terug moet krijgen

if change > 0: #miminum
  coinValue = 500 #maximum
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #Hier rekent het al uit qua wisselgeld en gaat vragen hoeveel je terug wilt
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #hier geldt ongeveer het zelfde
      change -= nrCoinsReturned * coinValue 


# comment on code below: 
    if coinValue == 500: 
      coinValue = 300
    elif coinValue == 300: 
      coinValue = 200
    elif coinValue == 200: 
      coinValue = 100
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:  
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #Als je de change niet terug geeft dan krijg je dit te zien
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')
