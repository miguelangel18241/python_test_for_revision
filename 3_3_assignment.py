score = input ("What is the score? ")
try:
    scoreNumber = float(score)
except:
    print('Something is wrong!!!')
    quit()
if scoreNumber >= 1.1:
    print ("Value is higher than accepted")
    quit()
if scoreNumber >= 0.9 :
    print('A')
elif scoreNumber >= 0.8 :
    print('B')
elif scoreNumber >= 0.7 :
    print('C')
elif scoreNumber >= 0.6 :
    print('D')
else :
    print ('F')
