class Staff:
    ''' This class describes the staff model '''

    def __init__(self, staffname):
        self.staffname = staffname

    def retrieve_manifest(self, manifest):
        """ retirve passenger manifest"""
        for name, route in manifest:
            print("%s is going to %s" % name, route)


