#!/usr/bin/env python
import os
import sys
from api.ArbolB import ArbolB, NodoArbolB, NodoLista, Carpeta
from api.AVL import Arbol,NodoArbol


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "miproyecto.settings")
    try:
    	from django.core.management import execute_from_command_line
    except ImportError:

    	try:
    		import django
    	except ImportError:
    		raise ImportError(
    			"Error"

    		)
    	raise
 
    execute_from_command_line(sys.argv)
    
