## Assignment Part-1
#Q1. Why do we call Python as a general purpose and high-level programming lauageng?

#There are two reason:Python is general purpose and high-level programing language.
#1.object oriented- This language is based around objects such as data rather than functions.
#2.High-level programming language-Mainly because it is easy for human to understand.

#Q2. Why is Python called a dynamically typed language?

#Python don't have any problem even if we dont declare the type of variable. 
#It states the kind of varaible in the runtime of the program.
#Python also take cares of the memory management which is crucial in programming .
#So, python is a dynamically typed language

#Q3. List some pros and cons of Python programming language?

#PROS:
#a.Extensive Libraries 
#Python features an extensive set of libraries and contains code for various purposes like documentation-generation, 
#regular expressions, web-browsers, unit-testing, CGI, databases, image manipulation, etc. 
#Hence, it eliminates the need to write the complete code manually.

#b. Embeddable
#Python is extensible, and most of its codes can even be written in other languages such as C++. 
#This lets us add scripting capabilities to our code in the other language.

#C.Portable
#Python is portable, which means it can be run on any other platform. 
#Here, you need to code only once, and you can run it anywhere. 
#This is called WORA (Write Once Run Anywhere). 
#This makes it easier for the developers to work with Python 
#as they do not need to make changes to it in case they want to run it on another platform.

#CONS:

#a. Issues with Design
#Python developers sometimes have to deal with complicated designs. 
#Therefore, highly efficient and experienced developers are preferred over beginners.

#b. Slower than Compiled Languages
#Python is slow compared to other non-compiled languages as it requires a lot of computational power. 
#So, this is the thing that you need to look at before choosing Python.

#c. Security
#Python is not 100% secure. You need to take the necessary steps to ensure the code’s security. 
#However, performing the right QA testing can fix this concern.


#Q4. In what all domains can we use Python?

#Python is the go-to programming language for domains such as artificial intelligence, machine learning 
#and deep learning, it's no surprise that it's also a fundamental tool for any data scientist.

#Q5. What are variable and how can we declare them?

#Variable is a name given to a memory location in a program.
#Python has no command for declaring a variable. A variable is created the moment you first assign a value to it


#Q6. How can we take an input from the user in Python?
            # for ex- syntax to take an input from the user
#name=input("Enter your name:")

#Q7. What is the default datatype of the value that has been taken as an input using input() function?

#In Python, the user's input is read and returned as a string using the input( ) method.

#Explanation:
#In Python, we implement the input() function to get user input. 
T#he input function translates whatever you give it as input into a string.
 #Even if an integer value is entered, the input() method accepts it as a string.

#Syntax: input(prompt)

#Parameter:

#Prompt: (optional) The string to write to standard output (typically the screen) without a newline.

#By default, it returns a string object.

#Q8. What is type casting?

#The conversion of one data type into the other data type is known as type casting in python or type conversion in python.
 #Python supports a wide variety of functions or 
 #Methods like: int(), float(), str(), tuple(), set(), list(), dict(), etc. for the type casting in python

# Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

# Yes,we can take more than one input from the user using single input() function.
# Given below is the example to support the arugment,
# x, y, z = input("Enter three values: ").split()  
# print("Total number of students: ", x)  
# print("Number of passed student : ", y)  
# print("Number of failed student : ", z)  
# print()

# Q10. What are keywords?

# Python keywords are special reserved words that have specific meanings 
# and purposes and can't be used for anything but those specific purposes. 
# These keywords are always available—you'll never have to import them into your code.

# Q11. Can we use keywords as a variable? Support your answer with reason.

# We cannot use a keyword as a variable name, function name, or any other identifier.
#  They are used to define the syntax and structure of the Python language.
#   All the keywords except True , False and None are in lowercase and they must be written as they are.

# Q12. What is indentation? What's the use of indentaion in Python?

# Indentation refers to the spaces at the beginning of a code line.
#  Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
#   Python uses indentation to indicate a block of code.

# Q13. How can we throw some output in Python?

# The basic way to do output is the print statement. 
# To end the printed line with a newline, add a print statement without any objects.
#  This will print to any object that implements write(), which includes file objects.

# Q14. What are operators in Python?

# In Python, there are seven different types of operators:
#  arithmetic operators, assignment operators, comparison operators, logical operators, identity operators, and boolean operators.

# Q15. What is difference between / and // operators?

# /=Single quote
# //=backslash

# Q16. Write a code that gives following as an output.
# ```
# iNeuroniNeuroniNeuroniNeuron
# print ('iNeuroniNeuroniNeuroniNeuron')
```
# Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

# num=int(input('Enter the number'))
# if num%2==0:
#     print("The given number is even:",num)
# else:
#     print('The given number is odd:',num)

# Q18. What are boolean operator?

#   and,or,not  are boolean oprator.

# Q19. What will the output of the following?
# ```
# 1 or 0

# 0 and 0

# True and False and True

# 1 or 0 or 0
```

# Q20. What are conditional statements in Python?

# Conditional Statements: if statement, if-elif statement if-else statement

# Q21. What is use of 'if', 'elif' and 'else' keywords?

# if=The if keyword is used to create conditional statements,
#    and allows you to execute a block of code only if a condition is True.

# elif=The elif keyword is pythons way of saying if the previous conditions were not true, then try this condition.

# else=The else keyword is used in conditional statements , and decides what to do if the condition is False.

# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".

# age=int(input("Enter your age:"))
# if age>=18:
#     print("I can vote")
# else:
#     print("I can't vote")


Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```


#Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
# num1=int(input('Enter the first number:'))
# num2=int(input('Enter the second number:'))
# num3=int(input('Enter the third number:'))
# if(num1>num2) and (num1>num3):
#     print("Greatest number is: ",num1)
# elif(num2>num1) and (num2>num3):
#     print("Greatest number is: ",num2)
# else:
#     print("Greatest number is: ",num3)

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]