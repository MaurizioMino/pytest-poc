from behave import given, when, then
from selenium import webdriver

@given('launch chrome browser in {url}')
def step_impl(context, url):
    context.driver = webdriver.Chrome(executable_path = './drivers/chromedriver.exe')
    context.driver.get(url)

@when('user click on My Account Menu')
def clickMyAccount(context):
    context.driver.find_element_by_xpath("//a[ text()='My Account' ]").click()

@when('enter {email} in email textbox')
def setEmail(context, email):
    context.driver.find_element_by_xpath("//input[ @id='username' ]").send_keys(email)

@when('enter {password} textbox')
def setPw(context, password):
    context.driver.find_element_by_xpath("//input[ @id='password' ]").send_keys(password)

@when('click on login button')
def clickLogin(context):
    context.driver.find_element_by_xpath("//input[ @name='login' ]").click()

@then('User must successfully login to the web page')
def checkSuccesfullyLogin(context):
    status = context.driver.find_element_by_xpath("//a[ text()='Sign out' ]").is_displayed()
    assert status is True

@then( 'Proper error must be displayed {err}' )
def checkSuccesfullyLogin( context, err ):
    status = context.driver.find_element_by_xpath( f"//*[ contains(text(),'{err}' )]" ).is_displayed()

    assert status is True

@then('close browser')
def close(context):
    context.driver.close()
