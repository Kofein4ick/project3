from behave import *
import subprocess

@given('подготовили тестовый файл "D:/project3/text1.txt"')
def step_impl(context):
    pass

@when('запускаем приложение с данным файлом')
def step_impl(context):
    context.response=subprocess.run(["python","D:/project3/main.py","D:/project3/text1.txt","налоги","доходы","10"], shell=True)

@then('получаем сообщение об ошибке')
def step_impl(context):
    assert context.failed is False