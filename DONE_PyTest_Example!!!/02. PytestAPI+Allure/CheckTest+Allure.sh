rm -r report
pytest -vs --alluredir report -n auto
allure serve report
