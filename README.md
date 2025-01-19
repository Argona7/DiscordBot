<a id="readme-top"></a>

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
[![Telegram][telegram-shield]][telegram-url]
[![Python][Python.com]][Python-url]

<h3 align="center">Discord Bot 1.0</h3>
  <p align="center">
    Auto farm level in <a href="https://discord.gg/CEUu4efxg7">Pixel Penguins discord</a>
    <br />
    <a href="https://github.com/Argona7/DiscordBot/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    •
    <a href="https://github.com/Argona7/DiscordBot/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-feature">Key Feature</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#env-management">Env Management</a></li>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#quick-start">Quick Start</a></li>
        <li><a href="#manual-installation">Manual Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#configuration">Account Management</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## About The Project

[![TVerse][product-screenshot]](https://discord.gg/CEUu4efxg7)

An automated script/code made by @Argona7 on [Python 3.11](https://www.python.org/downloads/release/python-3110/) for [Pixel Penguins](https://discord.gg/CEUu4efxg7), built using Playwright. It helps to work with the site directly without using requests. There is proxy support via an `proxy.txt`  file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Key Feature

- Multithreading
- Proxy Binding
- User-Agent Binding
- Auto Account Create
- Auto Text Messages
- Headless mode

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Getting Started

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Env Management

| Settings                        |                                                                                  Description (Usage)                                                                                   |
|---------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| **PATH_TO_PROFILES**            |                                                                Path to the folder where browser profiles will be saved                                                                 |
| **MAX_THREADS**              |                                                 Number of simultaneously running browsers, **it is recommended to set no more than 5**                                                 |
| **USE_PROXY**                     |                                                                         To use proxy when browsers work or not                                                                         |
| **HEADLESS**           | If enabled, browsers will run in the background without visualization, if disabled, browsers will run as normal. **To log into Discord accounts you need to disable the HEADLESS mod** |

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Prerequisites

> [!IMPORTANT]
> Make sure you have only [Python 3.11](https://www.python.org/downloads/release/python-3110/), or you will encounter errors.

**Check the python version before installation**

- Windows OS

  ```sh
  python -v
  ```

- Linux OS
  ```sh
  python3 —version
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Quick Start📚

1. Clone the repo
   ```sh
   git clone https://github.com/Argona7/DiscordBot.git
   ```

2. Edit your .env configuration, tutorial: ([#env-management](#env-management))
3. Run Batch/Bash file according to your operating system.
   - Run (Windows OS)
   ```sh
   run.bat
   ```
   - Run (Linux OS)
   ```sh
   ./run.sh
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Manual Installation

### Windows

1. Clone the repo
   ```sh
   git clone https://github.com/Argona7/DiscordBot.git
   ```
2. Install Environment Variables
   ```sh
   python -m venv venv
   ```
3. Activate Environment Variables
   ```sh
   venv\Scripts\activate
   ```
4. Install Required Package
   ```sh
   pip install -r requirements.txt
   ```
5. Install Browsers
   ```sh
   playwright install
   ```
6. Make .env file available
   ```sh
   copy .env-example .env
   ```
7. Edit .env file, as your will
   ```sh
   notepad .env
   ```
8. Run after all successful steps are done
   ```sh
   python main.py
   ```

### Linux

1. Clone the repo
   ```sh
   git clone https://github.com/Argona7/DiscordBot.git
   ```
2. Install Environment Variables
   ```sh
   python3 -m venv venv
   ```
3. Activate Environment Variables
   ```sh
   source venv/bin/activate
   ```
4. Install Required Package
   ```sh
   pip3 install -r requirements.txt
   ```
5. Install Browsers
   ```sh
   playwright install
   ```
6. Make .env file available
   ```sh
   cp .env-example .env
   ```
7. Edit .env file, as your will
   ```sh
   nano .env
   ```
8. Run after all successful steps are done
   ```sh
   python3 main.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

> [!TIP]
> Edit `.env` file before running script; Checkout ([#env-management](#env-management))

After the script is successfully installed, you will see four options:

1. **Run Bot**
2. **Register profiles**
3. **Register profiles from txt**
4. **Save profiles to spreadsheet**

**You must be a member of the [Pixel Penguins channel](https://discord.gg/CEUu4efxg7) with verification passed!**

First you need to register your accounts, use **Register profiles** to do this
If you use proxy, check ([#configuration](#configuration))
Second you need to run the bot with the **headless mod turned off** to log into discord accounts
After that you can enable the headless mod at your discretion, the script will send messages to the Pixel Penguins Chat



<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Configuration
1. Accounts Setup 🔒

   Once you have registered accounts, arrange their addresses or private keys in `data/farm.txt`
   
   ![image](https://i.ibb.co/w7ybXMn/accounts-farm.png)

2. Proxy Setup 🔒

   Configure your proxies with the *ANY* (socks, http/s, ...) format in `data/proxy.txt` 🌐

   ![Proxy Configuration](https://i.ibb.co/WfXmfhY/proxy-farm.png)


## License

Distributed under the MIT License.
The GNU General Public License is a free, copyleft license for software and other kinds of works.

More Info on [LICENSE](https://github.com/m3taphor/TinyVerse/blob/main/LICENSE) file.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[forks-shield]: https://img.shields.io/github/forks/Argona7/DiscordBot.svg?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0Ij48cGF0aCBkPSJNOC43NSAxOS4yNWEzLjI1IDMuMjUgMCAxIDEgNi41IDAgMy4yNSAzLjI1IDAgMCAxLTYuNSAwWk0xNSA0Ljc1YTMuMjUgMy4yNSAwIDEgMSA2LjUgMCAzLjI1IDMuMjUgMCAwIDEtNi41IDBabS0xMi41IDBhMy4yNSAzLjI1IDAgMSAxIDYuNSAwIDMuMjUgMy4yNSAwIDAgMS02LjUgMFpNNS43NSA2LjVhMS43NSAxLjc1IDAgMSAwLS4wMDEtMy41MDFBMS43NSAxLjc1IDAgMCAwIDUuNzUgNi41Wk0xMiAyMWExLjc1IDEuNzUgMCAxIDAtLjAwMS0zLjUwMUExLjc1IDEuNzUgMCAwIDAgMTIgMjFabTYuMjUtMTQuNWExLjc1IDEuNzUgMCAxIDAtLjAwMS0zLjUwMUExLjc1IDEuNzUgMCAwIDAgMTguMjUgNi41WiIgZmlsbD0iI2ZmZmZmZiIvPjxwYXRoIGQ9Ik02LjUgNy43NXYxQTIuMjUgMi4yNSAwIDAgMCA4Ljc1IDExaDYuNWEyLjI1IDIuMjUgMCAwIDAgMi4yNS0yLjI1di0xSDE5djFhMy43NSAzLjc1IDAgMCAxLTMuNzUgMy43NWgtNi41QTMuNzUgMy43NSAwIDAgMSA1IDguNzV2LTFaIiBmaWxsPSIjZmZmZmZmIi8+PHBhdGggZD0iTTExLjI1IDE2LjI1di01aDEuNXY1aC0xLjVaIiBmaWxsPSIjZmZmZmZmIi8+PC9zdmc+
[forks-url]: https://github.com/Argona7/DiscordBot/network/members
[stars-shield]: https://img.shields.io/github/stars/Argona7/DiscordBot.svg?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij4NCiAgPHBhdGggZD0iTTggLjI1YS43NS43NSAwIDAgMSAuNjczLjQxOGwxLjg4MiAzLjgxNSA0LjIxLjYxMmEuNzUuNzUgMCAwIDEgLjQxNiAxLjI3OWwtMy4wNDYgMi45Ny43MTkgNC4xOTJhLjc1MS43NTEgMCAwIDEtMS4wODguNzkxTDggMTIuMzQ3bC0zLjc2NiAxLjk4YS43NS43NSAwIDAgMS0xLjA4OC0uNzlsLjcyLTQuMTk0TC44MTggNi4zNzRhLjc1Ljc1IDAgMCAxIC40MTYtMS4yOGw0LjIxLS42MTFMNy4zMjcuNjY4QS43NS43NSAwIDAgMSA4IC4yNVptMCAyLjQ0NUw2LjYxNSA1LjVhLjc1Ljc1IDAgMCAxLS41NjQuNDFsLTMuMDk3LjQ1IDIuMjQgMi4xODRhLjc1Ljc1IDAgMCAxIC4yMTYuNjY0bC0uNTI4IDMuMDg0IDIuNzY5LTEuNDU2YS43NS43NSAwIDAgMSAuNjk4IDBsMi43NyAxLjQ1Ni0uNTMtMy4wODRhLjc1Ljc1IDAgMCAxIC4yMTYtLjY2NGwyLjI0LTIuMTgzLTMuMDk2LS40NWEuNzUuNzUgMCAwIDEtLjU2NC0uNDFMOCAyLjY5NFoiIGZpbGw9IiNmZmZmZmYiPjwvcGF0aD4NCjwvc3ZnPg0K
[stars-url]: https://github.com/Argona7/DiscordBot/stargazers
[license-shield]: https://img.shields.io/github/license/Argona7/DiscordBot.svg?style=for-the-badge
[license-url]: https://github.com/Argona7/DiscordBot/blob/main/LICENSE
[telegram-shield]: https://img.shields.io/badge/Telegram-29a9eb?style=for-the-badge&logo=telegram&logoColor=white
[telegram-url]: https://t.me/ArgonaResearch
[product-screenshot]: https://i.ibb.co/nQpckyZ/Discord.png
[Python.com]: https://img.shields.io/badge/python%203.10-3670A0?style=for-the-badge&logo=python&logoColor=ffffff
[Python-url]: https://www.python.org/downloads/release/python-3110/
