# Source this.
# Setup virtualenv

sudo apt-get install -y \
    python-pip \
    build-essential \
    git \
    python \
    python-dev

sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 

if [ ! -d venv ]
then
  virtualenv venv
fi

. venv/bin/activate

sudo apt-get install python-tk


#pip install numpy
# To deactivate the venv, use
#
# $ deactivate
#
# as a command on the command line.
# To set up the venv again, then type
#
# $ source setup.sh
