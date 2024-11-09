# Corrosion
Simple backend application for managing corrosion's offers.

# Install
#### Clone the repo
   `git clone git@github.com:davidalsh/corrosion.git`
# Run

### With Docker
1. `docker build -t corrosion . && docker run -p 8000:8000 -d corrosion`

### Without Docker
1. `pip3 install -r requirements.py` or using pipenv `pipenv install`
2. `python3 manage.py runserver`

# To be continued
### Implementation
1. add ability to manage offers through API.
2. add price calculation.
3. add generation for every possible variant of product.
4. add unit tests.
5. think about custom CMS (not built in django admin)
6. deploy

# Notes
*Project has SQLite DB, which already contain all needed records for testing (so just start the project)
Use django admin panel to manage Corrosion's products.*
### admin creds:
   username: `admin`\
   password: `adminadmin`
