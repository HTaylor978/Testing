class FileHandler:
    def __init__(self,filename, props):
        self._filename = filename
        self._props = props

    def save_dictlist(self,list_of_dictionaries):
        with open(self._filename,mode='w') as fileobject:
            for d in list_of_dictionaries:
                s = ','.join(d.values())
                fileobject.write(s)

    def load_dictlist(self):
        result = []
        with open(self._filename, mode='r') as fileobject:
            for line in fileobject.readlines():
                result.append( zip(self._props, line.split(',')) )
        return result
