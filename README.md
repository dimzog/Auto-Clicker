## Auto-Clicker (for Randomly Spawning Images)

Take a screenshot of your desired image to be clicked and place it under *"img" folder* as *target.png*.

due to limitations of [PyAutoGUI](https://github.com/asweigart/pyautogui). This script only works in **Main Screen** (when using multiple).

On Windows, cmd needs Admin privillages.
#### Required
* Python 3.8

#### Installation
```pip
pip install -r requirements.txt
```

#### Run
```python
python clicker.py --interval 10 --unit min
```

where 

* --unit: unit of time (e.x sec/min/hour)
* --interval: time to wait between each submission

