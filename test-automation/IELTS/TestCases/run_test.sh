#!/bin/bash

# Define the configurations
CONFIGS=(
    "--browser_name=chrome --device='iPhone X'"
    "--browser_name=chrome --device='Pixel 2'"
    "--browser_name=chrome"
)

# Loop through each configuration and run pytest, ignoring test_login.py and test_suite.py
for CONFIG in "${CONFIGS[@]}"; do
    echo "Running tests with: $CONFIG"
    
    # Construct the pytest command
    COMMAND="pytest -n 5 $CONFIG --ignore=test_login.py --ignore=test_suite.py --disable-warnings > pytest_output.log 2>&1"
    
    # Print the command that will be executed
    echo "Running pytest with options: $COMMAND"
    
    # Execute the command
    eval $COMMAND || echo "Tests failed for: $CONFIG"
done