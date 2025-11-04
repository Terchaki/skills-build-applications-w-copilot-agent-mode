from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Limpa dados existentes
        User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Cria times
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Cria usuários
        tony = User.objects.create_user(username='tony', email='tony@stark.com', password='ironman', first_name='Tony', last_name='Stark', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@rogers.com', password='cap', first_name='Steve', last_name='Rogers', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@wayne.com', password='batman', first_name='Bruce', last_name='Wayne', team=dc)
        diana = User.objects.create_user(username='diana', email='diana@themyscira.com', password='wonder', first_name='Diana', last_name='Prince', team=dc)

        # Cria atividades
        octo_models.Activity.objects.create(user=tony, type='run', duration=30, calories=300)
        octo_models.Activity.objects.create(user=steve, type='cycle', duration=45, calories=400)
        octo_models.Activity.objects.create(user=bruce, type='swim', duration=60, calories=500)
        octo_models.Activity.objects.create(user=diana, type='yoga', duration=50, calories=200)

        # Cria workouts
        octo_models.Workout.objects.create(name='Full Body', description='Treino completo para super-heróis')
        octo_models.Workout.objects.create(name='Cardio Power', description='Cardio intenso para resistência')

        # Cria leaderboard
        octo_models.Leaderboard.objects.create(user=tony, points=1000)
        octo_models.Leaderboard.objects.create(user=steve, points=900)
        octo_models.Leaderboard.objects.create(user=bruce, points=950)
        octo_models.Leaderboard.objects.create(user=diana, points=980)

        self.stdout.write(self.style.SUCCESS('Banco octofit_db populado com dados de super-heróis!'))
