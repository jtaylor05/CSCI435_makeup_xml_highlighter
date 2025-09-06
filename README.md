### CSCI435 XML+Screenshot Highlighter ###

The attached code was developed using Python 3.12.2 and requires all the dependencies listed in **requirements.txt**. To install the dependencies, navigate to the directory where you cloned this repository and run the following command in your CMD line:
```console
C:\path\to\repo>pip install -r requirements.txt
```

After the computer has installed all dependencies, run the following command to start the program. Make sure that the input is made up of .xml and .png file pairs which share the same name, and provide as an argument the file path to the input
```console
C:\path\to\repo>python3 main.py data\folder
```

After that, the program will return a set of .pngs (one per pair) which share the same name other than **.highlight** added to the end.
