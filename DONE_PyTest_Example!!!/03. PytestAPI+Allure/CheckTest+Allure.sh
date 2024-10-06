rm -r report
pytest -sv --alluredir report -n auto
allure serve report
