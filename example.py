import jsondict

param_root = "https://raw.github.com/eric-switzer/physical_constants/master/"

constants_http = jsondict.load_json_over_http_file(param_root +
                                            "NIST_constants_Feb2013_cgs.json")

constants = jsondict.load_json("NIST_constants_Feb2013_cgs.json")

print constants['Newtonian_constant_of_gravitation']
print constants_http['Newtonian_constant_of_gravitation']
