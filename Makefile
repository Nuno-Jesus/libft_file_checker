TARGET = main.py
FLAGS = -B
PY = python3

all:
	git pull
	echo "Searching for updates..."
	$(PY) $(FLAGS) $(TARGET)
