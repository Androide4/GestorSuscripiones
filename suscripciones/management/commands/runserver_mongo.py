from django.core.management.commands.runserver import Command as RunServer

class Command(RunServer):
    def inner_run(self, *args, **options):
        from django.conf import settings
        print("🚀 Usando MongoDB Atlas como base de datos")
        super().inner_run(*args, **options)