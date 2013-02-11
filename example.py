import physical_constants
"""This is an example for using the constant library
One option is to use the dictionary of constants in later code.
Another option is to let the dictionary define variables in the module. This
module can be imported and used in other code.
"""
import physical_constants as pc

print pc.parsec_cm
print pc.desc["parsec_cm"]
