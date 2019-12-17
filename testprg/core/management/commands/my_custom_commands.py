from core.models import MyModel
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import argparse

parser = argparse.ArgumentParser(description='Example with non-optional arguments')

class Command(BaseCommand):
    help = 'To edit file field'

    def add_arguments(self, parser):
        parser.add_argument('file', help='Update for the file content')

    def handle(self, *args, **kwargs):
        file = kwargs['file']
        #print(type(total))
        #for i in range(total):
        for i in MyModel.objects.all():
        	s=MyModel(input_file=file)
        	i.input_file=s.input_file
        	i.save()