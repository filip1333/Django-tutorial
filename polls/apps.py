from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'

    def create_question(question_text, days):
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)