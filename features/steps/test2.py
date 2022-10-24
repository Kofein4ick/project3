from behave import *
import subprocess

@given('на вход даем тестовый файл "D:/project3/text2.txt"')
def step_impl(context):
    pass

@when('запускаем приложение с параметрами налоги доходы 100')
def step_impl(context):
    context.response=subprocess.run(["python","D:/project3/main.py","D:/project3/text2.txt","налоги","доходы","100"], shell=True)

@then('получаем кол-во равное 6')
def step_impl(context):
    assert context.failed is False