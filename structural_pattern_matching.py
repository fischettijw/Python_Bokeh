import os
os.system('cls')

def has_guessed_correctly(command):
    match command:
        case "quit":
            print("quit")
        case "reset":
            print("reset")
        case unknown_command:
            print (f"Unknown command '{unknown_command}")

has_guessed_correctly('hello')