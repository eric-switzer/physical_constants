try:
    import simplejson as json
except ImportError:
    import json
import jsondict


class PhysicalConstants:
    """A simple manager of physical constant data

    Each constant is a key in master_db, and its value is another dictionary
    with keys:
    * units: a string giving the units of the constant
    * value, uncertainty: a float
    * desc: a description string
    """

    def __init__(self):
        self.master_db = {}

    def load(self, locator):
        """concatenate a configuration -> master_db"""

        if ("http://" in locator) or ("https://" in locator):
            print "opening url: ", locator
            new_consts = jsondict.load_json_over_http_file(locator)
        else:
            print "opening file: ", locator
            new_consts = jsondict.load_json(locator)

        for name, const_info in new_consts.iteritems():
            if name in self.master_db:
                print "WARNING: overwriting entry for: ", name

            self.master_db[name] = const_info

    def save(self, filename):
        """save master_db to a json file"""

        with open(filename, 'wb') as outfile:
            json.dump(self.master_db, outfile, sort_keys=True,
                      indent=4, separators=(',', ': '))

    def add_const(self, name, value,
                  uncertainty=None, desc=None, units=None):

        entry = {}
        entry['value'] = value
        entry['uncertainty'] = uncertainty
        entry['desc'] = desc
        entry['units'] = units

        print "adding name, entry: ", name, entry
        if name in self.master_db:
                print "WARNING: overwriting entry for: ", name

        self.master_db[name] = entry

    def emit(self, field="value"):
        const_dict = {}
        for name, const_info in self.master_db.iteritems():
            const_dict[name] = const_info[field]

        return const_dict

#-----------------------------------------------------------------------------
# use the library to build a local constants library
param_root = "https://raw.github.com/eric-switzer/physical_constants/master/"
def generate_local():
    print "Generating physical constant database"
    build_lib = PhysicalConstants()
    build_lib.load(param_root + "NIST_constants_Feb2013_cgs.json")
    build_lib.load(param_root + "astrophysical.json")
    build_lib.add_const("one", 1.)
    build_lib.save("combined_constants.json")

const_lib = PhysicalConstants()

# try to load the local constant database, if unavailable, build a new one
try:
    const_lib.load("combined_constants.json")
except IOError:
    generate_local()
    const_lib.load("combined_constants.json")

const_dict = const_lib.emit()
desc = const_lib.emit("desc")

# register these constants
for varname, varvalue in const_dict.iteritems():
    vars()[varname] = varvalue

if __name__=="__main__":
    generate_local()
