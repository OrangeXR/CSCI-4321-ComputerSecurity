# Computer Security


[Installation](#Installation)</a ><br />
[File Structure](#FileStructure)</a ><br />
[Commands](#Commands)</a ><br />

=======<br />



    ▄▄▄▄    ██▓    ▄▄▄       ▄████▄   ██ ▄█▀ ▄▄▄▄    ██▓ ██▀███  ▓█████▄ 
    ▓█████▄ ▓██▒   ▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█████▄ ▓██▒▓██ ▒ ██▒▒██▀ ██▌
    ▒██▒ ▄██▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒██▒ ▄██▒██▒▓██ ░▄█ ▒░██   █▌
    ▒██░█▀  ▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒██░█▀  ░██░▒██▀▀█▄  ░▓█▄   ▌
    ░▓█  ▀█▓░██████▒▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▓█  ▀█▓░██░░██▓ ▒██▒░▒████▓ 
    ░▒▓███▀▒░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▒▓███▀▒░▓  ░ ▒▓ ░▒▓░ ▒▒▓  ▒ 
    ▒░▒   ░ ░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░▒░▒   ░  ▒ ░  ░▒ ░ ▒░ ░ ▒  ▒ 
    ░    ░   ░ ░    ░   ▒   ░        ░ ░░ ░  ░    ░  ▒ ░  ░░   ░  ░ ░  ░ 
    ░          ░  ░     ░  ░░ ░      ░  ░    ░       ░     ░        ░    
        ░                  ░                     ░               ░      

The Blackbird github repository, by p1ngul1n0, can be found <a href="https://github.com/p1ngul1n0/blackbird">here</a> <br>


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

download and replace:<br />
<a href="https://github.com/OrangeXR/CSCI-4321-ComputerSecurity/blob/main/Semester%20Project/blackbird.py">blackbird.py</a><br />
<a href="https://github.com/OrangeXR/CSCI-4321-ComputerSecurity/blob/main/Semester%20Project/blackbird-gui.py">blackbird-gui.py</a><br />
<a href="https://github.com/OrangeXR/CSCI-4321-ComputerSecurity/blob/main/Semester%20Project/blackbird.png">blackbird.png</a><br />
<a href="https://github.com/OrangeXR/CSCI-4321-ComputerSecurity/blob/main/Semester%20Project/blackbird_web.py">blackbird_web.py</a><br />
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
    ├── blackbird.png <---------------- background image for gui
    ├── blackbird.py <---------------- updated for gui
    ├── blackbird_gui.py <------------ gui for the blackbird
    ├── blackbird_web.py <------------ flask integration for blackbird
    └── requirements.txt




```
_____/\\\\\\\\\\\\__/\\\________/\\\__/\\\\\\\\\\\_        
 ___/\\\//////////__\/\\\_______\/\\\_\/////\\\///__       
  __/\\\_____________\/\\\_______\/\\\_____\/\\\_____      
   _\/\\\____/\\\\\\\_\/\\\_______\/\\\_____\/\\\_____     
    _\/\\\___\/////\\\_\/\\\_______\/\\\_____\/\\\_____    
     _\/\\\_______\/\\\_\/\\\_______\/\\\_____\/\\\_____   
      _\/\\\_______\/\\\_\//\\\______/\\\______\/\\\_____  
       _\//\\\\\\\\\\\\/___\///\\\\\\\\\/____/\\\\\\\\\\\_ 
        __\////////////_______\/////////_____\///////////__
```



The filter usage for the most part is the same as the original Blackbird app

Including:<br>
- Properties<br>
    ```name``` Name of the site being checked.<br>
    ```cat``` Category of the site.<br>
    ```uri_check``` The URL used to check for the existence of an account.<br>
    ```e_code``` Expected HTTP status code when an account exists.<br>
    ```e_string``` A string expected in the response when an account exists.<br>
    ```m_string``` A string expected in the response when an account does not exist.<br>
    ```m_code``` Expected HTTP status code when an account does not exist.<br>
- Operators<br>
    ```=``` Equal to<br>
    ```~``` Contains<br>
    ```>``` Greater than<br>
    ```<``` Less than<br>
    ```>=``` Greater than or equal to<br>
    ```<=``` Less than or equal to<br>
    ```!=``` Not equal to<br>
- Usage<br>
    ``` name~JohnDoe``` filter by name containing "JohnDoe"<br>
    ``` site=Twitter ``` Filter by site "Twitter"<br>
    ``` cat=social and name~JohnDoe ``` filter by category "Social" and name containing "JohnDoe"<br><br>
- Categories<br>
   ```archived```<br>
   ```art```<br>
   ```blog```<br>
   ```business```<br>
   ```coding```<br>
   ```dating```<br>
   ```finance```<br>
   ```gaming```<br>
   ```health```<br>
   ```hobby```<br>
   ```images```<br>
   ```misc```<br>
   ```music```<br>
   ```news```<br>
   ```political```<br>
   ```search```<br>
   ```shopping```<br>
   ```social```<br>
   ```tech```<br>
   ```video```<br>
   ```xx NSFW xx```<br><br>
  more usage instructions are found <a href="https://github.com/p1ngul1n0/blackbird/blob/main/docs/advanced-usage.md">here</a>



