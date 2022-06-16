import http.client
import json

conn = http.client.HTTPSConnection("127.0.0.1", 8081)
payload = json.dumps({
  "ime": "Andjela",
  "prezime": "Preocanin",
  "username": "apreocanin2218RI",
  "smer": "RI",
  "predmeti": [
    {
      "ime": "Bezbednost mreza",
      "espb": "6"
    },
    {
      "ime": "Data centar infrastruktura",
      "espb": "6"
    },
    {
      "ime": "Racunarske mreze velikih sistema",
      "espb": "6"
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/users", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))