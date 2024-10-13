
# Flask API⚗️🔥

## Problem
1. Raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=5000): Max retries exceeded with url: /Hi%20flask!!@@ (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x0000015AE0451BB0>: Failed to establish a new connection: [WinError 10061] No connection could be made because the target machine actively refused it'))

2. LookupError: the converter ***test*** does not exist or TypeError: LearnFlask.get() got an unexpected keyword argument ***age***

3. **Error: 404, Response: <!doctype html>**
```html
[
    <html lang=en>
    <title>404 Not Found</title>
    <h1>Not Found</h1>
    <p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
]
```

4. **Additional character index added to the Post Message.**
```python
[
    {'message': "Hello (), you are {'name': 'Adam', 'age': 21} years old!"}
]
```

5. **Running `test.py` in the command prompt, not receiving an response towards from it.**
```bash
[   
    CMD -- test.py
    C:\Users\User\Desktop\Python\Python_Project\Flask_API>python test.py
    |
]
```

6. Argument of type "Literal['Music is not valid...']" cannot be assigned to parameter "code" of type "int | Response" in function "abort"
  Type "Literal['Music is not valid...']" is not assignable to type "int | Response"
    "Literal['Music is not valid...']" is not assignable to "int"
    "Literal['Music is not valid...']" is not assignable to "Response"

7. raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

8. return f"Music(name = {name}, views = {views}, likes = {likes})"

9. No parameter named "music_id"
   No parameter named "name"

10. sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: music_model

11. music_entry = MusicModel(music_id=music_playlist, name=args['id']) # type: ignore
    KeyError: 'id'

12. {'message': "Did not attempt to load JSON data because the request Content-Type was not 'application/json'."}
Error: 415, Response: {
    "message": "Did not attempt to load JSON data because the request Content-Type was not 'application/json'."
}

## Solution
1. Run the cmd terminal with two screens 'Flask_API.py' && 'test.py', execute 'Flask_API.py' once to begin the server and run 'test.py' as many as you want to see the results...

2. Insert data type inside the key input instead of arguments

3. **Missing separator (like a slash /) between the base path and the parameters**
```python
[
    api.add_resource(LearnFlask, "/Hi flask!!@@/<string:name>/<int:test>")
]
```

4. **Post Message expectation**
```python
    [
        {'message': 'Hello Adam, you are 21 years old!'}
    ]
```

5. **Add print statement after each request to help debug and wait for responses**

6. **Specify a valid HTTP status code when calling `abort`.**
```python
[
    def abort_if_music_playlist_not_exist(music_playlist):
    if music_playlist not in music_disk:
        abort(404, description="Music playlist not found.")
]
```

7. **Remove .json under requests.Delete method**

8. **Add self parameter for each attributes**

9. **Type: ignore Warning**

10. **Application Context**
```python
[
    with app.app_context():
    db.create_all()
    # Creating database tables within an application context
]
```

11. **Check Argument Names**
```python
[
    music_entry = MusicModel(
        music_id=music_playlist,
        name=args['name'],
        views=args['views'],
        likes=args['likes']
    )
]
``` 

12. **Sending the correct Content-Type header in your PATCH request.**
```python
[
    # Define the payload
    payload_2 = {"views": 99}

    # Send the PATCH request with the correct headers
    response = requests.patch(URL_BASE + "music/2", json=payload_2, headers={"Content-Type": "application/json"})
]
```

## Results
1. **Server Client-Side**
```python
[
    * Serving Flask app 'Flask_API'
    * Debug mode: on
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5001
    Press CTRL+C to quit
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 601-289-737
]
```

1. **Testing-Side**
```python
[
    {'name': 'Adam', 'test': 21}
]
```

## Notes
1. Every time returning some type of information from our API, we need to make sure that information is ***serializable.***

