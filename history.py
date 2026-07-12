from datetime import datetime
import hashlib
import os

HISTORY_FILE = "history.txt"
  
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_history(password, score, strength): 

    hashed = hash_password(password)

    with open(HISTORY_FILE, "a") as file:
        file.write(
            f"{datetime.now()} | "
            f"SHA-256: {hashed} | "
            f"{score}/10 | "
            f"{strength}\n"
        )

def view_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            content = file.read()

            if content:
                print("\n===== History =====")
                print(content)
            else:
                print("History is empty.")

    except FileNotFoundError:
        print("No history found.")