# Battleshipasaurus

Battleshipasaurus is a Battleship game created using **Python**, and runs on a mock terminal on Heroku.

:point_right: [Live Project](https://battleshipasaurus.herokuapp.com/)

## Instructions

The aim of the game is to sink the enemies battleships:

- If they correctly guess all the ships on the board they win

- If they don't hit all the ships within the number of turn they lose the game

## Features

- One player game

-

### Future Features

- User to play against the computer

- Custom grid size

- Increased game difficulty

- Option to add different types of ships like the Carrier, Cruiser, Submarine etc.

## Data Model

Game is made using python functions

## Testing

### Bugs

- Game start prompt will not start the game loop if too many gaps are typed in the console.

#### Solved bugs

- Fix bug where value entered in terminal did not match the board index.

- Fix bug where console with give valueError when game is run for the first time

- Fix bug where game over prompt was not being triggered at the end of game loop

#### Unfixed bugs

- unfixed bugs description

#### Validator testing

- PEP8
  - errors found or not found

## Deployment

Game was deployed using [Heroku](https://www.heroku.com/)

- In your vscode or gitpod terminal inside your current worskspace:
  type in:
  - `touch requirements.txt`
  - `pip3 freeze > requirements.txt`

This is to add dependencies to your deployed project

- To deploy this project you need a Heroku account

- Once logged in, click the CREATE NEW APP button

- Add a unique name for your project in lowercase and spaces separated by '-' the create new app

- Click on the settings page and add the Python THEN the Node.js build packs

- Go to the Deploy tab

- Connect your GitHub account and select the 'main' brach of your project

- Near the bottom on the page, you have two options on how to deploy your project. You can either do:

  - Automatic Deployment which will deploy your project after every change to your main github repository
  - Manual Deployment where the user has to prompt for the deployment.

- Which ever option you decide you have to do an initial Manual deployment to Heroku for the first upload.

- The app will install the necessary files and dependencies. Finally, a message was displayed: 'Your app was successfully deployed.'

## Credits

- [Codeacademy Python 2: Lists and Functions](https://www.codecademy.com/courses/learn-python/lessons/battleship)
- [ASCII table](http://sticksandstones.kstrom.com/appen.html)
- [Alphabet string](https://www.kite.com/python/answers/how-to-make-a-list-of-the-alphabet-in-python)
