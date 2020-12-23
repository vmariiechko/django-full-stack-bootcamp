import mymodule
print("1) ", end='')
mymodule.func_in_module()

import mymodule as mm
print("2) ", end='')
mm.func_in_module()

from mymodule import func_in_module
print("3) ", end='')
func_in_module()

from mymodule import *
print("4) ", end='')
func_in_module()
