class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3 and all(self.isIPv4(i) for i in IP.split('.')):
            return 'IPv4'
        if IP.count(':') == 7 and all(self.isIPv6(i) for i in IP.split(':')):
            return 'IPv6'
        return 'Neither'
        
        
    def isIPv4(self, IP):
        try:
            return str(int(IP)) == IP and 0 <= int(IP) <= 255
        except:
            return False
    
    def isIPv6(self, IP):
        if len(IP) > 4:
            return False
        try:
            return int(IP, 16) >= 0 and IP[0] != '-'
        except:
            return False
        
    
        
        
