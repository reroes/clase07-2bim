import sys
from rx import Observable
from rx import of, create, operators as op

def leer_archivo(observer, schedule):
    for l in ["hola", "mundo", "en", "reactive"]:
        observer.on_next(l)
    observer.on_completed()

suscribe = create(leer_archivo)

composed = suscribe.pipe(
    op.map(lambda s:s),
    op.filter(lambda i: len(i)>2)
)
composed.subscribe(lambda i: print("Received {0}".format(i)))
print("done")
