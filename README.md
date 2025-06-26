<h1>Password Manager & Message Encryption Tool</h1>
This Python program is a simple command-line password manager combined with a message encryption/decryption tool. It allows users to securely generate, store, and retrieve passwords as well as encrypt and decrypt messages using custom character mapping.

<h3>Features</h3>
<h2>🔑 Password Generator</h2>
<li>Generate strong random passwords with a custom number of characters.</li>
<h2>🔐 Password Manager</h2>
<li>Set a master password to secure access.</li>
<li>Add new accounts with username and encrypted password.</li>
<li>List saved accounts.</li>
<li>Retrieve and decrypt passwords for any saved account.</li>
<li>All data is saved securely in a JSON file and encrypted using Fernet (AES) and bcrypt hashing.</li>
<h2> ✉️ Message Encryption/Decryption</h2>
<li>Encrypt any text using a shuffled character mapping.</li>
<li>Decrypt encrypted messages back to readable text.</li>
<br>
 <h2>Requirements</h2>
 <li>Python 3.6+</li>
 <li>cryptography</li>
 <li>bcrypt</li>
<h4>Install dependencies with:</h4>
 <ul><i>pip install cryptography bcrypt<i></i></ul>
<h2>⚠️ Security Note</h2>
<p>
  This project was developed for educational purposes to demonstrate basic concepts of cryptography and secure credential storage. Although it uses valid techniques such as:
</p>

<ul>
  <li><strong>Symmetric encryption via Fernet (based on AES)</strong> to protect stored passwords</li>
  <li><strong>Secure hashing with bcrypt</strong> to protect the master password</li>
  <li><strong>Local storage in an encrypted JSON file</strong></li>
</ul>

<p>
  ⚠️ <strong>It is not recommended for use in production environments or to store real credentials</strong>, as it has not undergone rigorous security audits.
</p>

<p>
  Additionally:
</p>

<ul>
  <li>The <strong>message encryption functionality</strong> uses a simple substitution cipher (not secure for critical or sensitive communication).</li>
  <li>The main focus is educational, making it ideal for studying and understanding information security concepts.</li>
</ul>
