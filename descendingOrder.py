"""
Name:    descendingOrder.py
Purpose: Enter three numbers and print them in descending order using if statements.
Author:  Adam P
"""
firstNumber = int(input("Enter a number: "))
                  
secondNumber = int(input("Enter another number: "))
                   
thirdNumber = int(input("Enter another number: "))

if firstNumber > secondNumber > thirdNumber:
    print("Here are your numbers in descending order:", firstNumber,",",secondNumber,",",thirdNumber)
elif firstNumber > thirdNumber > secondNumber:
      print("Here are your numbers in ascending order:", firstNumber, ",", thirdNumber, ",", secondNumber)
elif secondNumber > firstNumber > thirdNumber:
      print("Here are your numbers in descending order:", secondNumber, ",", firstNumber, ",", thirdNumber)
elif secondNumber > thirdNumber > firstNumber:
      print("Here are your numbers in descending order:", secondNumber, ",", thirdNumber, ",", firstNumber)
elif thirdNumber > firstNumber > secondNumber:
      print("Here are your numbers in descending order:", thirdNumber, ",", firstNumber , ",", secondNumber)
elif thirdNumber > secondNumber > firstNumber:
      print("Here are your numbers in descending order:", thirdNumber, ",", secondNumber, ",", firstNumber)
