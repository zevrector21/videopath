from django.core.management.base import BaseCommand

import importlib

class Command(BaseCommand):

    def handle(self, *args, **options):
    	
    	app_name = args[0]
    	action_name = args[1]
    	
    	print '\n\n'
    	print 'Running action ' + action_name + ' from app ' + app_name
    	print '==========================================\n'

    	path = 'videopath.apps.' + app_name + '.actions.' + action_name
    	action = importlib.import_module(path)

        command_args = args[2:]
    	action.run(*command_args)

    	


