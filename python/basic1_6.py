#Write a Python program to accept a filename from the user and print the extension of that
from fileinput import filename


filename = input("Input the file name : ")
f_extns = filename.split(".")
print("The Extension of the file is : "+ repr(f_extns[-1]))
# repr function returns the printable representation of the given object