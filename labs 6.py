from aplicacion.banco.cliente_bancario import ClienteBancario
#============================================
#try : intenta (correr las instrucciones)
#except: atrapar el error en una variable e
#e se puede convertir a string
#============================================
#============================================
#Error por sacar más dinero del que tiene
#============================================

try:
    cliente= ClienteBancario("jaime Andrade","Hernandez Sanches",28,0.0)
    cliente.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente.imprimirInfo)
#============================================
#Exception es el objeto mas general de error
#============================================
except Exception as e:
    print("Error:"+ str(e))
#============================================
#Error para usar un atributo privado
#============================================
try:
    print(cliente._nombres)
except Exception as ex:
    print("Error: "+ str(ex))
#============================================
#Forma correcta
#============================================
print(cliente.nombres)
