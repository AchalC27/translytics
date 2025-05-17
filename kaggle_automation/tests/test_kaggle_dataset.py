# tests/test_kaggle_dataset.py
import pytest
import time
import csv
from pages.home_page import HomePage
from pages.datasets_page import DatasetsPage
from pages.dataset_detail_page import DatasetDetailPage

test_results = []

@pytest.mark.usefixtures("setup")
def test_kaggle_dataset(setup):
    driver = setup  
    start = time.time()
    test_id = "TC001"
    test_name = "Validate Kaggle Huge Stock Market Dataset Page"

    try:
        driver.get("https://www.kaggle.com")

        home = HomePage(driver)
        home.go_to_datasets()

        datasets = DatasetsPage(driver)
        datasets.search_dataset("Huge Stock Market Dataset")

        detail = DatasetDetailPage(driver)
        activity_data = detail.validate_activity_overview()

        assert activity_data["views"] == "1.16M"
        assert activity_data["downloads"] == "129K"
        assert activity_data["engagement"] == "0.11121"
        assert activity_data["comments"] == "105"

        detail.select_last_six_months()
        downloads = detail.get_downloads_for_date()
        assert downloads == "79"

        status = "Pass"

    except Exception as e:
        print(f"Test failed: {e}")
        status = "Fail"

    end = time.time()
    exec_time = round(end - start, 2)

    test_results.append([test_id, test_name, status, exec_time])

    # Write to CSV
    with open("test_results.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Test Case ID", "Test Case Name", "Test Case Status", "Execution Time (s)"])
        writer.writerows(test_results)
