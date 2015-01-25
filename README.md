# Shortlinks #

Little link shortener built with [Flask][flask].

This simple app is built as an exercise for job application. I wanted to try
something new and Flask felt like suitable tool for this. Persistent storage was not required, but this felt like a good chance to learn basics of SQLAlchemy as well, so links are stored to database permanently.

I developed and tested this app with Python 3.4, but it should work with python
2.7 as well.

Layout is built using [Pure.css][pure].

## Getting started  ##

1. Create python3 virtualenv with your favorite tool.
2. Install dependencies `pip install -r requirements.txt`
3. Start development server: `./runserver.py`
4. Open browser and go to `http://localhost:5000`

## Improvement ideas ##

* Users and editable links
* Change return type based on Accept-header
* Rate limit
* Better input validation

## License ##

This project is licensed under MIT license. See LICENSE.md for complete
license.

[flask]:http://flask.pocoo.org/ "Flask"
[pure]: http://purecss.io/ "Pure"
