Ginger
======================

For the foodie in you.

Quickstart
----------

To bootstrap the project::

    virtualenv venv
    source venv/bin/activate
    cd path/to/ginger/repository
    pip install -r requirements.txt
    pip install -e .
    cp ginger/local_settings.py.example ginger/local_settings.py
    manage.py syncdb --migrate
