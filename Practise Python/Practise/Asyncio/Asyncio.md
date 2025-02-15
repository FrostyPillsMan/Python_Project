
# Asyncio

## Sample
--> "Simple chat server and client application"

1. test2.py
```python
    [
        # Server -- listen for incoming connections on a specified address and port, using 'handle_client' function as a callback.
        Serving on ('::1', 12345, 0, 0)
        New connection from ('::1', 50486, 0, 0)
        Received message from ('::1', 50486, 0, 0): Hello
        Server stopped.
    ]
```

2. test3.py
```python
    [
        # The client establishes connection to the chat server and launches two tasks: 
        # 1. one for sending messages (handled by send_message()) 
        # 2. and another for receiving messages (handled by receive_message()).
        Enter message: Hello
        Enter message: Receive
        Enter message: Really
        Enter message: Wow
        Enter message: Amazing
        Enter message: kinko
        Enter message: Chao
        Enter message: Khong Sao
    ]
```
---
**Advanced asyncio techniques**

1. ***Future objects*** - test4.py
2. ***Timeouts and cancellation*** - test5.py
3. ***Exception handling*** - test6.py

## Reference
1. https://docs.python.org/3/library/asyncio-stream.html