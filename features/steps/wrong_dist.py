from behave import *
import subprocess

@given('подаем тестовый файл "D:/project3/text.txt"')
def step_impl(context):
    pass

@when('запускаем приложение с неверно указанным расстоянием')
def step_impl(context):
    context.response=subprocess.run(["python","D:/project3/main.py","D:/project3/text.txt","налоги","доходы","a"], shell=True)

@then('получаем сообщение об ошибке неправильного расстояния')
def step_impl(context):
    assert context.failed is False