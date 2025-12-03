from behave import given, when, then

@given('Open Reelly sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()

@when('Click on sign in link')
def click_sign_in_link(context):
    context.app.sign_in_page.click_sign_in_link()

@when('Enter an email')
def enter_email(context):
    context.app.sign_in_page.enter_email()

@when('Enter a password')
def enter_password(context):
    context.app.sign_in_page.enter_password()

@when('Click on continue button')
def click_continue_button(context):
    context.app.sign_in_page.click_continue_button()
