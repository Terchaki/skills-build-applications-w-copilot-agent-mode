from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='Desc')
        self.activity = Activity.objects.create(user=self.user, type='run', duration=10, calories=100)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=123)

    def test_user_team(self):
        self.assertEqual(self.user.team.name, 'Test Team')
    def test_activity(self):
        self.assertEqual(self.activity.type, 'run')
    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 123)
