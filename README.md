# Web Traffic Transformation

## Objective

Write a python script/program to transform web traffic data stored in time-record format where
each row is a page view into a per-user format where each row is a different user and the
columns represent the time spent on each of the pages.

## unit tests

Unit tests use pytest. To run, do the following (assuming you've pip installed pytest)
```bash
pytest tests/
```

## requirements.txt
```
atomicwrites==1.4.0
attrs==21.2.0
colorama==0.4.4
iniconfig==1.1.1
numpy==1.21.4
packaging==21.2
pandas==1.3.4
pluggy==1.0.0
py==1.11.0
pyparsing==2.4.7
pytest==6.2.5
python-dateutil==2.8.2
pytz==2021.3
PyYAML==6.0
six==1.16.0
toml==0.10.2
```