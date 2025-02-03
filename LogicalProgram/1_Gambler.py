import random
stake=int(input("Enter the stake amount: "))
goal=int(input("Enter the goal amount: "))
bet_amount=1
#number_of_times=0
number_of_times=int(input("Enter the number of times to play: "))
win=0
loss=0

#while stake>0 and stake<goal:
    #random_value=random.randint(0,1)
for i in range(number_of_times):
    random_value=random.randint(0,1)
    if random_value==1:
        stake=stake+bet_amount
        win+=1
        #number_of_times+=1
    else:
        stake=stake-bet_amount
        loss+=1
        #number_of_times+=1
    


percentage_of_win=(win/number_of_times)*100
percentage_of_loss=(loss/number_of_times)*100
#print("Number of times played: ",number_of_times)
print("Number of win: ",win)
print("Number of loss: ",loss)
print("Percentage of win: ",percentage_of_win)
print("Percentage of loss: ",percentage_of_loss)
