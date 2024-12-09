# 🧾 Custom DNS Server

A lightweight custom DNS server built using Python and the `dnslib` library. This server listens for DNS queries and responds based on predefined records.

## 📜 Features

- **UDP-based DNS server** listening on a specified port (default: `8053`).
- Handles multiple DNS query types (e.g., `A`, `AAAA`, `MX`).
- Customizable DNS records through a `dns_records.py` module.
- Easy-to-extend for additional DNS functionalities.

## 🛠️ Prerequisites

- Python 3.x
- `dnslib` library

### Install `dnslib`

```bash
pip install dnslib
```

## 📄 Project Structure

```
dns-server/
│-- dns_server.py      # Main DNS server script
│-- dns_records.py     # Custom DNS records
└-- README.md          # Documentation
```

## 🗂️ Custom DNS Records (`dns_records.py`)

Create a `dns_records.py` file to define your custom DNS records. Example:

```python
from dnslib import RR, A, AAAA, MX

DNS_DATA = {
    'example.com.': [
        RR('example.com.', rtype='A', rdata=A('127.0.0.1')),
        RR('example.com.', rtype='AAAA', rdata=AAAA('::1'))
    ],
    'mail.example.com.': [
        RR('mail.example.com.', rtype='MX', rdata=MX('mail.example.com.'))
    ],
    'test.com.': [
        RR('test.com.', rtype='A', rdata=A('192.168.1.1'))
    ]
}
```

## 🚀 How to Run

1. **Start the Server**:

   ```bash
   python main.py
   ```

   The server will listen on `0.0.0.0:8053` by default.

2. **Test the Server** using `dig`:

   ```bash
   dig @localhost -p 8053 example.com
   ```

## 📝 Code Overview

### `main.py`

This script contains:

- **`handle_query(data)`**: Handles incoming DNS queries and prepares the response.
- **`run_server()`**: Starts the UDP server to listen for DNS requests.

## 🧪 Example Output

When a query is received, you'll see output like:

```
DNS server listening on 0.0.0.0:8053...
Received request from ('127.0.0.1', 45678)
Received query: example.com. (A)
```

## 🛑 Stopping the Server

Press `Ctrl+C` to stop the server gracefully.

## 📝 License

This project is licensed under the MIT License.

---

## 📬 Contact

For any questions or suggestions, feel free to reach out:

**Email:** [thesomen123@gmail.com](mailto:thesomen123@gmail.com)

---

This `README.md` helps explain how to set up and use the DNS server, including your custom `dns_records.py`.
