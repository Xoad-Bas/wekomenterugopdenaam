# RUN THE GAME
   # Virtual environment
   python3 -m venv .venv

   # mac
      source .venv/bin/activate
      export PYTHONPATH=$(pwd)/src 
      which python 
   # windows:
      .venv\Scripts\activate
      $env:PYTHONPATH = "$(pwd)"
      where python

   python3 -m pip install --upgrade pip
   pip3 install -r requirements.txt

   # run game
   python3 run_game.py

   # close virtual environment
   deactivate

