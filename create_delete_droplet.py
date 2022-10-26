import requests, os, json

zsh_env_token = os.getenv('token')

droplet_info = '{"name": "Oksana-Droplet", "region": "nyc3", "size": "s-1vcpu-1gb", "image": "ubuntu-20-04-x64"}'

def create_droplets(do_token):
    url = 'https://api.digitalocean.com/v2/droplets'
    two_headers = {"Content-Type": "application/json","Authorization": "Bearer " + do_token}
    response = requests.post(url, headers=two_headers, data=droplet_info)
    resp = response.json()
    return resp


def get_droplets(do_token):
    url = 'https://api.digitalocean.com/v2/droplets'
    two_headers = {"Content-Type": "application/json","Authorization": "Bearer " + do_token}

    response = requests.get(url, headers=two_headers)
    resp = response.json()
    # print(resp['droplets'])
    for droplet in resp['droplets']:
        # print(droplet['id'])
        droplet_id = droplet['id']

    return droplet_id

# print((get_droplets(do_token=zsh_env_token)))

def delete_droplet(do_token):
    droplet_id = get_droplets(do_token=zsh_env_token)
    url = 'https://api.digitalocean.com/v2/droplets/%s' % droplet_id
    two_headers = {"Content-Type": "application/json","Authorization": "Bearer " + do_token}
    response = requests.delete(url, headers=two_headers)
    resp = response.content
    print(resp)

delete_droplet(do_token=zsh_env_token)