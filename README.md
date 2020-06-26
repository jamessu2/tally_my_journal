# tally_my_journal
Tally my actions-of-interest over a given month


## Functionality
This Python script will parse a journal-entry doc for a given month (in a format that I personally write in), by:
	- tallying the number of days I slept well, ate well, meditated, exercised, and read
	- counting the total number of hours that I wasted on Youtube


## Install/Setup
```bash
git clone "https://github.com/jamessu2/tally_my_journal.git"
source tally_journal.sh
```

**Note #1**: You need to go into  *tally_journal.sh* and change the directory path to your own directory path.

**Note #2**: You need to go into  *tally_journal.py* and change the directory path to the `temp.txt` file that is opened.

**Note #3**: The `source tally_journal.sh` command only works if you're in the *tally_my_journal* directory. Also, it only sets `tally` as a Terminal command for the current Terminal session. (You'd need to rerun on every new Terminal session.)

- To have the `tally` command persist, add the *tally_my_journal* directory to `$PATH`, as well as the `source tally_journal.sh` command to *.bash_profile* / *.bashrc* (probably located in your ~ directory).

**Note #4**: You need [**Python 3**](https://www.python.org/downloads/) installed.


## Usage
First, copy the desired journal entry to parse into the `temp.txt` file.

Then, to run the script, type in `tally` from anywhere inside Terminal.


## Future Development Ideas
Next-level functionality:

1. Parse directly from Google Drive
