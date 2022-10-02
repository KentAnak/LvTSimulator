import numpy as np

class Human():
    def __init__(self):
        self.talent = np.random.normal(0.6, 0.1, None)
        self.wealth = 10
        self.lucky_cnt = 0
        self.unlucky_cnt = 0
        
    def face_event(self):
        freq = np.random.poisson(lam=0.45)
        for i in range(1,freq):
            lucky = bool(np.random.randint(0,2))
            if lucky:
                if(np.random.random() < self.talent):
                    self.wealth *= 2
                self.lucky_cnt +=1
            else:
                self.wealth =  self.wealth/2
                self.unlucky_cnt +=1

    def header(): return "wealth,talent,lucky_cnt,unlucky_cnt"
    def to_str(self): return f"{self.wealth},{self.talent},{self.lucky_cnt},{self.unlucky_cnt}" 


class SociableHuman(Human):
    def __init__(self):
        super().__init__()

    def face_event(self): # overrides
        freq = np.random.poisson(lam=self.talent-0.15) 
        for i in range(1,freq):
            lucky = bool(np.random.randint(0,2))
            if lucky:
                if(np.random.random() < self.talent):
                    self.wealth *= 2
                self.lucky_cnt +=1
            else:
                self.wealth =  self.wealth/2
                self.unlucky_cnt +=1

class PreventiveHuman(Human):
    def __init__(self):
        super().__init__()

    def face_event(self): # overrides
        freq = np.random.poisson(lam=0.5) 
        for i in range(1,freq):
            lucky = bool(np.random.randint(0,2))
            if lucky:
                if(np.random.random() < self.talent):
                    self.wealth *= 2
                self.lucky_cnt +=1
            else:
                if(np.random.random() > self.talent):
                    self.wealth =  self.wealth/2
                self.unlucky_cnt +=1

def run_simulation(class_arg):
    population = []
    for n in range(1000):        
        population.append(class_arg())

    for i in range(80):
        for man in population:
            man.face_event()
    try:
        with open("data.csv", "w") as file:
            file.write(Human.header()+"\n")
            for man in population:
                file.write(man.to_str()+"\n")
    except:
        print("write file error.")

#run_simulation(Human)
#run_simulation(SociableHuman)
run_simulation(PreventiveHuman)



