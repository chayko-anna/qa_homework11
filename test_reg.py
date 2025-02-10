import allure
from selene import have, browser
import os


@allure.title("Successful fill form")
def test_registration(browser_settings):
    with allure.step("Открыть страницу с формой"):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")

    with allure.step("Заполнить имя и фамилию"):
        browser.element('[id="firstName"]').type('Anna')
        browser.element('[id="lastName"]').type('Chayko')

    with allure.step("Заполнить email"):
        browser.element('[id="userEmail"]').type('al.nchko@gmail.com')

    with allure.step("Выбрать пол"):
        browser.element('[for="gender-radio-2"]').click()

    with allure.step("Заполнить номер телефона"):
        browser.element('[id="userNumber"]').type('9102906632').press_tab()

    with allure.step("Выбрать дату рождения"):
        browser.element('[class="react-datepicker__month-select"]').element('[value="0"]').click()
        browser.element('[class="react-datepicker__year-select"]').element('[value="2000"]').click()
        browser.element('[class="react-datepicker__day react-datepicker__day--013"]').click()

    with allure.step("Выбрать предмет"):
        browser.element('[id="subjectsInput"]').type('A')
        browser.all('.subjects-auto-complete__menu').element_by(have.text('Arts')).click()

    with allure.step("Выбрать хобби"):
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-2"]').click()

    with allure.step("Загрузить изображение"):
        browser.element('[id="uploadPicture"]').set_value(os.path.abspath("res/shutterstock_2331893385.jpg"))

    with allure.step("Заполнить адрес"):
        browser.element('[id="currentAddress"]').type('Улица Пушкина, дом Колотушкина')

    with allure.step("Выбрать штат и город"):
        browser.element('[id="state"]').click()
        browser.element('#react-select-3-option-0').click()
        browser.element('[id="city"]').click()
        browser.element('#react-select-4-option-1').click()

    with allure.step("Отправить форму"):
        browser.element('[id="submit"]').click()

    with allure.step("Проверить успешность отправки формы"):
        browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))

    with allure.step("Проверить данные в таблице"):
        browser.element('[class="table-responsive"]').should(have.text('Anna Chayko'))
        browser.element('[class="table-responsive"]').should(have.text('al.nchko@gmail.com'))
        browser.element('[class="table-responsive"]').should(have.text('9102906632'))
        browser.element('[class="table-responsive"]').should(have.text('13 January,2000'))
        browser.element('[class="table-responsive"]').should(have.text('Female'))
        browser.element('[class="table-responsive"]').should(have.text('Arts'))
        browser.element('[class="table-responsive"]').should(have.text('Sports'))
        browser.element('[class="table-responsive"]').should(have.text('Reading'))
        browser.element('[class="table-responsive"]').should(have.text('shutterstock_2331893385.jpg'))
        browser.element('[class="table-responsive"]').should(have.text('Улица Пушкина, дом Колотушкина'))
        browser.element('[class="table-responsive"]').should(have.text('NCR Gurgaon'))
