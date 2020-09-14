from django.db import models


# Create your models here.
class Question(models.Model):
    title = models.CharField('Название вопроса', max_length=50)
    image = models.ImageField('Картинка', upload_to='question_files')
    question = models.CharField('Вопрос', max_length=50)
    answer1 = models.CharField('Вариант ответа 1', max_length=50)
    answer2 = models.CharField('Вариант ответа 2', max_length=50)
    answer3 = models.CharField('Вариант ответа 3', max_length=50)
    answer4 = models.CharField('Вариант ответа 4', max_length=50)
    correct_answer = models.CharField('Правильный ответ', max_length=50, null=True)
    correct_title = models.CharField('Заголовок правильного ответа', max_length=50, null=True)
    correct_text = models.CharField('Текст правильного ответа', max_length=50, null=True)
    correct_data = models.FileField('Файл правильного ответа', upload_to='question_files', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
