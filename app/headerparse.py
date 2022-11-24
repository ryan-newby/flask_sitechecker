class headerParse:
    
    def __init__(self, header_in):
        self.description = "Parse HTTP headers"
        self.header_in = header_in
        self.null_string = "null"

    def parse_sts(self):
        if "strict-transport-security" in self.header_in:
            return self.header_in['strict-transport-security']
        else: 
            return self.null_string
    
    def parse_xcto(self):
        if "x-content-type-options" in self.header_in:
            return self.header_in['x-content-type-options']
        else: 
            return self.null_string

    def parse_xfo(self):
        if "x-frame-options" in self.header_in:
            return self.header_in['x-frame-options']
        else: 
            return self.null_string

    def parse_csp(self):
        if "content-security-policy" in self.header_in:
            return self.header_in['content-security-policy']
        else: 
            return self.null_string