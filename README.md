# CloakMe
<p align="center"> <img width="150" src="image.png"> </img></p> 
<p align="center"> Cloak your face from Big Brother </p>
<br>

CloakMe is a web interface implementation of the [Fawkes](https://github.com/Shawn-Shan/fawkes) algorithm developed by researchers at SANDLab, University of Chicago. You can check out more information on their [website](http://sandlab.cs.uchicago.edu/fawkes/#code).


<h1 align="center"> Installation </h1>

#### Pre-installation
You will need to install `python3.7` (version must be <3.8), `python3 pip` and `git`.

#### Quick Installation (Linux Only)
1. Clone this repository:

`git clone https://github.com/pluja/CloakMe`

2. Change permissions and run setup file:

`chmod a+x setup.sh`

`./setup.sh`

#### Manual Installation
1. Clone this repository:

`git clone https://github.com/pluja/CloakMe`

2. Move into the directory:

`cd CloakMe`

3. Create a virtual environment:

`python3 -m venv venv`

4. Activate it:

`source venv/bin/activate`

5. Install requirements:

`python3 -m pip install -r requirements.txt`

6. Run the flask server:

`flask run --host 0.0.0.0`

7. Open the url and enjoy: [URL](http://127.0.0.0:5000)
