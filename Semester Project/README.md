# Computer Security


<a href="https://github.com/OrangeXR/CSCI-4321-ComputerSecurity/tree/main/Semester%20Project/Milestones/Milestone%201">Milestone 1</a ><br />
<a href="https://github.com/OrangeXR/CSCI-4321-ComputerSecurity/tree/main/Semester%20Project/Milestones/Milestone%202">Milestone 2</a ><br />
<a href="https://github.com/OrangeXR/CSCI-4321-ComputerSecurity/tree/main/Semester%20Project/Milestones/Milestone%203">Milestone 3</a ><br />

=======<br />

<a href="https://github.com/OrangeXR/CSCI-4321-ComputerSecurity/tree/main/Semester%20Project/Blackbird-gui">Blackbird GUI</a>



=======<br />
```
sudo apt update
sudo apt install git
git clone https://github.com/p1ngul1no/blackbird
cd blackbird
pin install -r requirements.txt

sudo apt install python3-pip
sudo apt install python2-venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo apt-get install python3-tk
pip install pillow
```

download and replace:
blackbird.py<br />
blackbird-gui.py<br />
blackbird.png<br />
blackbird_web.py<br />
```
sudo apt install python3-flask

python blackbird_web.py
```

=======<br />
The ending file structure should look as follows:

    .
    ├── blackbird/
    │   ├── assets/
    |   │   ├── app.js
    │   │   └── fonts/
    |   |   |   ├── Montserrat-Bold.ttf
    |   |   |   └── Montserrat-Regular.ttf
    │   │   └── img/
    |   |   |   ├── ai-stars.png
    |   |   |   ├── arrow.png
    |   |   |   ├── blackbir-logo.png
    |   |   |   ├── link.png
    |   |   |   └── warning.png
    │   │   └── text/
    |   |       └── splash.txt
    │   ├── data/
    │   │   ├── email-data.json
    │   │   └── useragents.txt
    │   │   └── wmn-metadata.json
    │   ├── docs/
    │   │   ├── LICENSE
    │   │   ├── README.md
    │   │   ├── SUMMARY.md
    │   │   ├── advanced-usage.md
    │   │   ├── ai.md
    │   │   ├── basic-usage.md
    │   │   ├── getting-started.md
    │   │   └── use-cases.md
    │   ├── src/
    │   │   ├── __init__.py
    │   │   ├── config.py
    │   │   └── modules/
    │   │      ├── ai/
    │   │      |   ├── __init__.py
    |   |      |   ├── client.py
    |   |      |   └── key_manager.py
    │   │      ├── core/
    |   |      |   ├── email.py
    |   |      |   └── username.py
    │   │      ├── export/
    │   │      |   ├── csv.py
    │   │      |   ├── dump.py
    │   │      |   ├── file_operations.py
    │   │      |   ├── json.py
    │   │      |   └──pdf.py
    │   │      ├── sites/
    |   |      |   └── instagram.py
    │   │      ├── utils/
    │   │      |   ├── file_operations.py
    │   │      |   ├── filter.py
    │   │      |   ├── hash.py
    │   │      |   ├── http_clients.py
    │   │      |   ├──input.py
    │   │      |   ├── log.py
    │   │      |   ├── parse.py
    │   │      |   ├── permute.py
    │   │      |   ├── precheck.py
    │   │      |   └──userAgent.py
    │   │      └── whatsmyname/
    |   |          ├── __init__.py
    |   |          └── list_operations.py
    │   └── tests/
    |       ├── test_core.py
    |       ├── test_export.py
    │       └── data/
    │           ├── mock-email.json
    │           └── mock-username.json
    ├── .env
    ├── .gitignore
    ├── Dockerfile
    ├── READMEmd
    ├── blackbird.py
    ├── blackbird.py <---------------- updated for gui
    ├── blackbird_gui.py <------------ gui for the blackbird
    ├── blackbird_web.py <------------ flask integration for blackbird
    └── requirements.txt



