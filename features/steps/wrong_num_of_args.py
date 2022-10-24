from behave import *
import subprocess

@given('подготовили тестовый файл "D:/project3/text.txt"')
def step_impl(context):
    pass

@when('запускаем приложение с недостаточным количеством аргументов')
def step_impl(context):
    context.response=subprocess.run(["python","D:/project3/main.py","D:/project3/text.txt","налоги","доходы"], shell=True)

@then('получаем сообщение об ошибке недостатка аргументов')
def step_impl(context):
    assert context.failed is False