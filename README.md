# CABLE setup

Repository to setup a svn development branch for the first time.

The code will: (i) check out and (ii) build the code. There is also a minimal
example to test the code works at Tumbarumba.

To work, the expectation is that the user will update the relevant entries (paths, library locations, etc) within:

    $ initial_setup.py

    #------------- User set stuff ------------- #
    user = "XXX579"

    ...
    # ------------------------------------------- #

In many cases we recommend you don't change the defaults, e.g. (however things **should** be robust to you doing as you please)

    src_dir = "src"
    run_dir = "runs"
    log_dir = "logs"
    plot_dir = "plots"


## Code dependencies

The code has been written such that it has very few dependancies to ease personal set up. Nevertheless, it does depend on a few fairly standard python libraries:

* [numpy](http://numpy.scipy.org/)
* [pandas](https://pandas.pydata.org/)
* [xarray](http://xarray.pydata.org/en/stable/)

All of which can be easily built using [anaconda](https://www.anaconda.com/distribution/).

To install on raijin in your personal space:

Download [the linux anaconda file](https://www.anaconda.com/download/#linux). Then create an environment called "science" (or whatever sensible name springs to mind).

    $ conda create --name science python=3

then

    $ source activate science

then

    $ conda install xarray matplotlib pandas scipy numpy

If you're working locally on a mac or linux machine, you could as easily use your favourite package manager (e.g. macports, apt-get, etc).

## Contacts
* [Martin De Kauwe](http://mdekauwe.github.io/)
