import physical_constants

param_root = "https://raw.github.com/eric-switzer/physical_constants/master/"
const_lib = physical_constants.PhysicalConstants()

#const_lib.load(param_root + "NIST_constants_Feb2013_cgs.json")
const_lib.load("NIST_constants_Feb2013_cgs.json")
const_lib.load("astrophysical.json")
const_lib.add_const("one", 1.)
const_lib.save("combined_constants.json")

const_dict = const_lib.emit()

print const_dict['Newtonian_constant_of_gravitation']
print const_dict['critical_density_g_cm']
print const_dict["one"]
