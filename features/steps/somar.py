from behave import given, when, then

from calculadora import Calculadora


@given('I have entered {number1:d} into the calculator')
def enter_number1(context, number1):

    context.number1 = number1


@given('I have also entered {number2:d} into the calculator')
def enter_number2(context, number2):

    context.number2 = number2


@when('I press add')
def press_add(context):

    context.calculator = Calculadora()

    context.result = context.calculator.somar(context.number1, context.number2)


@then('the sum should be {result:d}')
def check_result(context, result):

    assert context.result == result
