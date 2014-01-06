Robin Winslow CV
===

This is the code for [my CV site](http://cv.robinwinslow.co.uk).

I build it in Django as an experiment, so I could play around with Django.

For the most part, this site is just flat templates - it doesn't use a database at all. The most interesting bits of code are:

- The API consumers in [profiles.py](cv/profiles.py)
- The [Markdown template tag](cv/templatetags/markdown.py)

Running locally
---

``` bash
$ sudo apt-get install python-pip python-dev libpq-dev
$ sudo pip install -r requirements.txt
$ ./manage.py runserver
```
