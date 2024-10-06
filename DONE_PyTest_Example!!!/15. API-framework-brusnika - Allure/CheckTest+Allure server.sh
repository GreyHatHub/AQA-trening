rm -r report
pytest -v -s --alluredir report -n auto --tb=no
allure serve report
