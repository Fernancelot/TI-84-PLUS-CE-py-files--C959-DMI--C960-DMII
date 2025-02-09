# TI-84-PLUS-CE-py-files-C960-DMII

Programmed for the TI-84 Plus CE Python Edition calculator

Programmed on TI-OS (also doubles as TI-Python version) v5.8.1
Works on latest update (as of 02/09/2025) v5.8.2

Transfer files from PC to calc using TI-Connect software and usb A to usb B mini cable for data transfer

TI claims:
Memory Management:
The available memory for the Python experience will be a maximum of 100 Python programs (PY AppVars) or 50K of memory.
The modules that are bundled with the app in this Python release will share the same space with all files.

I deleted the 3 or 4 python files that came pre-installed and from my experience 32 kb was the maximum available for my .py files.
Over 32 kb crashed the calc's python program and the calc had to be reset and programs re-uploaded picking and choosing which ones to stay within 32 kb max.
You can upload and archive some to the 3 MB of flash storage available to the whole calc, but you would have to go back and forth between archiving and unarchiving programs to do this.
It is tedious and impractical.
The programs included here well exceed 32 kb and uploading all of them will crash your calc and require resetting it.
Choose which ones you want on the calc in Windows (file) Explorer, ensure it's under 32 kb, then upload. Change out as needed via TI-Connect

According to TI:
TI-Python is a Python interpreter for the TI-84 Plus CE Python Graphing Calculator that's based on CircuitPython.
CircuitPython is a variant of Python 3 that's designed for teaching coding and working with small microcontrollers. 
The original CircuitPython implementation has been adapted for use by TI.

When coding if using AI assistance, ensure to explicitly state the calc model and TI-OS type and Python version being a variant of CircuitPython, referred to regarding the calc as TI-Python.
Certain coding aspects are different with CircuitPython (coding strings, etc). Reference these files for an example.

Related Info:
https://education.ti.com/html/eguides/stem/innovator-python/EN/content/resources/pdf/v1.5/ti-pyappprgg_v570_en.pdf
https://blog.adafruit.com/2021/06/25/adafruit-interviews-texas-instruments-education-about-python-on-calculators-and-more-ticalculators-ticodes/
https://circuitpython.org/
https://education.ti.com/html/webhelp/eg_ti84pluscepy/uk/content/eg_gsguide/m_apps/apppyfray.HTML#:~:text=TI%2DPython%20is%20based%20on,from%20the%20CE%20OS%20calculations.
