# 🔐 Secure Password Generator

This Python script helps you generate secure, customizable passwords and evaluate their strength using entropy and estimated crack time — all using the built-in `secrets` module for cryptographic randomness.

---

## 🧰 Features

- Generate strong, random passwords
- Customize:
  - Password length
  - Inclusion of uppercase letters, lowercase letters, digits, and special characters
- Ensure at least one character from each selected category
- Calculate entropy (in bits) based on character pool and length
- Assess password strength based on entropy score
- Estimate how long it would take to brute-force the password

---

## 📸 Example Output

<pre> Enter the desired password length: 12 Include uppercase letters? (yes/no): yes Include lowercase letters? (yes/no): yes Include digits? (yes/no): yes Include special characters? (yes/no): no Generated password: rXqWw1ni6G1R Entropy: 71.45 bits Strength: Strong (70/100) Estimated time to crack: 3734105 days, 1 hours, 10 minutes, 39 seconds Do you want to create another password? (yes/no): </pre>
