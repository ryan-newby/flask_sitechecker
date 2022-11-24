import requests
import dns.resolver


class httpStatus:
    
    def __init__(self):
        self.description = "HTTP Status Code"
            
    def try_dns(dns_in):
        ip_result = []
        try:
            result = dns.resolver.resolve(dns_in, 'A')
            for ipval in result:
                ip_result.append(str(ipval))
            if ip_result[0] == '127.0.0.1':
                return "Unable to resolve address"
            else:
                return ip_result[0]
        except dns.resolver.NXDOMAIN:
            return "No such domain"
        except dns.resolver.Timeout:
            return "Timed out while resolving"
        except dns.exception.DNSException:
            return "Unhandled exception"

    def http_response(url_in):
        http_rlist = []
        try:
            response = requests.get(url_in)
            http_rlist.append(response.status_code)
            http_rlist.append(response.reason)
            http_rlist.append(response.headers)
            return http_rlist
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            raise SystemExit(e)

  


        
