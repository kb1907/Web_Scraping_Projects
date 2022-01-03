import requests
import json

response = requests.get('https://formulae.brew.sh/api/formula.json')

homebrew_packages_json = response.json()

results = []

for homebrew_package in homebrew_packages_json:
    homebrew_package_name = homebrew_package['name']
    homebrew_package_desc = homebrew_package['desc']
    homebrew_package_url = f'https://formulae.brew.sh/api/formula/{homebrew_package_name}.json'

    r = requests.get(homebrew_package_url)
    homebrew_package_json = r.json()

    try:
        installs_30 = homebrew_package_json["analytics"]["install_on_request"]["30d"][homebrew_package_name]
        installs_90 = homebrew_package_json["analytics"]["install_on_request"]["90d"][homebrew_package_name]
        installs_365 = homebrew_package_json["analytics"]["install_on_request"]["365d"][homebrew_package_name]

        data = {'name': homebrew_package_name,
                'desc': homebrew_package_desc,
                'analytics': {
                    '30d': installs_30,
                    '90d': installs_90,
                    '365d': installs_365
                }
                }
    except Exception as e:
        pass

    results.append(data)


with open("homebrew_package_info.json", 'w') as f:
    json.dump(results, f, indent=2)
