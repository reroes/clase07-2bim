import sys
import csv
from rx import Observable
from rx import of, create, operators as op


def leer_archivo(observer, schedule):
    archivo = csv.DictReader(open("ods_1_2.csv", "r"))
    for l in archivo:
        observer.on_next(l)
    observer.on_completed()

suscribe = create(leer_archivo)

composed = suscribe.pipe(
    op.map(lambda i: i['id_str'])
)
composed.subscribe(
        on_next = lambda i: print("Received {0}".format(i)),
        on_completed = lambda: print("Done!")
        )
