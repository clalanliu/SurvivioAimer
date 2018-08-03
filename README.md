# SurvivioAimer

> A concise Surviv.io aim assist based on image processing.

**Key features:**

* Resist to Surviv.io updates.
* Dynamical adjustion for detecting radius of enimes.

**Steps:**  

* Install necessary packages first (python3.5 needed):  
  ```bash
	pip install numpy pillow scikit-image keyboard pyautogui matplotlib
	```

* To run the program:
  ```bash
	python SurvivioAimer.pyw
	```

* To build the executable file:
  ```bash
	pyinstaller -F SurvivioAimer.pyw
	```

**Usage:**
* Z/z: Turn on/off SurvivioAimer, and it will turn off/on until next pressing.
* O/o: Reset the radius of enimes to appropriately. (Please do this after changing the scope every time.) 
* Shift without releasing: Turn on SurvivioAimer temporarily.
* Ctrl + C: Exit.


