import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.

class QuestionModelTests(TestCase):
        time=timezone.now() + datetime.timedelta(days=30)
        future_question=Question(date=time)
        
        self.assertIS(future_question.was_published_recently(), True)
