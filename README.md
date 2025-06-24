<h1>Password Manager & Message Encryption Tool</h1>
This Python program is a simple command-line password manager combined with a message encryption/decryption tool. It allows users to securely generate, store, and retrieve passwords as well as encrypt and decrypt messages using custom character mapping.

<h3>Features</h3>

<h3>🔑 Password Generator</h3>
<ul>Generate strong random passwords with a custom number of characters.</ul>
<br>
<h3>🔐 Password Manager</h3>
<ul>Set a master password to secure access.</ul>
<ul>Add new accounts with username and encrypted password.</ul>
<ul>List saved accounts.</ul>
<ul>Retrieve and decrypt passwords for any saved account.</ul>
<ul>All data is saved securely in a JSON file and encrypted using Fernet (AES) and bcrypt hashing.</ul>
<br>
<h3> ✉️ Message Encryption/Decryption</h3>
<ul>Encrypt any text using a shuffled character mapping.</ul>
<ul>Decrypt encrypted messages back to readable text.</ul>
<br>
<h3> ⚠️ Security Note</h3>
<ul>The encryption used for messages is a simple substitution cipher (not recommended for real-world secure communication).</ul>
<ul>Passwords are encrypted using Fernet and protected by a master password with bcrypt hashing.</ul>
