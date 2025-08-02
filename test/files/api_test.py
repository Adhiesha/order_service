import requests
import sys
import os


def test_endpoint(base_url, path, expected_status=200):
    full_url = f"{base_url.rstrip('/')}/{path.lstrip('/')}"
    print(f"Testing {full_url} ...")
    try:
        response = requests.get(full_url)
        assert response.status_code == expected_status
        print(f"[PASS] {full_url}")
    except Exception as e:
        print(f"[FAIL] {full_url} - {e}")
        sys.exit(1)


def main():
    base_url = os.environ.get("API_BASE_URL")
    if not base_url:
        print("Missing environment variable: API_BASE_URL")
        sys.exit(1)

    test_endpoint(base_url, "/recommendations/trending")
    test_endpoint(base_url, "/recommendations/most_played")
    test_endpoint(base_url, "/recommendations/top_categories")


if __name__ == "__main__":
    main()
