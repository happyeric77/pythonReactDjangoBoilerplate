import os
from django.core.management.base import BaseCommand

BASE_DIR = os.path.dirname(
            os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.abspath(__file__)))))

project_name = ''
project_dir = ''
for project_name_candidate in os.listdir(BASE_DIR):
    if os.path.exists(os.path.join(BASE_DIR, project_name_candidate, 'settings')):
        project_name = project_name_candidate
        project_dir = os.path.join(BASE_DIR, project_name_candidate)


class Command(BaseCommand):
    help = 'Renames a Django project'

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str, help='The new Django project name')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']
        if len(new_project_name)>10:

            files_to_rename = [os.path.join(project_dir, 'settings/base.py'), os.path.join(project_dir, 'wsgi.py'), 'manage.py']
            folder_to_rename = project_name

            for f in files_to_rename:
                with open(f, 'r') as file:
                    filedata = file.read()

                filedata = filedata.replace(project_name, new_project_name)

                with open(f, 'w') as file:
                    file.write(filedata)

            os.rename(folder_to_rename, new_project_name)

            self.stdout.write(self.style.SUCCESS(
                'Project has been renamed to {newName} from {oldName}'.format(oldName=project_name, newName=new_project_name)
            ))
        else:
            raise EnvironmentError('Length of project name needs to be > 10')