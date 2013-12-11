TwitterAPI
==========

This project is the work of Mary Gillen, a 2nd year MSIS student at the School of Information and Library Science at the University of North Carolina at Chapel Hill. The hope is that the following documentation and provided Python script will be of use to other students within the program, specifically those focusing on information retrieval, text/data mining or other similar projects where access to large amounts of Twitter data is needed. 


Project Background
---

Twitter is an online social networking and microblogging website that allows users to read, post and respond to short text messages ('tweets') of 140 characters. The service is a cultural phenomenon, with more than 200 million tweets posted every day. While they are most commonly used for entertainment and communication between friends, tweets also represent an enormous source of potential knowledge. It is for this reason that some researchers may find it necessary to gather and store said tweets. The Twitter TOS forbids this, however, making it necessary for researchers to gather new data for each project. This is most easily accomplished by querying the Twitter API. The steps necessary to doing this will be documented below and a script (written in Python) provided. 

What is an API?
---

An API ('application programming interface') specifies how some software components should interact with each other. In the case of Twitter, the API stands between the user needing specific information and the actual information itself. Twitter and its users privacy rights are the heart of this. Before beginning any work with the Twitter API, you should familiarize yourself with Twitter's developer rules found here https://dev.twitter.com/terms/api-terms. 

Twitter uses two separate APIs, the REST API and the Streaming API. The REST API lets you query or modify a user's account. You don't need their permission to query their account, but you do need it to modify their account. They provide permission through OAuth authentication.

The Streaming API delivers tweets based on search terms or for specific users you request, along with information about the author, in real-time. You do not need the tweet author's permission. You must log into some Twitter account to use streaming, using either basic or OAuth authentication. The Streaming API also favors real-time delivery.

For the purposes of this project, we will be using the Streaming API. 

Preparation
---

<i>Getting Authorization</i>

Twitter requires that users querying the API register their 'apps', or projects in order to receive the authorization codes necessary for using the API. You will need a Twitter account in order to do this so sign up if you don't have one! Go to https://dev.twitter.com and log in. From there, go to https://dev.twitter.com/apps/new and fill out the form. 

Once you've gotten approval, you will be assigned the necessary authorization codes. These can be found by navigating to Your Applications and clicking the appropriate one. Keep these handy for later.

<i>Set Up</i>

In order to use the Twitter API, we will need to write a script that can query for exactly what we need. For the purposes of this project, our script will be written in Python, but other languages can be used as well, including C++, Java, JavaScript, Perl, PHP, etc. 

In order to write a script, we are going to need some help. This is where Twitter Libraries come in handy. While we could write a Python script to directly interact with the Twitter API, it is much simpler to use a library. Libraries define the various ways to query the Twitter API in their code and simplify the language and process. In simpler terms, we will write our Python script in the language used by the library and the library will translate this into the language necessary for the Twitter API to react. 

There are loads of libraries out on the web for use. A starting list can be found here: https://dev.twitter.com/docs/twitter-libraries. This project uses Twython ('https://github.com/ryanmcgrath/twython') because of its ease of use, stellar documentation and frequent and responsive updates.

Getting Started
---

We'll be using the Ubuntu terminal to both write and run our Python script. You can either find a computer with Ubuntu already installed or use your own with a Virtual Machine and then installing Ubuntu. (http://www.ubuntu.com/download/desktop/install-desktop-latest) If you're unfamiliar with Ubuntu and/or Linux, you're going to want to study up a bit as this project won't get into how to use it. For the most part, we'll be using simple commands such as `cd`, `ls` and `nano.` A nice review can be found here: https://help.ubuntu.com/community/UsingTheTerminal. 

To begin, get the terminal up and running. The first thing we need to do is install the Twython library on our machine. 
(<i>Keep in mind the following is also documented by the Twython developers themselves (http://twython.readthedocs.org/en/latest/), though there are some small differences between the code below and theirs.</i>)

```python
sudo pip install twython
```
That's it for installing Twython! Easy. We're using `sudo` here because `sudo` allows a permitted user to execute a command as the superuser or another user. This simply guarantees we'll be able to install what we need.
 
Familiarize yourself with the contents of the twython file now installed on your machine. Twython has some neat features that they've documented for building your script. They can be found in the `endpoints.py` file in the `twython/twython` directory. These will be helpful for you later as we won't go into all of the various options available to you for querying when writing the script. 

Writing the Code
---

Twython's own documentation is going to be a great asset for you when writing or editing your script. Their step-by-step process is outlined here: http://twython.readthedocs.org/en/latest/

To begin our script, we need to open a blank file. In the terminal, type:

```python
nano
```

This will open a blank file. The first thing we need to do is import our settings to the script. This will tell it what programs to run and how to process information.

```python
from twython import Twython
import csv, json

# Here we are importing the Twython library we previously installed. We are also importing the csv and json programs so we can later save the data we're gathering from Twitter into an easy-to-read and use Excel file.
```

Make sure you save frequently. In fact, let's do it now. Ctrl+O is the command to save in Ubuntu. It will prompt you name your file, so let's name it `api.py`. The `.py` lets the machine know what language we're using and will also color code various commands for easier reading.

If you want to test your script from time to time, you will need to exit the nano file by using Ctrl+X. This will put you back in the terminal. From there, you'll type `python api.py` and the script will either run (sucess!) or fail (boo!). The easiest way to constantly edit and test will be to have two terminals open, one running nano and containing the python script and the other open to the basic terminal. However, you are free to do whatever works best for you!

In order to query the Twitter API, we have to provide it with our authorization codes from before. In your script, type the following: 

```python
APP_KEY = '1234567890'
APP_SECRET = '1234567890'
OAUTH_TOKEN = '1234567890'
OAUTH_TOKEN_SECRET = '1234567890'
```

Now obviously '1234567890' isn't the actual code you need for the script to work, it's simply a placeholder. Refer back to your My Applications page on the Twitter Developer page. The naming Twitter uses for these authorization codes is a little confusing, but to make it easier:

APP_KEY = Consumer Key<br>
APP_SECRET = Consumer Secret<br>
OAUTH_TOKEN = Access Token<br>
OAUTH_TOKEN_SECRET = Access Token Secret

Simply replace '1234567890' with the keys that correspond. You will need the single quotation marks to offset the key, so don't leave them out.

After you have that information written in, add in the following: 

```python
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET, oauth_version=2)

ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(access_token=ACCESS_TOKEN)
```
 
These commands tell the API where to look for the information and to pull the corresponding keys down so that it can grant you access.

Now is a good time to save and run your script. If all goes well... Nothing will happen. If you have an error, check your code again. A single typo can ruin everything, so make sure your code is good and your keys are accurate!

Now it's time to add in some true functionality. We'll start with a very basic search. 
