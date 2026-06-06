# class Vehicle:

#     def __init__(self,color,speed,milage):

#         self.color=color
#         self.speed=speed
#         self.milage=milage

#     def vehicle_info(self):

#         print("Color :",self.color)
#         print("Speed :",self.speed)
#         print("Milage :",self.milage)
#         print("---------------------------")


# list1=[]

# for i in range(3):

#     color=input("Enter color of vehical :")
#     speed=int(input("Enter top speed :"))
#     milage=int(input("Enter milage of vehical :"))

#     v1=Vehicle(color,speed,milage)
#     list1.append(v1)

# print("Vehicle Details")
# print('--------------------')

# for obj in list1:

#     obj.vehicle_info()






# class Method:

#     def method_a(self):
#         print("Final step reached")

#     def method_b(self):
#         self.method_a()

#     def method_c(self):
#         self.method_b()

# c1=Method()
# c1.method_c()


class Fraction:

    def __init__(self,numerator,denominator):

        self.numerator=numerator
        self.denominator=denominator

    def __str__(self):

        return "{}/{}".format(self.numerator,self.denominator)
    

    # Addition of two fractions a/b + c/d 
    def __add__(self,other): # fraction 1 =self and fraction 2 = other
        
        new_num =  self.numerator * other.denominator + self.denominator * other.numerator  # a*c + b*d
        new_den =  (self.denominator * other.denominator)  # b * d

        return Fraction(new_num,new_den)
    
f1=Fraction(1,2)
print("Fraction 1 :",f1)

f2=Fraction(3,4)
print("Fraction 2 :",f2)

print("Addition of two object :",f1+f2) # it will call __add__ using obj1+obj2