# 42-tool

## Description

This tool was developed to help **42** students to speed up boring checkings like missing files or wrong function prototypes in the first project of the Common Core, **libft**. At the time of the first launch (November 11th, 2022), the tool was built using the most up-to-date version of the subject found so far on intra.

## This is great, you mind if I use your code?

**You are free to fork the repository and study/modify/test the code on your own**. However, I would really appreciate it if you could text me on Slack (**ncarvalh**) whenever you find a bug or you have a suggestion, so I can properly introduce hotfixes or deploy some quality-of-life patches that can benefit the 42 community in general.

## Is there any software required?
> If you're planning on running the tool in the 42 clusters, you can skip this section. 

In order to correctly execute the tool, you must:
- have [Python](https://www.python.org/downloads/) installed;
- have either [Ubuntu](https://ubuntu.com/download) or [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) on your computer;
- install [pip](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/) **ONLY IF** there is a missing package that you might need to install manually (text me, otherwise I won't know);

## Great, I managed to do it! What's next?
**1.** Fork/download the code from the repository to any path of your choice in your computer (the best would be to sit right next to your libft folder, like described below)

**2.** If your directory tree looks like this...

```txt
	│
	├── 42-tool (this directory)
	├── libft 	(your repository)
	│
	...
```
then you can skip this step. Otherwise, you must change the "path" variable inside the **utils.py** file. It should look something like this:

```py
	import os
	import copy
	import random
	import subprocess

	from colorama import Style
	from colorama import Fore

	# INSERT YOUR PATH HERE, INSIDE QUOTES
	path = '../libft/'

	...
```

**3.** If you reached this step, you can finally execute it! Because the 'brain' of the tool was built on Python, there is no need for compilation and binary files generation (unlike C). Just open a terminal inside this directory's folder and run the following command:

```shell 
python3 -B main.py
```

It should prompt you with something similar to this:

| Main Menu |
|:--:|
||

You should press the char that corresponds to the option you want to run and press ENTER when you're done.

## Can you give me a quick tour about the features and how they work?
Sure!

**1. Check for forbidden files**

It prints out any extraneous files/folders your repository contains. Here's an example:

| Good Example | Bad Example |
|:--:|:--:|
|||

**2./3. Check filenames for Mandatory/Bonus files**

It prints out the result of checking if every Mandatory/Bonus part file was delivered. Unless you chose the last option, you can chose to run this parts separately, since the Bonus part is optional. Here's an example of possible outputs: 

| Good Example | Bad Example |
|:--:|:--:|
|||

> <span style='color: orange'> **NOTE**: as it is for now, if you created your bonus files with the "_bonus" as a suffix, the parser will considered it wrong. Since the Moulinette didn't complain about having or not having it, you are free to take it off, at least to parse the files. 
If you don't, probably the rest of the checks will fail in cascade. I'll fix it in the next patches.</span>


**4. Run the Norminette**

You all know her. You all know how she looks like. I don't think I need an image for this one (for now...).

**5./6. Look for incorrect function prototypes in '.c'/'libft.h' files**

Like 2 and 3, this two can be done separately, not because they are not mandatory (because both are), but mostly due to modularity. You don't need to go through all the correct parts if you want a specific one. Here are the possible results for a prototype:

- In '.c' files:
	- [<span style='color:#00FF88'>**CORRECT**</span>] - Your prototype matches the parser's
	- [<span style='color:#FFDD00'>**NOT FOUND**</span>] - The parser found the file, but not the prototype (this one is still in the works to improve)
	- [<span style='color:#FF7777'>**FILE NOT DELIVERED**</span>] - That one is pretty straight forward
- In 'libft.h':
	- [<span style='color:#00FF88'>**CORRECT**</span>] - The same
	- [<span style='color:#FFDD00'>**UNKNOWN**</span>] - It found a strange prototype
	- [<span style='color:#FF7777'>**NOT FOUND**</span>] - The same
	- [<span style='color:#FF7777'>**FILE NOT DELIVERED**</span>] - The same

> <span style = 'color: orange'> NOTE: as it is for now, the parser considers any prototype that is different from the ones he's looking for, as UNKNOWN. To clarify, if you have the right prototype with 1 more space (for e.g.) he'll display two entries: [UNKNOWN] and [NOT FOUND], because the strings are not an exact match (will be fixed in the next updates). 
In order to minimize this from happening, you should have your files passing the Norminette.</span>

| Parsing '.c' files | Parsing 'libft.h' file |
|:--:|:--:|
|||

**7. Full run**

Runs all of the above.

## Will there be more features?

Definitely! I intend to integrate more functionalities as I implement them, like analysing what and how the Makefile is compiling, do unit tests, upgrade the current features, normalize the UI and, of course, integrate good suggestions. Everytime I release a new patch or hotfix, I'll be deploying a new **[release](https://github.com/Nuno-Jesus/42-tool/releases)**, so make sure you check it!

## Author

Nuno Jesus, 42 Porto, ncarvalh

