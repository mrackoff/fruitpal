# fruitpal
$ clone the repository
# install virtual directory
$ py -3 -m venv venv
$ venv\Scripts\activate.bat
# install app
$ pip install -e .
# setup flask and run
$ set FLASK_APP=fruitpal
$ set FLASK_ENV=development
$ flask init_db
$ flask run
# test
$ pip install '.[test]'
$ pytest
