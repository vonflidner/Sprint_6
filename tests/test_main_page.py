import allure
import pytest
from data import ANSWER_1, ANSWER_2, ANSWER_3, ANSWER_4, ANSWER_5, ANSWER_6, ANSWER_7, ANSWER_8, Urls
from pages.main_page import MainPage


@allure.feature("Часто задаваемые вопросы")
class TestMainPage:

    @allure.title("Тест: проверка правильности отображаемого ответа на вопрос")
    @allure.description('Проверяем, что при клике на вопрос отображается правильный ответ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize(
        'num, result',
        [
            (0, ANSWER_1),
            (1, ANSWER_2),
            (2, ANSWER_3),
            (3, ANSWER_4),
            (4, ANSWER_5),
            (5, ANSWER_6),
            (6, ANSWER_7),
            (7, ANSWER_8),
        ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)

        with allure.step("Переход на главную страницу"):
            main_page.go_to_url(Urls.MAIN_PAGE_URL)

        with allure.step(f"Нажатие на вопрос {num+1}"):
            answer_text = main_page.get_answer_text(num)

        with allure.step("Проверка текста ответа"):
            assert answer_text == result, f"Ожидалось: {result}, но получено: {answer_text}"

