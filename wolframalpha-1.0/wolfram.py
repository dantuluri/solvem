import wolframalpha

input = raw_input("Question: ")
app_id = "Q6G3AR-YAQHKRG6LK"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print answer