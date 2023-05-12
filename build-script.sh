#!/bin/bash

# Instalacja modułu decouple
pip install python-decouple -t ./python_packages/lib/python3.9/site-packages

# Przekazanie kontroli dalej do wersji @vercel/python
vercel-python "$@"
