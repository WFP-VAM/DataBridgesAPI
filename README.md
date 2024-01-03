# DataBridgesAPI
Scripts and applications for testing DataBridges API from the API Gateway

# Getting started
## How to install
You can use pip to install the package:
```
pip install databridgesapi@git+https://github.com/WFP-VAM/DataBridgesAPI
```

If developing the package, use this command from the repo root for a local and editable installation:

```
pip install -e .
```

## Handling credentials
Create an .env file to be placed in the root directory of your project looking like:

```
MY_KEY='placeHereYourAPIKey'  
MY_SECRET='placeHereYourAPISecret'  
```
## Running the code
See the examples folder to see how to use the DataBridgesAPI library

# How to contribute
Your contribution is more than welcome...but we ask you to follow some rules:
- Work on a branch and submit your code for review
- Try to write general code, avoiding hard-coded values
- Use [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
- Document your code using Google Docstrings and [type hinting](https://docs.python.org/3/library/typing.html)
- Follow [PEP8 reccomendations](https://www.python.org/dev/peps/pep-0008/)
- After implementing something, test it (using pytest)!
- Use issues to track your code.
- **DO NOT COMMIT** sensitive files
