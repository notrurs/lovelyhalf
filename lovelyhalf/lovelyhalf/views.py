from random import choice
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request):
    return render(request, 'lovelyhalf/index.html', {'title': 'Привет, любимая ❤'})


def vote_page(request, question_id=1, correct_answer=None, next_question_id=None, media=None):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'lovelyhalf/vote_page.html', {
        'title': '❤❤❤❤❤',
        'question': question,
        'correct_answer': correct_answer,
        'next_question_id': next_question_id,
        'media': media
    })


def restaurant_page(request):
    return render(request, 'lovelyhalf/restaurant.html', {
        'title': 'ПАДАРАЧКИИИИ'
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = request.POST['choice']
    except Exception:
        # Redisplay the question voting form.
        return render(request, 'lovelyhalf/vote_page.html', {
            'question': question,
            'error_message': f"Didn't find choice: {request.POST}",
        })
    else:
        if question.correct_answer == selected_choice:
            next_question_id = question_id + 1

            correct_data_extension = question.correct_data.url.split('.')[1]
            if correct_data_extension == 'mp4':
                return render(request, 'lovelyhalf/vote_page.html', {
                    'title': '❤❤❤❤❤',
                    'question': question,
                    'correct_answer': True,
                    'next_question_id': next_question_id,
                    'media': 'video'
                })
            return render(request, 'lovelyhalf/vote_page.html', {
                'title': '❤❤❤❤❤',
                'question': question,
                'correct_answer': True,
                'next_question_id': next_question_id,
                'media': 'image'
            })
        else:
            correct_answer = False

            titles = [
                'Ну зачем ты так со мной? :(',
                'Мяу мяу мяу :(',
                'НЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕТ D;',
                'Я щас заплачу :(',
                'Это. Было. Больно.',
            ]

            signs = [
                'Ну вот, теперь в мире на одного плачущего котика больше',
                'Пожалуйста, больше так не делай, ладно?',
                'Вот посмотри, до чего ты довела кота!',
                'Ой! Моё сердечко! Кольнуло что-то((((',
                'Это сейчас я',
            ]

            buttons = [
                'Обещаю исправиться!',
                'Всё-всё-всё, сейчас всё будет хорошо!',
                'Ой, прости, пожалуйста!',
                'Я больше так не буду!',
                'Это была ошибка всей моей жизни!',
            ]

            imgs = [
                'sad-cat-1.gif',
                'sad-cat-2.gif',
                'sad-cat-3.gif',
                'sad-cat-4.gif',
                'sad-cat-5.gif',
                'sad-cat-6.gif',
            ]

            modal_data = {
                'title': choice(titles),
                'sign': choice(signs),
                'button': choice(buttons),
                'img': choice(imgs)
            }

            return render(request, 'lovelyhalf/vote_page.html', {
                'title': '❤❤❤❤❤',
                'question': question,
                'correct_answer': correct_answer,
                'modal_data': modal_data,
            })
