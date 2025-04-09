from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Initialize MongoDB collections for octofit_db'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Create collections and indexes
        db.users.create_index("email", unique=True)
        db.teams.create_index("name", unique=True)
        db.activity.create_index("activity_id", unique=True)
        db.leaderboard.create_index("leaderboard_id", unique=True)
        db.workouts.create_index("workout_id", unique=True)

        self.stdout.write(self.style.SUCCESS('MongoDB collections initialized successfully.'))
