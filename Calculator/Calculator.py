def calculator():
    while True:
        try:
            expression_value = input("\nEnter the expressions(values) given: ")
            if expression_value.lower() in ["q" or "quit"]:
                exit()
            else:
                exp_result = eval(expression_value)
                print("Result:", exp_result)
                break
        except Exception as err:
            print("Error:", err)
            print(
                "1. Press (q/quit()) to exit the game for prompted wrongly.\n"
                "2. Type right expressions to continue."
            )
        finally:
            print("Goodbye!")


calculator()
