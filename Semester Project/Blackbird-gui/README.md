
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
All requirements for Blackbird
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

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


For the gui you'll need to install tkinter<br />
```sudo apt-get install python3-tk```




Save the blackbird image as "blackbird.png" in the same folder as blackbird-gui.py<br>
install Pillow if you haven't already:<br>
``` pip install pillow ```


![image](https://github.com/user-attachments/assets/9a3a0df3-de76-4c27-a1d9-efc42b85c5db)




The filter usage for the most part is the same as the original Blackbird app

Including:<br>
- Properties<br>
    ```name```  Name of the site being checked.<br>
    ```cat```  Category of the site.<br>
    ```uri_check```  The URL used to check for the existence of an account.<br>
    ```e_code```  Expected HTTP status code when an account exists.<br>
    ```e_string```  A string expected in the response when an account exists.<br>
    ```m_string```  A string expected in the response when an account does not exist.<br>
    ```m_code```  Expected HTTP status code when an account does not exist.<br>
- Operators<br>
    ```=``` Equal to<br>
    ```~``` Contains<br>
    ```>``` Greater than<br>
    ```<``` Less than<br>
    ```>=``` Greater than or equal to<br>
    ```<=``` Less than or equal to<br>
    ```!=``` Not equal to<br>
- Usage
    ``` name~JohnDoe```<br> filter by name containing "JohnDoe"
    ``` site=Twitter ```<br> Filter by site "Twitter"
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
