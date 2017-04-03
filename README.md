# Basics
## Installing python
If you don't have python already on your system, you will need to install it. Please install python version 3.5 available here: https://www.python.org/downloads/
## Installing required python modules
### Installing using requirements.txt
Now that you have python installed, we would like to install additional modules to enable us to use python for computational modeling. 
We recommend installing the python modules needed for this course using "pip" (https://pip.pypa.io/en/stable/quickstart/), which is installed during python installation. First, download this repository by clicking on the green button on the top right of this page. When finished downloading, extract the contents of the file to your home directory. Finally, open a terminal, and type: 
```
cd Basics-master 
pip install -r requirements.txt
```
### Installing each module separately
#### matplotlib
 http://matplotlib.org/1.3.1/users/installing.html
#### pandas
http://pandas.pydata.org/pandas-docs/stable/install.html
#### scikit-learn
http://scikit-learn.org/stable/install.html
#### tensorflow
https://www.tensorflow.org/install/ 
Make sure to install the CPU version of tensorflow, as all course examples are relatively compute-friendly (small datasets, models with relatively few parameters). Using the native "pip" installation is easiest and recommended. 
