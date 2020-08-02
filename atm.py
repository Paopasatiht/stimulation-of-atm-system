#atm.py

money = 10000

print('กด 1 : ถอนเงิน')
print('กด 2 : เช็คยอดเงิน')
print('กด Q : ออกจากระบบ')
print('-------------')
menu = input('กรุณาเลือกเมนู: ')#user เลือกแล้วเราจะเก็บเมนูไว้

while menu != 'Q':
	if menu == '1':
		print('<<< ถอนเงิน >>>')
		withdraw = int(input('กรุณากรอกจำนวนเงิน: '))
		while withdraw > money:
			print('เงินในบัญชีไม่พอ กรุณากรอกยอดเงินให้ถูกต้อง')
			withdraw = int(input('กรุณากรอกจำนวนเงิน: '))

		print('กรุณารับเงิน {} บาท'.format(withdraw))
		money = money - withdraw
		print('คุณมียอดเงินคงเหลือ: {} บาท'.format(money))
	elif menu == '2':
		print('ยอดเงินของคุณคือ: {} บาท'.format(money))

	'''
		print('กด 3 : เช็คยอดเงินคงเหลือ')
		Q = input('เลือกเมนู: ')
		if Q == '3':
			x = (money - withdraw)
			print(x)
		elif Q == '2':
			print('จบเมนู')
	'''

	print('-------------')
	print('กด 1 : ถอนเงิน')
	print('กด 2 : เช็คยอดเงิน')
	print('กด Q : ออกจากระบบ')
	menu = input('กรุณาเลือกเมนู: ')

print('ขอบคุณที่ใช้บริการ กรุณารับบัตรค่ะ')