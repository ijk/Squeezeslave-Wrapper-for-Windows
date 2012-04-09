#!/usr/bin/python

def maclist():
    """Returns a list of mac addresses strings
    Windows Only
    
    """
    #http://groups.google.com/group/comp.lang.python/msg/fd2e7437d72c1c21
    # code from "HOWTO: Get the MAC Address for an Ethernet Adapter"
    # MS KB ID: Q118623
    import netbios
    mac_list = []
    ncb = netbios.NCB()
    ncb.Command = netbios.NCBENUM
    la_enum = netbios.LANA_ENUM()
    ncb.Buffer = la_enum
    rc = netbios.Netbios(ncb)
    if rc != 0: raise RuntimeError, "Unexpected result %d" % (rc,)
    for i in range(la_enum.length):
        ncb.Reset()
        ncb.Command = netbios.NCBRESET
        ncb.Lana_num = ord(la_enum.lana[i])
        rc = netbios.Netbios(ncb)
        if rc != 0: raise RuntimeError, "Unexpected result %d" %(rc,)
        ncb.Reset()
        ncb.Command = netbios.NCBASTAT
        ncb.Lana_num = ord(la_enum.lana[i])
        ncb.Callname = "*               "
        adapter = netbios.ADAPTER_STATUS()
        ncb.Buffer = adapter
        netbios.Netbios(ncb)
        mac = ""
        for ch in adapter.adapter_address:
            if len(mac) > 0:
                mac += ":"
            #mac += str("%02x" % (ord(ch),) ,)
            mac +=  "%02x" % (ord(ch))
        mac_list.append(mac)
    return mac_list

if __name__ == "__main__":
    for mac in maclist():
        print mac
