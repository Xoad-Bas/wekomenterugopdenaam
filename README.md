# RUN THE GAME
   # Virtual environment
   python3 -m venv .venv 

   # mac
      source .venv/bin/activate
      export PYTHONPATH=$(pwd)/src 
      which python 
   # windows:
      .\venv\Scripts\activate
      $env:PYTHONPATH = "$(pwd)/src"
      where python

   python3 -m pip install --upgrade pip 
   pip3 install -r requirements.txt

   # run game
   python3 run_game.py

   # close virtual environment
   deactivate

# RAPID FIRE DECISIOPNMS ELLES & BAS
 - TOPDOWN
 - FIGHTS / INTERACT
 - Character always in middle
 - Cosy / horror vibes

 # BACKLOG
 - MOODBOARD
 - Eerste sprite
    Voor / zij/ achter
 - Verhaal grote lijnen presenteren aan broer
 - Map layout maken ( 1600 x 1600 )
    - 1 map
    - Blokjes worden gerenderd binnen ~50 blokjes van character
