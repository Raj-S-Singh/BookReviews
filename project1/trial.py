import requests
KEY="UP3KG3M255x6CSKNKT6hw"
res=requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": KEY, "isbns": "9781632168146"})
print(res.json())
