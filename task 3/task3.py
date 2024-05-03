def main():
    print("Password Generator Application")
    print("=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=")

    try:
        length = int(input("Enter the desired length of the password (minimum 8 characters): "))
        if length < 8:
            raise ValueError("Password length must be at least 8 characters.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Generate and display the password
    password = generate_password(length)
    print("\nGenerated Password:")
    print(f"{password}\n")
    print("Copy the password to your clipboard?")
    print("1. Yes")
    print("2. No")

    try:
        choice = int(input("Enter your choice (1-2): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if choice == 1:
        import pyperclip
        pyperclip.copy(password)
        print("Password copied to clipboard.")
    else:
        print("Password not copied.")

    # Save the generated password to a file
    with open("password.txt", "w") as f:
        f.write(password)

if __name__ == "__main__":
    main()