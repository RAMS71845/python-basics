import requests

# response=requests.get("https://api.github.com/")
# response.raise_for_status()
# print("status code: ",response.status_code)
# data=response.json()
# print(data["current_user_url"])


#POST-call
#post request k wakt jo data bhejtey hai usko payload kahtey hain
payload={"prompt":"hello","max_tokes":50,"temp":.2}
headers= {"Authorization":"Bearer Fake-key"}

post=requests.post(
    "https://httpbin.org/post",
    json=payload,
    headers=headers,
    timeout=10
)
post.raise_for_status()
echoed_data=post.json()
print(echoed_data)


