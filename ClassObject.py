# OBJECT CLASS
class Computer:
    def config(self):
        print("i,16gb,1TB")


comp1 = Computer()
comp1.config()  # object comp1 is used to call config
Computer.config(comp1)  # config method belong to comp1 and passing object comp1
print(type(comp1))
