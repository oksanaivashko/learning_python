import json, requests

token = 'token'
url = 'https://api.digitalocean.com/v2/droplets'
two_headers = {"Content-Type": "application/json","Authorization": "Bearer " + token}
create_droplet = '{"name": "example.com", "region": "nyc3", "size": "s-1vcpu-1gb", "image": "ubuntu-20-04-x64"}'
response = requests.post(url, headers=two_headers, data=create_droplet)
print(response)