# TD-Shooter
TD-Shooter is a top down battle royale style game. The point of this game is to use multiple SenseHats to make a large screen to play across.
To play, you need 4+ Raspberry Pis with SenseHats

This is a project my lecturer gave me to experiment with some networking across the Pis. This being my second ever project in Python and being a little rushed, the code isn't the best but it works.

## Controls
Controls can be set in the config but the defaults are:
#### Movement
[W]-[A]-[S]-[D]
#### Shooting
[Space]
#### Change Weapon
[Q]

## Setup
The setup will require a bit of work.
#### Client
* - The client is easy. This is just for displaying, not controlling.
* Open the script.
* Run the script.
* Set the ID (start at 1 for the top left - top to bottom, left to right).
#### Server
* - The server is the easiest to setup.
* Open the script.
* Run the script.
#### Controller
* - The Pi running this will control a player and display the screen.
* Go into the config.py and set the controller ID. For each controller, add 1 to the ID, starting at 1 (script is setup for 4 players)
* Now run the script.
* Set the ID like you would wit the client.
* Ensure a keyboard is plugged in and play.

## Updates
Due to not owning enough Pis to test this at home, it is unlikely this will receive many updates from me. The creating of this was done with VMs and emulators which was difficult at times.
