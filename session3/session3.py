# Program created by Muhammad Fikry Haikal
# TI22I class


#input 
print("=" * 25, "Biodata Apps", "=" * 25)

name = input("Please, enter your name: ")
age = int(input("Enter your age: "))
kelas = input("Enter your class: ")
major = input("Enter your major: ")
motto = input("Enter your motto: ")
favoriteFood = input("Do you like mie || yes/no: ")

hobbie_1 = input("Enter your hobbie 1 : ")
hobbie_2 = input("Enter your hobbie 2 : ")
hobbie_3 = input("Enter your hobbie 3 : ")

hobbies = [hobbie_1,hobbie_2,hobbie_3]

print("=" * 60)


#condition 
if favoriteFood == "yes":
    favoriteFood = True
else:
    favoriteFood = False


#display 

print(f"Name :             {name}")   
print(f"Age  :             {age}")        
print(f"Class :           {kelas}") 
print(f"Major :           {major}")        
print(f"Motto :           {motto}")        
print(f"Favorite food : {favoriteFood}")        
print(f"Hobbie :          {hobbies}")        
   


