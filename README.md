# API and UI tests
This is a Pet Project.

Due to restrictions(i.e. captcha) I didn't create all possible test cases, so consider
my pet project as example of my knowledge of Python, architecture approaches and libraries in automation testing.
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
#### Linux
```bash
export PYTHONPATH=src:$PYTHONPATH

```
#### Windows
```bash
set PYTHONPATH=src:$PYTHONPATH

```
Run tests

For UI tests you need to have installed chromedriver and Chrome Browser with compatible versions. 
```bash
pytest src/ui/tests -v

```
For API tests you need to make a few preconditions:
1. Execute instruction https://get.exnessaffiliates.help/hc/en-us/articles/360023817591-The-Exness-Partnership-API
2. Create file src/api/tests/secrets.json with your login and password with the structure below

```
{
  "login": "string",
  "password": "string"
}
```
After that you can run tests
```bash
pytest src/api/tests -v

```