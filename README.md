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

## Weapons
There are three weapons you can toggle through with [Q].
#### Machine Gun
* The machine gun is a rapid fire gun that has short range and lacks accuracy.
#### Sniper
* The sniper is a gun with huge range and perfect accuracy but a slow rate of fire.
#### Crowbar
* The crowbar is a melee weapon that hit at both points in front of you.

## Reloading
* All weapons but the crowbar have a limited rate of fire or reload time.
* The reload is indicated by part of the weapon darkening. When it lights back up, you are ready to fire.
* You can also hold the fire key down to fire as soon as you are ready to do so.

## Obstacles
* Obstacles will randomly spawn when generating the map or when you kill a player.
* These obstacles can be destroyed with any weapon - the crowbar's speciality.

## Blue Zone
* Avoid the Blue Zone at all costs... It means certain death!

## Player Damage
* The player's color is the only part that receives damage, not their gun.

## Setup
The setup will require a bit of work.
#### Server
- The server is the easiest to setup.
* Open the script.
* Run the script.
#### Client
- The client is easy. This is just for displaying, not controlling.
* Make sure the config.py HOST address is set to your server's IP.
* Open the script.
* Run the script.
* Set the ID (start at 1 for the top left - top to bottom, left to right).
#### Controller
- The Pi running this will control a player and display the screen.
* Make sure the config.py HOST address is set to your server's IP.
* Now run the script from the terminal (controller needs the terminal).
* Set the ID like you would with the client.
* Set the Controller ID the same as above. For each controller, add 1 to the ID, starting at 1 (script is setup for 4 players)
* Ensure a keyboard is plugged in and play.

## Updates
Due to not owning enough Pis to test this at home, it is unlikely this will receive many updates from me. The creating of this was done with VMs and emulators which was difficult at times.

## Issues
#### Can't move
* Ensure caps lock is off.
* Make sure you are focused on the terminal to control the player.
* Check your HOST address is set to your server's IP in config.py
#### Not displaying correctly
* Make sure to set all IDs correctly
* Do not use the server as a client or controller at the same time