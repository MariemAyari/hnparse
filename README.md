# Hacker news scraper
Web scraper that extract the top posts from hacker news web site given as entry the number of posts you want to display in JSON format

## Getting started
Start by cloning the project. Tested and working in python 3.6

## Prerequisites
To install the requirements run the command `pip install -r requirements`

## Running tests

## Run from command line
 From the command line run `./hackernews --posts number_of_posts_to_dispay`
 If no argument was given it defaults to 30.

 Also number of posts to display can be set using envirenment variable with comand `export HN_POSTS=number_of_posts_to_display` beforerunning `./hackernews`

## Run with Docker
``` shell
# Build the container:
$ docker build -t hnparse .
# Run the container:
$ docker run -e HN_POSTS=number_of_posts_to_dispay hnparse
```

## Built with
* requests : allows to send http requests and it was used in the project to extract the web site content using get
* beautifulSoup : library used to parse the extracted content of the web site     
