#! /usr/bin/python3
#
# script simple para crear imagenes APNG y extraer las imagenes que conforman
# un archivo del tipo APNG
# autor: Roso Peñaranda
# email: rosopenaranda@gmail.com

from argparse import ArgumentParser
from apng import APNG
import sys

# Se parsean los argumentos de entrada
parser = ArgumentParser()
parser.add_argument('acc',help=" accion a tomar, crear o extraer", choices=['crear', 'extraer'])
parser.add_argument('-f', help="nombre del archivo con las imagenes, una por linea")
parser.add_argument('-i', help="nombre de la imagenes")
parser.add_argument('-d', type=int ,help="delay en segundos")
parser.add_argument('-o', help="nombre de la imagen de salida")
args = parser.parse_args()

def crear(entrada, retardo, salida):

  try:
    with open(entrada) as archivo:
      lista = []
      for linea in archivo:
        lista.append(linea[:-1])

  except IndexError:
            sys.stdout.write("No se encuentra el archivo:\n")

  retarto = retardo * 100
  APNG.from_files(lista, delay=retardo).save(salida + ".png")


def extraer(imagen):

  anim = APNG.open(imagen)
  cont = 1
  for png, control in anim.frames:
    png.save('img-{cont}.png'.format(cont=cont))
    cont += 1

#main

if args.acc == "crear":
  retardo = 1
  if args.d != None:
    retardo = args.d

  salida = "img"
  if args.o != None:
    salida = args.o

  archivo = args.f
  if args.f == None:
    print ('debe indicar el nombre de un archivo')
    sys.exit()
  crear(archivo,retardo,salida)

elif args.acc == "extraer":

  imagen = args.i
  if args.i == None:
    print ('debe indicar el nombre la imagen')
    sys.exit()

  extraer(imagen)
