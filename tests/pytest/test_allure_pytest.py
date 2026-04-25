import allure 

@allure.step("Opening browser")
def open_browser():
    with allure.step("Get browser"):
        ...

    with allure.step('Creating course'):
        ...

@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    ... 

@allure.step('Closing browser')
def close_browser():
    ...

def test_feature():
    open_browser()

    create_course(title="Locust")
    create_course(title="sadas")
    create_course(title='jjuihus')
    create_course(title='uihiubd')

    close_browser()