from behave import given, when, then

from selenium import webdriver


@when('Click on Secondary tab')
def click_secondary_tab(context):
    context.app.secondary_page.click_secondary_tab()

@when('Click on Filter')
def click_filter_button(context):
    context.app.secondary_page.click_filter_button()

@when('Filter the products by “want to sell”')
def click_want_to_sell_filter(context):
    context.app.secondary_page.click_want_to_sell_filter()

@when('Close the filter panel')
def click_close_filter(context):
    context.app.secondary_page.click_close_filter()

@then('Verify all cards have a “for sale” tag')
def verify_for_sale_tag(context):
    context.app.secondary_page.verify_for_sale_tag()

