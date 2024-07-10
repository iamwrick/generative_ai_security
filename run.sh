#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Generate SSL certificates
openssl req -new -x509 -days 365 -nodes -out certs/cert.pem -keyout certs/key.pem <<EOF
US
California
San Francisco
MyOrganization
MyUnit
localhost
myemail@example.com
EOF

# Run AES Encryption and Visualization
python src/visualize_aes.py

# Run TLS Communication Server
python src/tls_communication_server.py &
SERVER_PID=$!

# Run TLS Communication Client
python src/tls_communication_client.py

# Kill the server process
kill $SERVER_PID

# Visualize TLS Communication Flow
python src/visualize_tls.py
