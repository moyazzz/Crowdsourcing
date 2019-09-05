'''
Usage: script for using the nlp server to
Data Input: list contains of Question with text + id; Corresponding Answers for each question with text + question id;
Data Output: dict that 1 answer corresponds to 1 question
'''

# impoer django settings module to make this script work separately
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "csgame.settings")
os.environ.setdefault("SPACY_WARNING_IGNORE", "W008")
import django
django.setup()
from users.models import Question, Answer, Attribute
from django.db.models import F, Q
import phase2_reducer
from users.views.rephrasing import rephrase_old as rephrase

'''
script function for phase02
'''
def phase02():
    import importlib
    importlib.reload(phase2_reducer)
    # Get all the queries for answer and question from database
    return phase2_reducer.AnswerReducer().reduce_within_groups(Answer.objects.values_list('text', 'question_id'))

if __name__ == "__main__":
    Answer.objects.update(isFinal=False, count=0)
    for q, (a, count) in phase02().items():
        print("a is: ", a)
        Answer.objects.filter(text=a, question_id=q)[:1].update(isFinal=True, count=count)
    print("Update successfully!")

    # rephrase and import into attributes we have
    for answer in Answer.objects.filter(Q(isFinal=True) & ~Q(text='')):
        Attribute.objects.get_or_create(word=rephrase(answer.question.text, answer.text), answer=answer)
