# Mini API Fuzzer

Small, simple API endpoint fuzzer that hits endpoints from a `wordlist.txt` and prints successful responses (200–399) and JSON output when available.

**Script:** `ApiFuzzer.py`. :contentReference[oaicite:0]{index=0}

## Features
- Loads endpoints from `wordlist.txt`
- Requests each endpoint with a configurable delay
- Only shows successful responses (HTTP 200–399)
- Prints JSON response body when available
- Colored terminal output for readability

## Requirements
- Python 3.8+
- Packages: `requests`, `colorama`

Install dependencies:
```
pip install requests colorama
```
**Usage**

1-Put ApiFuzzer.py and wordlist.txt in the same folder.
2-Run:

```python3 ApiFuzzer.py```
**Example session**
```
Enter target URL: https://example.com/
Delay between requests (seconds): 0.5
Loaded 100 words from wordlist.txt
Starting fuzzing against: https://example.com
Only showing successful responses (status codes 200-399)
[FOUND] https://example.com/admin (Status: 200)
[DATA] {"message":"ok"}
```
