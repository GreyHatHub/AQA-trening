rm -r report
pytest -v -s --alluredir report -n auto
allure serve report
