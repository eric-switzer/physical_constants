Physical constants in JSON/python

Available constants:
====================
* `NIST_constants_Feb2013.json`: full set of CODATA, mks units
* `NIST_constants_Feb2013_cgs.json`: a reduced version of the above in cgs units

Model:
======
* Several groups of constants can be combined into a common library that functions use
* Tasks with loading/saving/combining of groups are managed by a class
* This class can emit a python dictionary of just the constants (leaving out descriptions and units) that is fast to use in functions.
* Functions can derive new constants based on fundamental ones and save these in the same structure
* For a particular code, one can combine and then save a useful set of constants/paramters.
