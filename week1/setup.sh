#!bin/bash
echo "setting up....."

mkdir -p my app
echo "folder created"

echo "Hello from my app" > myapp/readme.txt
echo "file created"

echo "setup complete"
echo "Here is what was created"
ls -l myapp
