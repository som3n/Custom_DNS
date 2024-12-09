from dnslib import RR, QTYPE, A, AAAA, CNAME, MX, TXT, NS, PTR, SRV, SOA, CAA 

DNS_DATA = {
    'test.com.': [
        RR('test.com.', QTYPE.A, rdata=A('93.184.216.34')),
        RR('test.com.', QTYPE.AAAA, rdata=AAAA('2606:2800:220:1:248:1893:25c8:1946')),
        RR('test.com.', QTYPE.CNAME, rdata=CNAME('alias.test.com.')),
        RR('test.com.', QTYPE.MX, rdata=MX('mail.test.com.', preference=10)),
        RR('test.com.', QTYPE.TXT, rdata=TXT('v=spf1 include:_spf.test.com ~all')),
        RR('test.com.', QTYPE.NS, rdata=NS('ns1.test.com.')),
        RR('34.216.184.93.in-addr.arpa.', QTYPE.PTR, rdata=PTR('test.com.')),
        RR('_sip._tcp.test.com.', QTYPE.SRV, rdata=SRV(10, 5, 5060, 'sipserver.test.com.')),
        RR('test.com.', QTYPE.SOA, rdata=SOA(mname='ns1.test.com.', rname='hostmaster.test.com.', times=(2024042701, 3600, 1800, 1209600, 3600))),
        RR('test.com.', QTYPE.CAA, rdata=CAA(0, 'issue', 'letsencrypt.org'))
    ],
    'google.com.': [
        RR('google.com.', QTYPE.A, rdata=A('142.250.190.14')),
        RR('google.com.', QTYPE.AAAA, rdata=AAAA('2607:f8b0:4004:c09::8b')),
        RR('google.com.', QTYPE.MX, rdata=MX('aspmx.l.google.com.', preference=1)),
        RR('google.com.', QTYPE.MX, rdata=MX('alt1.aspmx.l.google.com.', preference=5)),
        RR('google.com.', QTYPE.TXT, rdata=TXT('v=spf1 include:_spf.google.com ~all')),
        RR('google.com.', QTYPE.NS, rdata=NS('ns1.google.com.')),
        RR('google.com.', QTYPE.NS, rdata=NS('ns2.google.com.')),
        RR('google.com.', QTYPE.NS, rdata=NS('ns3.google.com.')),
        RR('google.com.', QTYPE.NS, rdata=NS('ns4.google.com.')),
        RR('google.com.', QTYPE.CAA, rdata=CAA(0, 'issue', 'pki.goog'))
    ]
}
