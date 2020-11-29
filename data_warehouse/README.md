# AWS Data Warehouse - Sparkify Demo Project

## Summary
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

I have built an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms the data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to.

This repository houses the code that creates the necessary AWS Data Warehousing infastructure for that ETL pipeline. It initializes an AWS client, creates the SQL tables, and populates the tables in accordance with specifications.

## Setup
Requires:
- python 
