rm -r report
pytest -vs --alluredir report -n 1
allure serve report
