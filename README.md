# Web Traffic Transformation

## Objective

Write a python script/program to transform web traffic data stored in time-record format where
each row is a page view into a per-user format where each row is a different user and the
columns represent the time spent on each of the pages.

# How To

## Usage
Run the script from the command line as follows
```bash
python main.py
```

## Requirements
To install the necessary requirements, it's recommended to create a virtualenv

**!! Project uses Python 3.8+ !!**

### Virtual Env + Requirements
#### Unix / MacOS
```bash
#!/bin/bash

# Create virtual env and activate
python3 -m venv env
source env/bin/activate

# install what we need
pip install -r requirements.txt
```
#### Windows (Powershell)
```powershell
# Make sure powershell is allowed to execute scripts
$scope = Get-ExecutionPolicy
if ([string]$scope = "RemoteSigned") {
    "All is good."
} else {
    try {
        Set-ExecutionPolicy RemoteSigned
        Get-ExecutionPolicy
    } catch {
        Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
        Get-ExecutionPolicy
    }
}

# Create the virtual env
python -m venv winenv

# activate it
.\winenv\Scripts\activate

# install what we need
pip install -r requirements.txt
```

## Unit Tests

Unit tests use pytest. To run, do the following (assuming you've pip installed pytest)
```bash
# cd to the tests directory first to avoid path issues for test files
cd tests
# using `verbose` flag because it's pretty :)
pytest --verbose .
```