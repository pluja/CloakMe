echo "Setting up a Python virtual environment..."
python3 -m venv venv
source venv/bin/activate
echo "Installing requirements..."
pip3 install -r requirements.txt
echo "Getting Fawkes algorithm binaries..."
wget "https://mirror.cs.uchicago.edu/fawkes/files/fawkes_binary_linux-v0.3.zip"
echo "Preparing the enviroment"
unzip fawkes_binary_linux-v0.3.zip
rm -rf __MACOSX fawkes_binary_linux-v0.3.zip
mv protection-v0.3 fawkes
chmod a+x fawkes
mv fawkes bin/
echo "Running the flask server"
flask run --host 0.0.0.0