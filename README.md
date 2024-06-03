# Instructions for this project

## First of all you need to install PDM, which is needed for the backend development

Here are official PDM documentations with installation guides:

- https://pdm-project.org/en/latest/
- https://github.com/pdm-project/pdm

As an example we will use Homebrew install method:
1. Install Homebrew package manager for macOS or Linux:
    - https://brew.sh/
2. After the installation check the version via terminal with this command:
    - brew -v
3. Then execute this command in the terminal: 
   - brew install pdm
4. Check the version of PDM with this command:
   - pdm --version

If everything went well, you should be good to go for the next step.

### Set up your virtual environment for the project

After cloning the repository you must create a new branch:

- git checkout -b NAME_OF_YOUR_NEW_BRANCH

After that you need to change to the root directory of the project, which is ./lotto-csbme . 
Then execute this command:
- pdm install

### Important! You must be always on the root directory of the project, before executing pdm commands!

Afterward you need to change your interpreter to ./lotto-csbme/.venv/Scripts/python.exe

Then you should execute the following command:
- pdm sync

### Important! The .env file with a SECRET_KEY=Gq(0ISVBQOzMPUHVF>tJoVe-a3RDP; in it must be created in the root directory.

That should be it. You should be able to work with all the dependencies, which are needed for this project.

## Now you need to install nvm, Node.js and npm, which are needed for the frontend development

Here are official nvm, npm documentations with installation guides:

- https://github.com/nvm-sh/nvm
- https://docs.npmjs.com/downloading-and-installing-node-js-and-npm

As an example we will use Homebrew install method:
1. Install Homebrew package manager for macOS or Linux:
    - https://brew.sh/
2. After the installation check the version via terminal with this command:
    - brew -v
3. Then execute this command in the terminal: 
   - brew install nvm
4. Check the version of nvm with this command:
   - nvm --version
5. Now install Node.js with the help of nvm with this command:
   - nvm install node 
6. Afterward execute the following command:
   - nvm use node
7. Now install npm:
   - npm install -g npm
   - or brew install node (this should install Node.js and npm as well)

If you have some difficulties, try to use some methods from that topic:
- https://stackoverflow.com/questions/33575082/brew-install-npm-npm-command-not-found

## How to start the local backend development server 

You need to change to the backend directory of the project, which is ./lotto-csbme/src/backend . 
Then execute this command:
   - flask run --debug
   - or 
   - python app.py

It will start a local development server on your machine with the default address http://127.0.0.1:5000

Now you should be able to test your backend, for example with the help of Postman:
- https://www.postman.com/downloads/

Postman allows you to test the API with POST, GET, etc. requests. 
It is really useful, highly recommend to try it out!

## How to start the local frontend development server

You need to change to the frontend directory of the project, which is ./lotto-csbme/src/frontend . 
Then execute this command:
   - npm start

It will start a local development server on your machine with the default address http://localhost:3000

It is possible that you will be asked if you want to use another address, because your port 3000 might be already in use.

After that you should be able to navigate through the frontend in the browser and test things out. 

### Important! You should start the local backend development server as well, if you really want to test the whole project out, as the frontend might need the backend logic to properly work.

