## Setup project
```
python setup.py install
```

## Helper commands
```shell
# Read help
python main.py --help
# Set url link
python main.py --url="https://example.com/nlm/xml"  
# Display all errors in list if exists.
python main.py -e --url="https://example.com/nlm/xml"  
# Display number of check nodes.
python main.py -n --url="https://example.com/nlm/xml"  

```
## Install Manually Python Packages From a Requirements File
```
pip install -r requirements/prod.txt
```
## How to Maintain a Python Requirements File
```
pip list --outdated
```