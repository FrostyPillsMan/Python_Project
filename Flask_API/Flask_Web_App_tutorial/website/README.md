
# TroubleShoot🆘

## Problem
1. No parameter named ***"app"***
2. ValueError: Invalid hash method ***'sha256'.***
3. TypeError: ***'firstName'*** is an invalid keyword argument for User



## Solution
1. wrapped the call to create_database() within a with app.app_context():, allowing it to access the configuration and other resources associated with your Flask app.

Exp:
```python
    [
        with app.app_context():  # Ensure we are within the app context
        create_database(app)

        return app
    ]
```
---
2. Remove ***method="sha256"*** as generate_password_hash is part of the module method function.

3. Change the FirstName variables from `auth.py` and refer to `models.py`.

