# volumiolcd
Simple display for Volumio using LCD1602A I2C module

Using LCD library from https://github.com/mongonta0716/hd44780

To install add line to /etc/rc.local before `exit 0`

`/home/volumio/volumiolcd/venv/bin/python /home/volumio/volumiolcd/screen.py`

Adjust the paths to match your installation

To use the python virtual environment from the repository make sure that the VIRTUAL_ENV variable in `venv/bin/activate` is matching actual path.


## Disclaimer:

This is not using a preferred plugin management system as I am not crazy enough to use JS and npm. It actually blocks Volumio automatic update system. Use with caution.