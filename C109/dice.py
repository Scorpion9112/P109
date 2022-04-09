import random 
import statistics
import plotly.figure_factory as ff

diceResult=[]


for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceSum=dice1+dice2
    diceResult.append(diceSum)

mean=statistics.mean(diceResult)
mode=statistics.mode(diceResult)
median=statistics.median(diceResult)
sd=statistics.stdev(diceResult)

figure=ff.create_distplot([diceResult],["Dice Results"], show_hist=False)
figure.show()
print(mean)
print(mode)
print(median)
print(sd)