import json

class Request:
    version = "0.01"
    outLang = None
    reqId = None
    fio = ""
    index = ""
    woFlat = False
    useStructure = False
    useRegionPostOffice = False
    compliance = False
    addr = []
    historical = ""
    origin = ""

    def __dict__(self):
        d = {
            'version': self.version,
            'outLang': self.outLang,
            'reqId': self.reqId,
            'fio': self.fio,
            'index': self.index,
            'woFlat': self.woFlat,
            'useStructure': self.useStructure,
            'useRegionPostOffice': self.useRegionPostOffice,
            'compliance': self.compliance,
            'historical': self.historical,
            'origin': self.origin,
            'addr': [],
        }
        for ad in self.addr:
            d.append(dict(ad))
        return d


    def get_json(self):
        return json.dumps(dict(self))


    def add_addres(self, addr):
        self.append(addr)