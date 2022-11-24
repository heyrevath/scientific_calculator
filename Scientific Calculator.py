import math 

print("1 - Addition")
print("2 - Substraction")
print("3 - Multiplication")
print("4 - Division")
print("5 - Mod")
print("6 - Square Root")
print("7 - Exponent")
print("8 - Sin")
print("9 - Cos")
print("10 - Tan")
print("11 - Radian")
print("12 - Degree")

while True:
  print('\033[1m' + "\nSelect any operation" + '\033[0m')
  print("\n'Q' or 'q' or 'exit' or 'Exit' or 'EXIT' ---> To Quit")

  choice = input("\nEnter Choice (1/2/3/4/...) : ") 
  if choice == "1": 
      x = eval(input("\n1st number : ")) 
      y = eval(input("2nd number : ")) 
      print(x,"+", y ,"=",x + y) 

  elif choice == "2": 
      x = eval(input("\n1st number : ")) 
      y = eval(input("2nd number : ")) 
      print(x,"x", y ,"=",x-y) 

  elif choice == "3": 
      x = eval(input("\n 1st number : ")) 
      y = eval(input("2nd number : ")) 
      print(x,"-", y ,"=",x*y) 

  elif choice == "4": 
      x = eval(input("\n1st number : ")) 
      y = eval(input("2nd number : ")) 
      print(x,"/", y ,"=",x/y) 

  elif choice == "5": 
      x = eval(input("\n1st number : ")) 
      y = eval(input("2nd number : "))  
      print(x,"%", y ,"=",x%y)

  elif choice == "6": 
      x = eval(input("\nNumber is : ")) 
      print("√",x,"=",math.sqrt(x)) 

  elif choice == "7": 
      x = eval(input("\n1st number : ")) 
      y = eval(input("2nd number : ")) 
      print(x,"^",y,"=",math.pow(x,y)) 

  elif choice == "8": 
      x = eval(input("\nNumber is : "))  
      print("sin(",x,") =",math.sin(x)) 

  elif choice == "9": 
      x = eval(input("\nNumber is : ")) 
      print("cos(",x,") =",math.cos(x)) 

  elif choice == "10": 
      x = eval(input("\nNumber is : "))  
      print("tan(",x,") =",math.tan(x)) 

  elif choice == "11": 
      x = eval(input("\nNumber is : "))  
      print(x, "Degree =",math.radians(x),"Radian") 
      
  elif choice == "12": 
      x = eval(input("\nNumber is : "))  
      print(x,"Radian =",math.degrees(x),"Degree") 

  elif choice == "q" or choice == "Q" or choice == "exit" or choice == "Exit" or choice == "EXIT":
      print('\033[1m' + "\nSuccesfully Exited!" + '\033[0m')
      break
