import requests

Y_DISK_PATH = 'f1'


with open('yd_secret.txt', 'r') as file_object:
    yd_token = file_object.read().strip()

    def get_ya_headers():
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(yd_token)
        }

    def create_dir(Y_DISK_PATH):
        print_res = ''
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = get_ya_headers()
        params = {"path": Y_DISK_PATH, "overwrite": "true"}
        response = requests.put(url, headers=headers, params=params)
        res = response.status_code
        if res == 201:
            print_res = f'{res} Dir created'
        elif res == 409:
            print_res = f'{res} Dir exists'
        return print_res

if __name__ == '__main__':
    res = create_dir(Y_DISK_PATH)
    print(res)
