## Two Images Upload at a time
- two images upload at each request
- images update if BlogPost id is given
- WebScokets for API integration

## Installation and Running Project
### Step 1
`git clone https://github.com/phyodev/visit77-code-test.git`

### Step 2
`python -m venv venv`

### Step 3
`cd visit77_code_test`

### Step 4
`pip install -r requirements.txt`

### Step 5
`python manage.py migrate`

### Step 6
`daphne -p 8000 visit77_code_test.asgi:application`

### Step 7
open index.html file under visit77_code_test/blog/templates/blog/ outside of the project and run it on browser
**Note:** this index.html file is just to testing APIs

### Step 5
then wen can test uploading images and updating images