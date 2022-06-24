print("welcome to your axis ATM")
print("insert your card")
print("please do not remove your card until the processor")
lang=(input("choose your lang"))
if lang=="english":
	pincode=int(input("enter your secret number"))
	if pincode==8712:
		print("correct")
		account=(input("which typr of acount"))
		if account=="saving account":
			tranz=(input("enter your tranz"))
			if tranz=="withdrawal":
				amt=int(input("enter your amt"))
				b=20000
				if amt>=100 and amt<=20000:
					print("confirm")
					print("wait for your cash")
					print("Thank for your transaction and your current balance is",b-amt)
				elif amt=="insufficient balance":
					print("oops srry")
				else:
					print("error")
			elif tranz=="check your balance":
				print("enter your secret number")
			else:
				print("netbanking")
		elif acount=="current account":
			print("next")
		else:
			print("error")
	elif pincode=="try again":
		print("enter your pincode again")
	else:
		print("incorrect")
elif lang=="hindi":
	print("next")
else:
	print("another lang")