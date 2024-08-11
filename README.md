# What this project do?
This project simplely browse a given page from instagram and:

- Give it a like.

- May send a coment if previously specified.

- The program automatcaly rerun 24hrs after the "end" of each run.

- Making that a "infinit" loop until you shutdown the program.

# How it works
- Run the program using the line: 
```python ./app.py```

- Then the program need 4 informations to run. And they are:

    - The user of a instagram acount
    - The password
    - The target account
    - A coment (if you dont want to coment just left this camp empty)
- OBS:
```The program DOES NOT store ANY users information```

- After this, the automation process is started.

- And when it is done, the program takes a break of 24 hrs to finally rerun the 
automation process

# Technical informations
- The main technologi used in this project is
Selenium 4

- Has "wait strategys" when searching for elements. That makes the automation
harder to break.

- "Wait strategys" also make the program adaptable to your computer perform

    - It basically means: The faster your PC is, faster the program do his things

# Why use this program
- The program can be usefull if you want to follow constantly a single instagram page

- Can be easily incremented with a VPS service

# Dependences

- To know all the dependences to this project you can:
    - Take a loak to the module called:
    ```requirements.txt```
    - Or you can simplely install all them by runing the line:
    ```pip install -r requirements.txt```