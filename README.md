<h1>Password Manager & Message Encryption Tool</h1>
This Python program is a simple command-line password manager combined with a message encryption/decryption tool. It allows users to securely generate, store, and retrieve passwords as well as encrypt and decrypt messages using custom character mapping.

<h3>Features</h3>

<h3>🔑 Password Generator</h3>
<li>Generate strong random passwords with a custom number of characters.</li>
<br>
<h3>🔐 Password Manager</h3>
<li>Set a master password to secure access.</li>
<li>Add new accounts with username and encrypted password.</li>
<li>List saved accounts.</li>
<li>Retrieve and decrypt passwords for any saved account.</li>
<li>All data is saved securely in a JSON file and encrypted using Fernet (AES) and bcrypt hashing.</li>
<br>
<h3> ✉️ Message Encryption/Decryption</h3>
<li>Encrypt any text using a shuffled character mapping.</li>
<li>Decrypt encrypted messages back to readable text.</li>
<br>
 <h3>Requirements</h3>
 <li>Python 3.6+</li>
 <li>cryptography</li>
 <li>bcrypt</li>
 <br>
<h4>Install dependencies with:</h4>
 <ul>pip install cryptography bcrypt</ul>
<br>
<h2> ⚠️ Security Note</h2>
<li>The encryption used for messages is a simple substitution cipher (not recommended for real-world secure communication).</li>
<li>Passwords are encrypted using Fernet and protected by a master password with bcrypt hashing.</li>
