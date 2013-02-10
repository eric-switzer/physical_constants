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
            new_consts = jsondict.load_json_over_http_file(locator)
        else:
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

    def emit(self):
        const_dict = {}
        for name, const_info in self.master_db.iteritems():
            const_dict[name] = const_info["value"]

        return const_dict
