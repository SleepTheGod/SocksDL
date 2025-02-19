SocksDL

SocksDL is a Python script that downloads SOCKS5 proxy lists from various online sources and stores them in a ZIP file. Each proxy list is saved as a separate .txt file within the ZIP archive. This script is useful for users looking to gather and manage SOCKS5 proxies for various applications.

Features:
- Downloads SOCKS5 proxies from multiple URLs.
- Saves proxies in a ZIP file called socks.zip.
- Each proxy list is saved as a separate .txt file inside the ZIP.
- Automatically handles errors and skips failed URLs.

Installation:
1. Clone this repository to your local machine:

   git clone https://github.com/SleepTheGod/SocksDL.git
   cd SocksDL

2. Install the required Python dependencies using pip:

   pip install -r requirements.txt

Usage:
1. Run the script main.py to start downloading the proxy lists:

   python main.py

2. The script will download the proxies from the URLs listed in the script and save them in a ZIP file called socks.zip.

   - Each proxy list will be saved as a .txt file within the ZIP archive.
   - If any URL fails to provide proxies, the script will skip it and continue with the others.

Contributing:
Feel free to fork this project, submit issues, or create pull requests. Contributions are welcome!

License:
This project is licensed under the MIT License - see the LICENSE file for details.

Author:
SleepTheGod (https://github.com/SleepTheGod)
