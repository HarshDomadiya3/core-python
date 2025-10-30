# from cryptography.fernet import Fernet
# import os
# import csv
#
# KEY_FILE = "key.key"
# DATA_FILE = "passwords.csv"
#
# # Generate key if not exists
# if not os.path.exists(KEY_FILE):
#     key = Fernet.generate_key()
#     with open(KEY_FILE, "wb") as f:
#         f.write(key)
# else:
#     with open(KEY_FILE, "rb") as f:
#         key = f.read()
#
# fernet = Fernet(key)
#
# # Ensure CSV file exists
# if not os.path.exists(DATA_FILE):
#     with open(DATA_FILE, "w", newline="") as f:
#         writer = csv.writer(f)
#         writer.writerow(["Username", "Password"])
#
# # Add new credential
# def add_credential():
#     username = input("Enter username: ").strip()
#     password = input("Enter password: ").strip()
#
#     encrypted_password = fernet.encrypt(password.encode()).decode()
#
#     with open(DATA_FILE, "a", newline="") as f:
#         writer = csv.writer(f)
#         writer.writerow([username, encrypted_password])
#
#     print("Credential saved securely!")
#
# # View credentials
# def view_credentials():
#     with open(DATA_FILE, "r") as f:
#         reader = csv.reader(f)
#         credentials = list(reader)
#
#     if len(credentials) <= 1:
#         print("No credentials stored.")
#         return
#
#     print("\n--- Stored Credentials ---")
#     for i, row in enumerate(credentials[1:], 1):
#         decrypted_password = fernet.decrypt(row[1].encode()).decode()
#         print(f"{i}. Username: {row[0]}, Password: {decrypted_password}")
#     print("--------------------------")
#
# # Main menu
# def main():
#     while True:
#         print("\n--- PASSWORD MANAGER ---")
#         print("1. Add Credential")
#         print("2. View Credentials")
#         print("3. Exit")
#
#         choice = input("Choose: ").strip()
#
#         if choice == "1":
#             add_credential()
#         elif choice == "2":
#             view_credentials()
#         elif choice == "3":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Try again.")
#
# if __name__ == "__main__":
#     main()
