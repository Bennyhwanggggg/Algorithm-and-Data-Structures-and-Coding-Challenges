class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            local = local.split('+')[0]
            seen.add('{}@{}'.format(local, domain))
        
        return len(seen)
                
