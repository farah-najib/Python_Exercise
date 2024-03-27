# Write a program that takes two integers as input, base and exponent, and calculates the power using loops.

base =  int(input("Enter base: "))
exponent =  int(input("Enter exponent: "))
reslut=1
for i in range(1,exponent+1) :
    reslut=reslut*base

print(reslut)

