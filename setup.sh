echo installing all dependencies...
pip3 install -r requirements.txt

# shellcheck disable=SC2181
if [ $? -eq 0 ]
then
  echo dependencies installed, running python project...
  python main.py
fi
