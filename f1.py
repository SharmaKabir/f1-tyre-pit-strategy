import matplotlib.pyplot as plt
# print("hello")
import numpy as np 

class tyre:

    def __init__(self, compound, age, base):
        self.compound = compound
        self.age = age
        self.base = base

    def display(self):
        return 'Tyre compund: {} \n Age in Laps: {}'.format(self.compound, self.age)

    def lap_time(self):
        if(self.compound == 'H'):
            return (self.base+2.5)*(1.001)**self.age        
        if(self.compound == 'M'):
            return (self.base+1.6)*(1.003)**self.age      
        if(self.compound == 'S'):
            return self.base*(1.005)**self.age

def strategy(number_of_laps, c1, c2):
    time=500*number_of_laps
    pit_stop=0
    for i in range(number_of_laps):
        t=0

        c1_tyre = tyre(c1, 0, 90)
        t+=c1_tyre.lap_time()
        for j in range(i):

            c1_tyre=tyre(c1, c1_tyre.age+1, c1_tyre.base)
            t+=c1_tyre.lap_time()

        c2_tyre = tyre(c2, 0, 90)
        t+=c2_tyre.lap_time()
        for j in range(number_of_laps - i):
            c2_tyre=tyre(c2, c2_tyre.age+1, c2_tyre.base)
            t+=c2_tyre.lap_time()

        if time > t:
            time=t
        elif time < t:
            pit_stop=i-1
            break
    return pit_stop, time


def plot_strategy(number_of_laps, c1, c2):
    strat= strategy(number_of_laps, c1, c2)
    y1=[]
    c1_tyre= tyre(c1, 0, 90)
    y1.append(c1_tyre.lap_time())
    for j in range(strat[0]-1):
        c1_tyre= tyre(c1, c1_tyre.age+1, 90)
        y1.append(c1_tyre.lap_time())

    while(len(y1) != number_of_laps-1):
        y1.append(int(0))    

    y2=[]
    for j in range(strat[0]-1):
        y2.append(int(0))

    c2_tyre= tyre(c2, 0, 90)
    y2.append(c2_tyre.lap_time())
    y1.append(int(0))
    for j in range(number_of_laps - strat[0]):
        c2_tyre= tyre(c2, c2_tyre.age+1, c2_tyre.base)
        y2.append(c2_tyre.lap_time())    

    times= []
    t=0

    for i in range(number_of_laps):
        if y1[1] !=0:
            times.append(y1[i])
            t+=y1[i]
        else:
            times.append(y2[i])
            t+=y2[i]


    y2 = np.array(y2)
    y1= np.array(y1)
    y2[strat[0]]+= 15
    x=np.array([i+1 for i in range(number_of_laps)])                

    #print(len(y1), len(y2), len(x))
    
    if(c1=="S" and c2=="M"):
        plt.plot(x, y1, c="red")
        plt.plot(x, y2, c="yellow")
        plt.grid(c="orange")
        plt.show()
    elif(c1 == "S" and c2=="H"):
        plt.plot(x, y1, c="red")
        plt.plot(x, y2, c="black")
        plt.grid(c="orange")
        plt.show()
    elif(c1 == "M" and c2=="S"):
        plt.plot(x, y1, c="yellow")
        plt.plot(x, y2, c="red")
        plt.grid(c="orange")
        plt.show()
    elif(c1 == "M" and c2=="H"):
        plt.plot(x, y1, c="yellow")
        plt.plot(x, y2, c="black")
        plt.grid(c="orange")
        plt.show()
    elif(c1 == "H" and c2=="S"):
        plt.plot(x, y1, c="black")
        plt.plot(x, y2, c="red")
        plt.grid(c="orange")
        plt.show()
    elif(c1 == "H" and c2=="M"):
        plt.plot(x, y1, c="black")
        plt.plot(x, y2, c="yellow")
        plt.grid(c="orange")
        plt.show()
    else:
        plt.plot(x, y1, c="green")
        plt.plot(x, y2, c="green")
        plt.grid(c="orange")
        plt.show()

def pick_best(number_of_laps):
    best_c1= "S"
    best_c2= "M"
    best_time= strategy(number_of_laps, best_c1, best_c2)[1]
    
    new_time=strategy(number_of_laps, "S", "H")[1]
    if(new_time < best_time):
        best_time= new_time
        best_c1="S"
        best_c2="H"

    new_time=strategy(number_of_laps, "M", "H")[1]
    if(new_time < best_time):
        best_time= new_time
        best_c1="M"
        best_c2="H"

    plot_strategy(number_of_laps, best_c1, best_c2)

    return best_time/60, best_time%60, best_c1, best_c2
 
print(pick_best(int((input("Enter Number Of Laps: ")))))