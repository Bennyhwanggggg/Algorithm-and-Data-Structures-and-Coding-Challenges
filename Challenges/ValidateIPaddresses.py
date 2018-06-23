def validIPAddress(self, IP):
    """
    :type IP: str
    :rtype: str
    """
    m = re.match('([0-9a-fA-F][0-9a-fA-F]{0,3}:){7}([0-9a-fA-F][0-9a-fA-F]{0,3}){1}', IP)

    if m:
        return 'IPv6' if m.group() == IP else 'Neither'

    # ipv4
    groups = IP.split('.')

    if len(groups) != 4:
        return 'Neither'

    # validate no leading zeros and numbers
    for group in groups:
        try:
            if len(group) > 3:
                return 'Neither'
            if len(group) > 1 and int(group[0]) == 0:
                return 'Neither'
            if int(group) > 255 or int(group) < 0:
                return 'Neither'
        except:
            return 'Neither'

    return 'IPv4'