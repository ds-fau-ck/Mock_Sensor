# Mock_Sensor
#  Step 01 Create a conda environment
```
conda create --prefix ./env python=3.8 -y

```
# Step 02 Activate the conda environment
```
source activate ./env

```
# Step 03 Install all the requirments
```
pip install -r requirements.txt

```
# Step 04 Run the program
```
-- Before run the program change the username, password and database name according to your db configuration in db.py file.
python datarecorder.py 
python datavisualizer.py 

```
