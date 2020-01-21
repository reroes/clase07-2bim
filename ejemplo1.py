"""
	La programación reactiva es un paradigma enfocado en el trabajo con flujos de datos 
	finitos o infinitos de manera asíncrona
	
	Python:
	The Reactive Extensions for Python (RxPY)
	
	reactivex:
	http://reactivex.io/

"""

import sys
from rx import Observable
from rx import from_





# argv = Observable.from_(sys.argv[1:])
argv = from_(sys.argv[1:])

argv.subscribe(
    on_next=lambda i: print("on_next: {}".format(i)),
    on_error=lambda e: print("on_error: {}".format(e)),
    on_completed=lambda: print("on_completed"))
