import json


def install_sort(homebrew_package):
    return homebrew_package['analytics']['365d']


with open('homebrew_packages.json') as f:
    data = json.load(f)

# Top 5 Packages
data.sort(key=install_sort, reverse=True)

top5_packages = json.dumps(data[:5], indent=2)

print(f" Top 5 Homebrew Packages:\n {top5_packages}")


# Top 5 Video Packages
data_video_packages = [item for item in data if 'video' in item['desc']]

data_video_packages.sort(key=install_sort, reverse=True)

top5_video_packages = json.dumps(data_video_packages[:5], indent=2)

print(f" Top 5 Homebrew Video Packages:\n {top5_video_packages}")
