#########################################
#
# 3 Functions in Python to work with the Chilean Rut
#
# Created by Ceslat
#
# Copiright (c) 2015
# Dual licensed under the GPL v.3 licenses.
#
# http://github.com/ceslat/ChileanRut
#
#########################################


def format_chilean_rut(rut, format=4):
	unformat_rut = list(rut.strip().replace('.', '').replace('-', '').upper())
	if len(unformat_rut) < 8:
		return False, 'Input a Chilean Rut with verificator digit'
	else:
		format_b = ''.join(unformat_rut)
		unformat_rut.insert(len(unformat_rut) - 1,'-')
		format_c = ''.join(unformat_rut)
		format_a = format_c.split('-')[0]
		unformat_rut.insert(len(unformat_rut) - 5,'.')
		unformat_rut.insert(len(unformat_rut) - 9,'.')
		format_d = ''.join(unformat_rut)
		if format == 1:
			return True, format_a
		elif format == 2:
			return True, format_b
		elif format == 3:
			return True, format_c
		else:
			return True, format_d


def determined_check_digit(rut):
	status, unformat_rut = format_chilean_rut(rut, 1)
	secuence = [2, 3, 4, 5, 6, 7, 2, 3]
	if status:
		inversed_rut = map(int, reversed(str(unformat_rut)))
		s = sum(d * f for d, f in zip(inversed_rut, secuence))
		dv = 'K' if (-s) % 11 == 10 else (-s) % 11
		return True, rut, str(dv)
	else:
		return False, rut, 0


def valid_chilean_rut(rut):
	status, unformat_rut, dv = determined_check_digit(rut)
	if status:
		return True if dv == rut[-1] else False
	else:
		return False


rut = str(input('Input the Chilean Rut with verificator digit (DV) >> '))
if len(list(rut.strip().replace('.', '').replace('-', '').upper())) >= 8 :
	print '##############################################'
	print 'These are the formats which can be obtained.'
	print 'With DV: ' + format_chilean_rut(rut, 1)[1]
	print 'With point without script: ' + format_chilean_rut(rut, 2)[1]
	print 'Only Script: ' + format_chilean_rut(rut, 3)[1]
	print 'With point and script: ' + format_chilean_rut(rut, 4)[1]
	print '##############################################'
	print 'The Real DV is: ' + determined_check_digit(rut)[2]
	print '##############################################'
	print 'Is Valid this Chilian Rut? R: ' + str(valid_chilean_rut(rut))
else:
	print 'Input a Chilean Rut with verificator digit'
