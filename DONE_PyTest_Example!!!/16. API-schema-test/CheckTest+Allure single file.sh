rm -r report
rm -r allure-report
pytest -v -s --alluredir report -n auto --tb=no
allure generate --single-file report
