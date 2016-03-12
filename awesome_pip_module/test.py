import sys
import os

class Tax():
	def tax_evasion(self):
		print 'evaded taxes'
		last_time = raw_input("How much money did you make? ")
		print last_time
		file_name = raw_input("name of your tax file?")
		os.system('touch ' + file_name)
		new_file = open(file_name, 'w')
		new_file.write('this is how much money you made---' + last_time)
		new_file.close()


if __name__ == "__main__":
	if len(sys.argv) > 1:
		if sys.argv[1] == 'tax_evasion':
			print sys.argv
			tax = Tax() # creating a new object 
			tax.tax_evasion() # calling the tax_evasion method
	else: 
		print 'you didnt call a function'