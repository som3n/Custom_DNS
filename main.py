from dnslib import DNSRecord, QTYPE  # For handling DNS queries and record types
import socket  # For network communication
from dns_records import DNS_DATA  # Import DNS data records

# DNS server configuration
HOST, PORT = '0.0.0.0', 8053

# Handle incoming DNS queries
def handle_query(data):
    request = DNSRecord.parse(data)
    print(f'Received query: {request.q.qname} ({QTYPE[request.q.qtype]})')

    reply = request.reply()
    qname = str(request.q.qname)
    qtype = request.q.qtype

    if qname in DNS_DATA:
        for record in DNS_DATA[qname]:
            if record.rtype == qtype or qtype == QTYPE.ANY:
                reply.add_answer(record)
    else:
        print(f"No records found for {qname}")

    return reply.pack()

# Run the DNS server
def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((HOST, PORT))
        print(f"DNS server listening on {HOST}:{PORT}...")

        while True:
            data, addr = sock.recvfrom(512)
            print(f"Received request from {addr}")
            try:
                response = handle_query(data)
                sock.sendto(response, addr)
            except Exception as e:
                print(f"Error handling request: {e}")

if __name__ == '__main__':
    try:
        run_server()
    except KeyboardInterrupt:
        print("\nServer stopped.")
