def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()

print('Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы')


def inner_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()
inner_function()
