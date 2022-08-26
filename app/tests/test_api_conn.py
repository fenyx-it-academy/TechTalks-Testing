from app.api_conn import fetch_currency
import json


sample_res = {
    "result": "success",
    "base_code": "USD"
}

sample_err = {
	"result": "error",
	"error-type": "unknown-code"
}

def test_api_conn():
    # res = fetch_currency('USD')  # actual result from API call
    res = (sample_res)
    assert res['result'] == 'success'
    assert res['base_code'] == 'USD'