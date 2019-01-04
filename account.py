# Importar librería
import os

# Declaracion de variables
clientes = []
numCuentas = 0
opcion = 0

# Declaración de métodos
def crearCuenta(clientes):
	global numCuentas
	
	# Con este método se crea una cuenta bancaria
	nombre = input('Introduzca nombre: ')
	apellido = input('Introduzca apellido: ')
	
	# Se crea lista donde el index es el nombre de la variable
	cuenta = {'nombre': nombre, 'apellido': apellido, 'cuenta': {'saldo': 0, 'numeroCuenta': numCuentas}}
	clientes.append(cuenta)
	numCuentas += 1
	print('Cuenta creada ---> ' + str(numCuentas))
	input('Pulse Enter para continuar...')
	return clientes, numCuentas
	
def hacerDeposito(clientes):
	# Con este método se incrementa el saldo de la cuenta
	if len(clientes) > 0:
		cuenta = input('Inidique la cuenta al cual realizará el depósito: ')
		cantidad = input('Indique la cantidad a depositar: ')
		saldoActual = clientes[int(cuenta)]['cuenta']['saldo']
		clientes[int(cuenta)]['cuenta']['saldo'] = saldoActual + int(cantidad)
		print('Se ha realizado el depósito')
	else:
		print('No existen cuentas')
	
	input('Pulse Enter para continuar...')
	
def verCuentas(clientes):
	# Con este método se pueden visualizar todas las cuenta
	if len(clientes) > 0:
		for cliente in clientes:
			print('Nombre: ' + cliente['nombre'])
			print('Apellido: ' + cliente['apellido'])
			print('N° Cuenta: ' + str(cliente['cuenta']['numeroCuenta']))
			print('\n')
	else:
		print('No existen cuentas')
	
	input('Pulse Enter para continuar...')

def consultarSaldo(clientes):
	# Con este método se podrá ver el saldo en la cuenta
	if len(clientes) > 0:
		cuenta =  input('Inidique la cuenta que desea consultar: ')
		print('El saldo de la cuenta ' + cuenta + ' es de: ' + str(clientes[int(cuenta)]['cuenta']['saldo']) + ' Dólares.')
	else:
		print('No existen cuentas')
		
	input('Pulse Enter para continuar...')
	
def hacerRetiro(clientes):
	# Con este método se podrá restar saldo a la cuenta
	if len(clientes) > 0:
		cuenta =  input('Inidique la cuenta al cual realizará el retiro: ')
		cantidad = input('Indique la cantidad a retirar: ')
		saldoActual = clientes[int(cuenta)]['cuenta']['saldo']
		clientes[int(cuenta)]['cuenta']['saldo'] = saldoActual - int(cantidad)
		print('Se realizó el retiro')
	else:
		print('No existen cuentas')
	
	input('Pulse Enter para continuar...')

while ('6' != opcion):
	opcion = input('''Seleccione la operación a realizar:
	1. Ver Cuentas
	2. Crear Cuenta
	3. Ver Saldo
	4. Hacer Depósito
	5. Hacer Retiro
	6. Salir
	''')
	
	print('\n')
	
	if opcion == '1':
		verCuentas(clientes)
	elif opcion == '2':
		crearCuenta(clientes)
	elif opcion == '3':
		consultarSaldo(clientes)
	elif opcion == '4':
		hacerDeposito(clientes)
	elif opcion == '5':
		hacerRetiro(clientes)
	os.system("CLS")
	
print('Fin del Programa')
