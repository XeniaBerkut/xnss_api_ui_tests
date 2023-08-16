# exness
Pet Project.

Due to restrictions(i.e. captcha) I've not written test cases for successful registration.
## Run the project
How to build and run the project

Ensure you have Git and Python3 installed
 
Clone the project 
```bash
git https://github.com/XeniaBerkut/exness.git
```
Go to the directory
```bash
cd exness/
```
### Run the project via installing environment and requirements

Create virtual python environment
```bash
virtualenv venv
```
Activate virtual python environment
```bash
source venv/bin/activate
```
Install all the requirements
```bash
pip install -r requirements.txt
```
Export Python path
```bash
export PYTHONPATH=src:$PYTHONPATH

```
Run test
```bash
pytest src/ui/tests

```