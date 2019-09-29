EasyTorHiddenServicePython
====================================

EasyTorHiddenServicePython is a project to run a simple Python webserver to serve files on the darknet. The project was written and tested in Python 3.7.4.

[![Build status](https://ci.appveyor.com/api/projects/status/of7tpw39qss9qpb8?svg=true)](https://ci.appveyor.com/project/SeppPenner/easytorhiddenservicepython)
[![GitHub issues](https://img.shields.io/github/issues/SeppPenner/EasyTorHiddenServicePython.svg)](https://github.com/SeppPenner/EasyTorHiddenServicePython/issues)
[![GitHub forks](https://img.shields.io/github/forks/SeppPenner/EasyTorHiddenServicePython.svg)](https://github.com/SeppPenner/EasyTorHiddenServicePython/network)
[![GitHub stars](https://img.shields.io/github/stars/SeppPenner/EasyTorHiddenServicePython.svg)](https://github.com/SeppPenner/EasyTorHiddenServicePython/stargazers)
[![GitHub license](https://img.shields.io/badge/license-AGPL-blue.svg)](https://raw.githubusercontent.com/SeppPenner/EasyTorHiddenServicePython/master/License.txt)
[![Known Vulnerabilities](https://snyk.io/test/github/SeppPenner/EasyTorHiddenServicePython/badge.svg)](https://snyk.io/test/github/SeppPenner/EasyTorHiddenServicePython) 

## Setup:
1. Clone this project to a directory, e.g. /home/{username}/hidden-service/.
2. Install Python and Tor using e.g.

```bash
sudo apt-get install tor python3-pip python-pip
```

3. Install all required pip package dependencies with:

```bash
pip install -r requirements.txt
```

4. Add

```bash
HiddenServiceDir /home/{username}/hidden-service/
HiddenServicePort 80 127.0.0.1:8000
```
to the `/etc/tor/torrc` file (Change the directory of course) using

```bash
nano /etc/tor/torrc
```

5. Set the execute flags:

```bash
chmod +x install.sh
chmod +x run.sh
chmod +x restartTor.sh
chmod +x startTor.sh
chmod +x stopTor.sh
chmod +x statusTor.sh
```

6. Set the rights to the directory properly:

```bash
chmod 700 /home/{username}/hidden-service/
```

7. Add files to the web subfolder of your service to serve them.
8. Restart tor using

```bash
sudo service tor restart
```

9. Get your tor hostname from your service directory:

```bash
cat /home/{username}/hidden-service/hostname
```

10. Check that your firewall(s) do not block incoming traffic.
11. Access your hidden service over the hostname with the [Tor Browser](https://www.torproject.org/projects/torbrowser.html)

## Further Links:
* https://github.com/whackashoe/tor-hidden-service-setup/blob/master/setting-up-webserver.md
* https://github.com/whackashoe/tor-hidden-service-setup
* https://jordan-wright.com/blog/2014/10/06/creating-tor-hidden-services-with-python/
* https://robindoherty.com/tor/hidden-service.html
* https://robindoherty.com/tor/fancy-dot-onion.html
* https://stackoverflow.com/questions/7943751/what-is-the-python-3-equivalent-of-python-m-simplehttpserver

Change history
--------------

* **Version 1.0.0.1 (2019-09-29)** : Moved to Python3 "http.server".
* **Version 1.0.0.0 (2019-01-06)** : 1.0 release.