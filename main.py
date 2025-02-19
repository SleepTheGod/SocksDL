import requests
import zipfile
import os

# List of proxy URLs
urls = [
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
    "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt",
    "https://api.openproxylist.xyz/socks5.txt",
    "https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/BlackSnowDot/proxylist-update-every-minute/main/socks.txt",
    "https://proxyspace.pro/socks5.txt",
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true",
    "http://worm.rip/socks5.txt",
    "http://www.socks24.org/feeds/posts/default",
    "https://www.proxy-list.download/api/v1/get?type=socks5",
    "https://www.proxyscan.io/download?type=socks5",
    "https://www.my-proxy.com/free-socks-5-proxy.html"
]

# Function to download proxy list
def download_proxies(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None

# Function to save proxies to a zip file
def save_to_zip(proxies, filename, zipfile_name):
    with zipfile.ZipFile(zipfile_name, 'a') as zipf:
        zipf.writestr(filename, proxies)

# Main function to download from all URLs and save to zip
def main():
    zipfile_name = "socks.zip"
    for url in urls:
        print(f"Downloading proxies from {url}...")
        proxies = download_proxies(url)
        if proxies:
            # Create a filename for each proxy list based on URL
            filename = url.split('/')[-2] + '.txt'
            save_to_zip(proxies, filename, zipfile_name)
            print(f"Proxies from {url} saved as {filename} inside {zipfile_name}")
        else:
            print(f"Skipping {url} due to errors.")

if __name__ == "__main__":
    main()
