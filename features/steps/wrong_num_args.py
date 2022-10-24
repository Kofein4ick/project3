from behave import *
import subprocess

@given('даем тестовый файл "D:/project3/text.txt"')
def step_impl(context):
    pass

@when('запускаем приложение с избыточным количеством аргументов')
def step_impl(context):
    context.response=subprocess.run(["python","D:/project3/main.py","D:/project3/text.txt","налоги","доходы","10","20"], shell=True)

@then('получаем сообщение об ошибке аргументов')
def step_impl(context):
    assert context.failed is False