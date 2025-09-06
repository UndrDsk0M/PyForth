# PyForth

###  A Pythonic compiler for the Forth+ programming language 
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&style=for-the-badge&labelColor=181717&color=purple)](https://github.com/UndrDsk0M/PyForth)
[![License](https://img.shields.io/badge/License-MIT-181717?logo=mit&style=for-the-badge&labelColor=181717&color=orange)](LICENSE.md)

<img width="1183" height="382" alt="2025-09-06_16-39" src="https://github.com/user-attachments/assets/1205c3bf-dfaa-425b-b181-7783ecc74dcb" />

## Overview

PyForth is a minimalistic, Python-based compiler/interpreter for the Forth+ language. It aims to provide a straightforward and readable implementation while staying faithful to the Forth philosophy.
Furthermore i added some python method as sort, reverse and the True is set to 1 instead of -1 
## Features

+ Written in pure Python (with a sample forth script )
+ Supports both file execution and an interactive REPL
+ Lightweight design—easy to understand and extend
+ Includes a sample Forth script (test.fs) for quick testing 
GitHub
+ supports by ForthRights in vscode extention store
+ it will can connect to python libraries easier
+ modern forth while keeping old options 

# Getting Started
### Prerequisites
+ Python 3.x installed on your system.
+ (Optional but recommended) A virtual environment to manage dependencies.

### Installation
Clone the repository:

```
git clone https://github.com/UndrDsk0M/PyForth.git
cd PyForth
```
### Running the Interpreter
You can run PyForth with a Forth source file:
```
python pyforth.py test.fs
```

Or start an interactive REPL session:
```
python pyforth.py
# Then enter Forth code directly, e.g.:
1 2 + .
Stack<>  ok
```
Adjust accordingly based on your implementation details.

### Example

Here’s a simple example of Forth code execution (assuming REPL-like behavior):
```
5 3 * .  \ This will output 15
```
## Project Structure
```
PyForth/
├── pyforth.py    # Main Python moudle for the Forth interpreter
└── test.fs       # Sample Forth script with a error
```
### Contributing

Contributions are welcome! Consider:
+ Adding new Forth words or operations
+ Improving performance or readability
+ Enhancing the test suite and coverage
+ suggeting new options or words in my [Telegram](https://t.me/UndrDsk0M)!


Please:

1. Fork the repository.
2. Create a feature branch (git checkout -b feature/awesome).
3. Commit your changes (git commit -am "Add awesome feature").
4. Push to the branch (git push origin feature/awesome).
5. Open a Pull Request for review.
or just <b>give a star the Project :)</b>


### License
This project is licensed under the MIT License


Acknowledgments

+ Developed by UndrDsk0M
+ Inspired by the elegance and extensibility of Forth and Python
<img width="1000" height="500" alt="2025-09-06_16-37" src="https://github.com/user-attachments/assets/0d019413-e140-42e5-bdc0-cf8ab75247d2" />



# Next Steps
+ Compliting the if-else conditions, for, begin-until loops, and defining a word section. it also needs a float and string data type.
+ inlcude word to include both forth and python file and modules 
+ If you'd like help refining any section, feel free to share more specifics, I’d be happy to assist!
