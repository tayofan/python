class Animal:
    def __init__(self):
        self.age = 0
        
    def getOld(self):
        self.age += 1

class Human(Animal):
    def __init__(self):
        super().__init__()
        self.skill_lang = 0
        
    def momstouch(self,stroke):
        self.skill_lang += stroke


if __name__ == '__main__': #테스트할때는 main을 해서 태스해야 다른곳에서 실행이되지 않는다
    ani = Animal()
    print("myoop01",ani.age)
    ani.getOld()
    print("myoop01",ani.age) 
      
    hum = Human()
    print("age",hum.age)
    print("skill_lang",hum.skill_lang)
    hum.getOld()
    hum.momstouch(10)
    print("age",hum.age)
    print("skill_lang",hum.skill_lang)   
    

    
    