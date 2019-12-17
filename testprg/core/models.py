from django.db import models
from django.db.models.signals import post_save, post_init


# Create your models here.

class MyModel (models.Model):
	encrypt= models.CharField(blank = True , max_length =10000,null=True)
	input_file= models.FileField(blank = True )
	#test_feild = models.CharField(blank = True ,max_length =10000)
	state_check1 = models.CharField(default='Created', max_length =10000)
	#state_check2 = models.CharField(default='Created', max_length =10000)
	__original_feild1 = None
	#__original_feild2 = None
	file_contents=None
	
	def __init__(self, *args, **kwargs):
		super(MyModel, self).__init__(*args, **kwargs)
		self.__original_feild1 = self.input_file
		#self.__original_feild2 = self.encrypt
		

	def edits(self,strings=None):
		self.input_file._set_file(strings)


	def clean(self):
		if self.input_file :
			file_contents = self.input_file.read()
			self.encrypt='*'
			for i in file_contents:
				self.encrypt += '*'
		else:
			self.encrypt=None
			#self.state_check1="New file "


	def save(self, force_insert=False, force_update=False, *args, **kwargs):
		if self.input_file != self.__original_feild1:
			if self.state_check1 == "input_file changed":
				self.state_check1 = "input_file changed again"
			else :
				self.state_check1 = "input_file changed"

		super(MyModel, self).save(force_insert, force_update, *args, **kwargs)
		self.__original_feild = self.input_file