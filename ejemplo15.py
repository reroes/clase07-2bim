import sys
from rx import Observable
from rx import of, create, operators as op

def leer_archivo(observer, schedule):
    archivo = open("ods_1_2.csv", "r")
    lineas = archivo.readlines()
    for l in lineas:
        observer.on_next(l)
    observer.on_completed()

suscribe = create(leer_archivo)

composed = suscribe.pipe(
    op.map(lambda s:s),
    op.filter(lambda i: len(i)>2)
)
composed.subscribe(lambda i: print("Received {0}".format(i)))
print("done")
