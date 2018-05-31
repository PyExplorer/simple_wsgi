# simple_wsgi
Parse request, route to view, create response

**From command line:**

```
$ python3 uwsgi --http :9090 --wsgi-file simple_wsgi.py
```

Requirements
--
- at least python 3.5
- uwsgi=>2.0.17


Installation
--

just clone the project and install the requirements:

```
$ git clone https://github.com/PyExplorer/simple_wsgi.git
$ cd simple_wsgi
$ pip3 install -r requirements.txt
```

Docs
--
After run uwsgi server we can start browser with url 

**http://localhost:9090**

The script supports only 3 paths:
```
/ - Main page
/hello - Hello world page
/hello/help - Help for Hello world page

e.g. http://localhost:9090/hello/help
```

Contributing
--

To contribute, pick an issue to work on and leave a comment saying that you've taken the issue. Don't forget to mention when you want to submit the pull request.

Launch tests
--

Not yet...