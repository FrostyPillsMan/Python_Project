
# Socket Programming🔌⌨️

## Problem
('client.py')
ConnectionRefusedError: [WinError 10061] No connection could be made because the target machine actively refused it

## Solution
1. Deactive the Firewall Rules through ***Windows Security*** through ***Privacy & Security*** 
2. Run the cmd terminal with two screens('client.py') && ('server.py')
3. Run 'server.py' once to start the server and run 'client.py' as many as you want to see the results...

## Results
```python
[STARTING] server is starting...
[LISTENING] Server is listening on 192.168.0.161
[NEW CONNECTION] ('192.168.0.161', 49290) connected.
[ACTIVE CONNECTIONS] 1
[('192.168.0.161', 49290)] Hello Server!
[NEW CONNECTION] ('192.168.0.161', 49344) connected.
[ACTIVE CONNECTIONS] 2
[('192.168.0.161', 49344)] Hello Server!
[('192.168.0.161', 49344)] Testing the Server!
[('192.168.0.161', 49344)] Server Running Successfully!
[NEW CONNECTION] ('192.168.0.161', 49432) connected.
[ACTIVE CONNECTIONS] 3
[('192.168.0.161', 49556)] Hello Server!
[('192.168.0.161', 49556)] Testing the Server!
[('192.168.0.161', 49556)] Server Running Successfully!
[('192.168.0.161', 49556)] !DISCONNECT
```

