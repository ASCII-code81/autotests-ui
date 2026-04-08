from playwright.sync_api import sync_playwright, expect 

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
    context=browser.new_context()
    page=context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
    email=page.get_by_test_id('registration-form-email-input').locator('input')
    email.focus()
    for a in "user@gmail.com":
        email.type(a, delay=20)
    user=page.get_by_test_id('registration-form-username-input').locator('input')
    user.focus()
    for a in "user":
        user.type(a, delay=20)
    password=page.get_by_test_id('registration-form-password-input').locator('input')
    password.focus()
    for a in "password":
        password.type(a, delay=20)
    button=page.get_by_test_id('registration-page-registration-button')
    button.click()
    context.storage_state(path='abc.json')

with sync_playwright() as playwright:
    browser=playwright.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
    context=browser.new_context(storage_state='abc.json')
    page=context.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    page.wait_for_timeout(3000)
    header=page.get_by_test_id('courses-list-toolbar-title-text')
    expect(header).to_be_visible()
    expect(header).to_have_text('Courses')
    result=page.get_by_test_id('courses-list-empty-view-title-text')
    expect(result).to_be_visible() 
    expect(result).to_have_text("There is no results")
    empty=page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty).to_be_visible()
    pipeline=page.get_by_test_id('courses-list-empty-view-description-text')
    expect(pipeline).to_be_visible()
    expect(pipeline).to_have_text('Results from the load test pipeline will be displayed here')