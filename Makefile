TARGET = main.py
FLAGS = -B
PY = python3

all:
  echo "Searching for updates..."
	git pull
	sleep 1
  $(PY) $(FLAGS) $(TARGET)