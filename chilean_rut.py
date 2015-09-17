#########################################
#
# 3 Functions in Python to work with the Chilean Rut
# 3 Funciones en Python para trabajar con el Rut Chileno
#
# Created by Ceslat
#
# Copiright (c) 2015
# Dual licensed under the GPL v.3 licenses.
#
# http://github.com/ceslat/ChileanRut
#
#########################################


def format_chilean_rut(rut, format=3):
	unformat_rut = list(rut.strip().replace('.', '').replace('-', '').upper())
	format_a = ''.join(unformat_rut)
	if len(unformat_rut) == 9:
		unformat_rut.insert(8,'-')
		format_b = ''.join(unformat_rut)
		unformat_rut.insert(5,'.')
		unformat_rut.insert(2,'.')
		format_c = ''.join(unformat_rut)
	elif len(unformat_rut) == 8:
		unformat_rut.insert(7,'-')
		format_b = ''.join(unformat_rut)
		unformat_rut.insert(4,'.')
		unformat_rut.insert(1,'.')
		format_c = ''.join(unformat_rut)
	else:
		return 'Please enter a valid Rut'
	if format == 1:
		return format_a
	elif format == 2:
		return format_b
	else:
		return format_c


def determined_check_digit(rut):
	rut = format_chilean_rut(rut, 1)
	secuence = [2, 3, 4, 5, 6, 7, 2, 3]
	inversed_rut = map(int, reversed(str(rut[:-1])))
	s = sum(d * f for d, f in zip(inversed_rut, secuence))
	dv = 'K' if (-s) % 11 == 10 else (-s) % 11
	return str(dv)


def valid_chilean_rut(rut):
	dv = determined_check_digit(rut)
	return True if dv == rut[-1] else False
	