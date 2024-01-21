<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- ABOUT THE PROJECT -->
## About The Project

[![QA Website Screen Shot][website-screenshot]](https://github.com/AlexKraken/warehousing-scripts)

These are scripts used to make QA's job a little easier. They started out as scripts to be used from the terminal and Python's interactive shell, but now include a website for those more comfortable with a web browser - demo (hosted freely on pythonanywhere.com and may need a minute to start up) located here: [https://alexkraken.pythonanywhere.com/](https://alexkraken.pythonanywhere.com/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
You should already have Python installed, check by opening the terminal and running
```sh
python --version
```

### Installation
1. Clone the repo (or alternatively download as a .zip file) and change to the directory in the terminal
   ```sh
   git clone https://github.com/AlexKraken/warehousing-scripts.git
   cd warehousing-scripts
   ```
   
   
2. To start the Barcode Logger
   ```sh
   python run_logger.py
   ```
   
3. To use the weight checker (will need to be in a seperate terminal if you're already running the Barcode Logger)
   ```sh
   > python
   Python 3.11.3 
   >>>
   >>> from check_weight import check
   >>> check()
   ```
   To exit use
   ```sh
   >>> exit()
   ```
   
5. To use the website (will also need to be in a seperate terminal and in the `warehousing-scripts` directory)
   
   1. Create a python virtual environment
      ```sh
      python -m venv venv
      ```
      
   2. Enable the virtual environment
      ```sh
      source venv/bin/activate
      ```
      
   3. Install all the required packages
      ```sh
      pip install --requirement qa-flask-website/requirements.txt
      ```
      
   4. Start the server for the Flask app
      ```sh
      python qa-flask-website/main.py
      ```
      
   5. In the terminal output there should be a line
      ```sh
      * Running on http://127.0.0.1:5000
      ```
      
      Enter `http://127.0.0.1:5000` in a web browser to access the website (don't exit out of that terminal!)
      
   7. When finished, stop the server in the terminal by pressing `CRTL + C`, and deactivate the virtual environment by typing
      ```sh
      deactivate
      ```
      
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Barcode Logger
This is useful for quickly checking whether or not a particular item has been logged before. Since any changes to a item's specifications won't be in effect until the next day, this log is useful for catching errors that have already been fixed but will still be flagged until the system updates.

Run from the terminal - when prompted, enter the name of an existing log file to import previously logged barcodes, or enter a name for a new file:

    > python run_logger.py
    Enter log file name: barcodes.csv
    File not found, create a new file? [y/n]: y

The program will prompt with options:

    Available commands [add/check/exit]: 

    - - -

    add:
        Use to add a new barcode to the log. Returns 'LOG SUCCESSFUL' if it was not
        previously entered, else returns 'ALREADY LOGGED'.

    check:
        Use to check if a barcode has already been logged. Returns 'BARCODE FOUND'
        if it was previously entered, else returns 'NOT FOUND'. This will continue
        prompting for another barcode until the user enters 'exit'.

    exit:
        Use to exit the program and return to the command line.


### Weight Checker
This allows for quickly checking how far off the system's entry on an item's weight is from the actual amount. 

For now, this script is meant to be used from Python's interactive shell to complement the other calculations that are commonly used:

    > python
    Python 3.11.3 
    >>>
    >>> from check_weight import check
    >>> check()


##### Example:
Suppose an item's weight is measured to be 0.1 lbs, and the system has the weight as 1 lb. While in Python's interactive shell, run:

    >>> check()
    Enter the expected weight (in lbs): 1
    Enter the measured weight (in lbs): 0.1
    -----
    Absolute error:   0.90 lbs
    Percentage error: 900%


#### The Math
For fixing incorrect weights in the system, percentage error is defined as:
```math
\text{Percentage Error} = \frac{{\text{Expected Weight} - \text{Measured Weight}}}{{\text{Measured Weight}}} \times 100\%
```


##### Example:
Suppose an item's weight is measured to be 0.25 lbs but the system expects the item's weight to be 1.50 lbs.

```math
\text{Percentage Error} = \frac{{1.50 - 0.25}}{{0.25}} \times 100\% = 500\%
```

A 500% error means the system's expectation is 5 times OVER the actual weight, suggesting that the previous measurement could have been made on a case pack of 6 units, or the current item was mistakenly taken out of a case pack.


##### Example:
Suppose a case pack of 10 items is measured to be 1.20 lbs but the system expects the case pack to weigh 0.12 lbs.

```math
\text{Percentage Error} = \frac{{0.12 - 1.20}}{{0.12}} \times 100\% = -900\%
```

A -900% error means the system's expectation is 9 times UNDER the measured weight, which suggests that either the case pack isn't how the item should be sold, or that the previous measurement was made by mistakenly taking an item out of its case pack.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap
For the website version:
- [ ] Add ability to download barcode log as a .cvs file
- [ ] Add color highlighting to messages
- [ ] Add alternating colors to barcode log
- [ ] Add ability to populate 'Barcode Logger' with info from 'Weight Checker'

See the [open issues](https://github.com/AlexKraken/warehousing-scripts/issues) for a full list of proposed features (and known issues).


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

### Built With
* [![Flask][Flask]][flask-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

#### Other helpful resources!
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Img Shields](https://shields.io)
* [PythonAnywhere](https://www.pythonanywhere.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://flask.palletsprojects.com/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[website-screenshot]: images/screenshot.png
