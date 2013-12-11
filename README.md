TwitterAPI
==========

This project is the work of Mary Gillen, a 2nd year MSIS student at the School of Information and Library Science at the University of North Carolina at Chapel Hill. The hope is that the following documentation and provided Python script will be of use to other students within the program, specifically those focusing on information retrieval, text/data mining or other similar projects where access to large amounts of Twitter data is needed. 


Project Background
---

Twitter is an online social networking and microblogging website that allows users to read, post and respond to short text messages ('tweets') of 140 characters. The service is a cultural phenomenon, with more than 200 million tweets posted every day. While they are most commonly used for entertainment and communication between friends, tweets also represent an enormous source of potential knowledge. It is for this reason that some researchers may find it necessary to gather and store said tweets. The Twitter TOS forbids this, however, making it necessary for researchers to gather new data for each project. This is most easily accomplished by querying the Twitter API. The steps necessary to doing this will be documented below and a script (written in Python) provided. 

What is an API?
---

An API ('application programming interface') specifies how some software components should interact with each other. In the case of Twitter, the API stands between the user needing specific information and the actual information itself. Twitter and its users privacy rights are the heart of this. Before beginning any work with the Twitter API, you should familiarize yourself with Twitter's developer rules found here https://dev.twitter.com/terms/api-terms. 

Preparation
---

In order to use the Twitter API, we will need to write a script that can query for exactly what we need. For the purposes of this project, our script will be written in Python, but other languages can be used as well, including C++, Java, JavaScript, Perl, PHP, etc. 

In order to write a script, we are going to need some help. This is where Twitter Libraries come in handy. While we could write a Python script to directly interact with the Twitter API, it is much simpler to use a library. Libraries define the various ways to query the Twitter API in their code and simplify the language and process. In simpler terms, we will write our Python script in the language used by the library and the library will translate this into the language necessary for the Twitter API to react. 

There are loads of libraries out on the web for use. A starting list can be found here: https://dev.twitter.com/docs/twitter-libraries. This project uses Twython ('https://github.com/ryanmcgrath/twython') because of its ease of use, stellar documentation and frequent and responsive updates  
