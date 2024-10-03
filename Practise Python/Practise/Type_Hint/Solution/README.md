
# Problem
1. Expected 0 positional arguments

2. Creating Player Instances
    ```
    python
        [
            Player = Football("Player1", "Player2")
        ]
    ```

**Explanation** - It will raise an error because the constructor only accepts one argument (player).

3. Cannot access attribute "player1" for class "Team"
  Attribute "player1" is unknown 

  ```python
        [
            print(Machester_United.player1)
        ]

  ```

# Solution
1. Constructor method defined as **__init__** instead of **init.**

2. Create multiple players by separating instances for each player.
```python
    [
        player1 = Football("Player1")
        player2 = Football("Player2")
    ]
```

3. Accessing Specific Players

```python
    [
        print(Machester_United[0].player)  # Accesses the first player
        print(Machester_United[1].player)  # Accesses the second player
    ]

```

