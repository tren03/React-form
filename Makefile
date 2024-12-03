# Makefile for checking and managing React app and Python server

.PHONY: start_servers stop_servers restart_servers check_react check_python

# Check if the React app is running
check_react:
	@echo "Checking if React is running..."
	@lsof -i :3000 > /dev/null && echo "React is running" || echo "React is not running"

# Check if the Python server is running
check_python:
	@echo "Checking if Python server is running..."
	@lsof -i :8000 > /dev/null && echo "Python server is running" || echo "Python server is not running"

# Stop the React app (if running)
stop_react:
	@echo "Stopping React..."
	@lsof -i :3000 | grep "LISTEN" | awk '{print $$2}' | xargs kill -9

# Stop the Python server (if running)
stop_python:
	@echo "Stopping Python server..."
	@lsof -i :8000 | grep "LISTEN" | awk '{print $$2}' | xargs kill -9

# Start the React app
start_react:
	@echo "Starting React app..."
	@npm start --prefix ./ &  # Adjust this to your React app's directory

# Start the Python server (FastAPI/Flask)
start_python:
	@echo "Starting Python server..."
	@uvicorn backend.main:app --reload  # Adjust this for FastAPI
	# Or, if you use Flask:
	# @flask run --host=0.0.0.0 --port=8000

# Restart both servers
restart: stop start

stop: stop_react stop_python

start: start_react start_python

