from behave import *
import subprocess

@given('подаем тестовый файл "D:/project3/text3.txt"')
def step_impl(context):
    pass

@when('запускаем приложение с параметрами налоги России 2')
def step_impl(context):
    context.response=subprocess.run(["python","D:/project3/main.py","D:/project3/text3.txt","налоги","России","2"], shell=True)

@then('получаем кол-во равное 0')
def step_impl(context):
    assert context.failed is False