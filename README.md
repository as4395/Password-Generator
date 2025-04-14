# 🔐 Password Generator

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)

This Python script helps you generate secure, customizable passwords and evaluate their strength using entropy and estimated crack time — all using the built-in `secrets` module for cryptographic randomness.

---
## 🛠 Requirements

This script uses only built-in Python libraries:

- `secrets`
- `string`
- `math`
- `sys`

No additional packages are required.

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

<pre>
Enter the desired password length: 12
Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include digits? (yes/no): yes
Include special characters? (yes/no): no

Generated password: rXqWw1ni6G1R
Entropy: 71.45 bits
Strength: Strong (70/100)
Estimated time to crack: 3734105 days, 1 hours, 10 minutes, 39 seconds

Do you want to create another password? (yes/no):
</pre>

---

## 🚀 How to Use

### 1. Clone the Repository

To download the project files, open a terminal and run:

```bash
git clone https://github.com/as4395/password_gen.git
cd password_gen
```

### 2. Run the Script

Ensure you have Python 3 installed on your system. You can check your Python version by running:

```bash
python3 --version
```
If Python 3 is installed, run the script with:
```bash
python3 password_generator.py
```
If your system uses python instead of python3, try:
```bash
python password_generator.py
```

### 3. Follow the Prompts

Once the script is running, it will prompt you to enter:
- The desired password length
- Whether to include uppercase letters
- Whether to include lowercase letters
- Whether to include digits
- Whether to include special characters

Based on your input, the script will:
- Generate a secure password
- Calculate the entropy (in bits)
- Evaluate and print the password strength
- Estimate the time it would take to crack the password using brute force
After displaying the results, the script will ask if you want to generate another password. You can repeat the process or exit.

## 🧠 Tips

- For maximum security, avoid including predictable patterns.
- Disable internet access while running scripts if you're using passwords in secure environments.
- Do not reuse generated passwords — always generate a new one for each use case.




