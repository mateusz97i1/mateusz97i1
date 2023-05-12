#!/bin/bash

# Instalacja modułu decouple
pip install python-decouple -t ./python_packages

# Przekazanie kontroli dalej do wersji @vercel/python
vercel-python "$@"