import json
"""
various vim calls that are useful in converting
http://physics.nist.gov/cuu/Constants/Table/allascii.txt to a parsable list.
:%s/    /<tab>/g  -- puts separators between columns
:%s/  //g -- cleans some excess spaces
:%s/<tab>\+/<tab>/g -- replaces multiple tabs with one
:%s/<tab>$//g -- remove tabs at the end of the line
:%s/\([0-9]\) \([0-9]\)/\1\2/g -- remove spaces between numbers
:%s/ \([0-9]\)/\1\2/g -- remove space before numbers
:%s/\([0-9]\) e/\1\2e/g -- 1 e3 -> 1e3
:%s/(exact)/0.0/g
:%s/\.\.\. e/e/g
:%s/<tab> /<tab>/g
:%s/<tab>$//g -- remove tabs at the end of the line (again)
:%s/\.\.\.//gc -- remove spurious
:%s/ /_/g
"""

nist_const = open("NIST_constants_Feb2013_shortened.txt", "r")

nistdict = {}

for columns in ( line_entry.split("\t") for line_entry in nist_const ):
    paramdict = {}

    varname = columns[0]
    value = float(columns[1])
    uncertainty = float(columns[2])

    try:
        units = columns[3].strip()
        units = units.replace("_", " ")
    except:
        units = None

    paramdict["desc"] = varname.replace("_", " ")
    paramdict["value"] = value
    paramdict["uncertainty"] = uncertainty
    paramdict["units"] = units

    nistdict[varname] = paramdict

nist_const.close()

with open("NIST_constants_Feb2013.json", 'wb') as outfile:
    json.dump(nistdict, outfile, sort_keys=True,
               indent=4, separators=(',', ': '))
