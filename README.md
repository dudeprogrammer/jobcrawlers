# Jobcrawlers

A <a href="https://scrapy.org/">Scrapy</a> project aiming to collect job ad information from the web. At the moment the project only works with <a href="https://stackoverflow.com">stackoverflow.com</a>.


### Installing dependencies
First you need a working python on your OS.
Then run the following command to install python packges needed:
`pip install -r requirements.txt`

### Executing the crawler

To run the spider you can use the following command: </br>
`scrapy crawl stackoverflow -o stackoverflow_jobs.json` </br></br>
it saves the results in a file named "stackoverflow_jobs.json" in the same directory.

### Running tests

First change the working directory using `cd jobcrawlers` . Then run `pytest`
