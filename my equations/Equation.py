import math
class Quadratic_Equation():
    """This class is meant to help u work out a quadratic equation.
    it involves the basic algorithms of how to solve them"""
    def __init__(self,first,second,third,naming):
        self.first=first
        self.second=second
        self.third=third
        self.naming=naming
        
    def initialisation(self):
        """Working out the quadratic equation"""
        active=True
        while active:
            nassim=-(self.second)
            ntambi=(2.0*self.first)
            teddy=((self.second*self.second)-(4.0*self.first*self.third))
            if teddy>=0:
                nina=math.sqrt(teddy)
            else:
                active=False
            #euler initialisation
                print("This quadratic equation is not valid but can be given in euler form",self.naming.title())
                sewaya=teddy*-1
                sophia=math.sqrt(sewaya)
                first_x=(nassim+sophia)/ntambi
                second_x=(nassim-sophia)/ntambi
                print(self.naming.title(),"your answer in euler form is:",first_x,"i")
                print(self.naming.title(),"your answer in euler form is:",second_x,"i")
                break
            first_x=(nassim+nina)/ntambi
            second_x=(nassim-nina)/ntambi
            #printing answers
            print(self.naming.title(),"your answer is:",first_x)
            print(self.naming.title(),"your answer is:",second_x)
            break
            
            
            
class cubic_equation(Quadratic_Equation):
    """This class is meant to solve a cubic equation """
    def __init__(self,first,second,third,naming,fourth):
        super().__init__(first,second,third,naming)
        self.fourth=fourth
        
    def division(self):
        test_1=self.first+self.second+self.third+self.fourth
        alternate_1=self.fourth+self.second
        alternate_2=self.first+self.third
        if test_1==0:
            print(self.naming.title(),"your answer is:",1)
            value=1
            derrick=self.fourth*value+self.first
            Evans=derrick*value+self.second
            proceed=[]
            #Storing calculated values in a list "proceed" to be returned for further calculations 
            proceed.append(self.fourth)
            proceed.append(derrick)
            proceed.append(Evans)
            return proceed
            
                            
        elif (alternate_1==alternate_2):
            print(self.naming.title(),"your answer is:-1")
            value=-1
            derrick=self.fourth*value+self.first
            Evans=derrick*value+self.second
            proceed=[]
            #Storing calculated values in a list "proceed" to be returned for further calculations
            proceed.append(self.fourth)
            proceed.append(derrick)
            proceed.append(Evans)
            return proceed
            
                                
        else:
            forward=True
            while forward:
                for value in range(-100,100):
					# Carrying out yhe synthetic division
                    synthetic_divisor=((((((self.fourth*value)+self.first)*value)+self.second)*value)+self.third)
                    if synthetic_divisor==0:
                        print(self.naming.title(),"your answer is:",value)
                        derrick=self.fourth*value+self.first
                        Evans=derrick*value+self.second
                        proceed=[]
                        #Storing calculated values in a list "proceed" to be returned for further calculations
                        proceed.append(self.fourth)
                        proceed.append(derrick)
                        proceed.append(Evans)
                        return proceed
                        break
                    else:
                        value=(value/10)
                        # Carrying out yhe synthetic division
                        synthetic_divisor=((((((self.fourth*value)+self.first)*value)+self.second)*value)+self.third)
                        if synthetic_divisor==0:
                            print(self.naming.title(),"your answer is:",value)
                            derrick=self.fourth*value+self.first
                            Evans=derrick*value+self.second
                            proceed=[]
                            #Storing calculated values in a list "proceed" to be returned for further calculations
                            proceed.append(self.fourth)
                            proceed.append(derrick)
                            proceed.append(Evans)
                            return proceed
                            break
                        
                                
                        
                        
                         
                    
            
                
            
                                    
        
        





