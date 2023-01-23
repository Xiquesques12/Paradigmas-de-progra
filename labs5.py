#============================================
#del directorio aplicacion, el subdirectorio repositorio
#el archivo besedadatos.py : trae el objeto Basededatos
#============================================
from aplicacion.respositorio.basededatos import BaseDeDatos
#===========================================
#del directorio aplicacion, el subdirectorio repositorio
#el archivo s3.py:tre el objeto s3
#============================================
from aplicacion.repositorio.s3 import S3
#============================================
#del directorio aplicacion, el subdirecotio repositorio
#el archivo sistemadearchivos.py : trae el objeto sistemadeArchivos
#============================================
from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos
#============================================
#del directorio aplicacion, el subdirectorio modelos
#el archivo usuario.py: trae el objeto Usuario
#============================================
from aplicacion.modelos.usuario import Usuario
#============================================
#del directorio aplicacion, el subdirectorio negocios
#el archivo manejosdeinscripciones.py: trae el objeto ManejoDeInscripciones
#============================================
from aplicacion.negocios.manejosdeinscripciones import ManejosDeInscripciones
#============================================
#crear el objeto usuario
#============================================

usuario= Usuario("Roberto","jimenez",18)
#============================================
#crear el objeto s3
#============================================
repositorio = S3("2321321321","sdf324223","MiCubeta")
#============================================

#interface inscribirUsuario del objeto ManejoDeInscripciones
ManejosDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")
#============================================
#crear el objeto sistemadearchivos
#============================================
repositorioSistemaDeArchivos = SistemaDeArchivos("/home/users")
#============================================
#Interface inscribir usuario del objeto ManejoDeInscripciones
#============================================
ManejosDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")
#============================================
#crear el objeto basededatos
#============================================
repositorioBaseDeDatos = BaseDeDatos("localhost","admin","admin123")
#============================================
#interface inscribirUsuario del objeto ManejoDeInscripciones
#============================================
ManejosDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")

