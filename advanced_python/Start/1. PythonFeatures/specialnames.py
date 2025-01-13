# Example file for Advanced Python by Joe Marini
# Using special module names
import collections


# __name__ is the name of the module
print("Module name: ", __name__)

# __file__ contains the path to the file from which the module was loaded
print("\nFile name: ", __file__)

# __package__ indicates the package that the module belongs to.
print("\nPackage name: ", __package__)
print(collections.__package__)

if __name__ == "__main__":
    print("This code is being run directly.")