# import mymath
import mymath as ma  # not writing the complete module name
# import the module

#using the module--> module_name.function_in_module(parameters)
print(ma.sum(10,5))
print(ma.diff(10,5))


# not writing the modulename.fun.... everytime use from module import function
# * instead of function name to import all functions in the module
from mymath import *
# import the module

#using the module--> module_name.function_in_module(parameters)
print(sum(10,5))
print(diff(10,5))
