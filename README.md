# Basics
## Installing python 
If you don't have python already on your system, you will need to install it. Please install python version 3.5 available here: https://www.python.org/downloads/
## Installing required python modules
### Installing using 'pip'
Now that you have python installed, we would like to install additional modules to enable us to use python for computational modeling. 
We recommend installing the python modules needed for this course using "pip" (https://pip.pypa.io/en/stable/quickstart/), which is typically installed alongside python (Windows). Open a terminal, and type: 
```
pip3 install numpy scipy sklearn pandas
# For Ubuntu:
pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.0.1-cp35-cp35m-linux_x86_64.whl
# For Mac:
pip install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.1-py3-none-any.whl
# For Windows
pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow-1.0.1-cp35-cp35m-win_amd64.whl
```
### Troubleshooting: Try installing each module separately
#### matplotlib
 http://matplotlib.org/1.3.1/users/installing.html
#### pandas
http://pandas.pydata.org/pandas-docs/stable/install.html
#### scikit-learn
http://scikit-learn.org/stable/install.html
#### tensorflow
https://www.tensorflow.org/install/ 
Make sure to install the CPU version of tensorflow, as all course examples are relatively compute-friendly (small datasets, models with relatively few parameters). Using the native "pip" installation is easiest and recommended. 
