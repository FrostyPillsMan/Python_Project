while True:
    try:
        with open("./Practise Python/Practise/Error_Exception/data.csv") as file:
            file_read = file.readline()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    else:
        print(f"File read successfuly: {file_read}")
    finally:
        print("The File has been executed well.")
    break

