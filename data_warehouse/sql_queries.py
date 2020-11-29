# ----------------------------------------------------------------
# Author: Demerrick Moton
# Summary: Houses the various SQL events for Sparkify
# ----------------------------------------------------------------

import configparser

# ----------------------------------------------------------------
# Source code is below, Constants and Imports are above
# ----------------------------------------------------------------

# CONFIG
config = configparser.ConfigParser()
config.read("dwh.cfg")

# DROP TABLES

staging_events_table_drop = """DROP TABLE IF EXISTS "event_staging";"""
staging_songs_table_drop = """DROP TABLE IF EXISTS "song_staging";"""
songplay_table_drop = """DROP TABLE IF EXISTS "songplay";"""
user_table_drop = """DROP TABLE IF EXISTS "user"; """
song_table_drop = """DROP TABLE IF EXISTS "song";"""
artist_table_drop = """DROP TABLE IF EXISTS "artist";"""
time_table_drop = """DROP TABLE IF EXISTS "time";"""

# CREATE TABLES

staging_events_table_create = """
    CREATE TABLE event_staging (
        artist_name VARCHAR(250),
        auth VARCHAR(100),
        first_name VARCHAR(50),
        gender CHAR,
        item_in_session INTEGER,
        last_name VARCHAR(50),
        length FLOAT,
        level VARCHAR(50),
        location VARCHAR(250),
        method VARCHAR(10),
        page VARCHAR(100),
        registration VARCHAR(250),
        session_id VARCHAR(10),
        status VARCHAR(250),
        title VARCHAR(250),
        ts BIGINT,
        useragent VARCHAR(250),
        user_id VARCHAR(100)
    );
"""

staging_songs_table_create = """ 
    CREATE TABLE song_staging (
        num_songs INTEGER,
        artist_id VARCHAR(100),
        artist_latitude REAL,
        artist_longitude REAL,
        artist_location VARCHAR(250),
        artist_name VARCHAR(100),
        song_id VARCHAR(100),
        title VARCHAR(250),
        duration FLOAT,
        year INTEGER
    );
"""
songplay_table_create = """
    CREATE TABLE songplay (
        songplay_id INTEGER IDENTITY(0,1) PRIMARY KEY,
        start_time TIMESTAMP,
        user_id VARCHAR(100) NOT NULL,
        level VARCHAR(50),
        song_id VARCHAR(100) NOT NULL,
        artist_id VARCHAR(100) NOT NULL,
        session_id VARCHAR(100) NOT NULL,
        location VARCHAR(50),
        user_agent VARCHAR(50)
    );
"""

user_table_create = """
    CREATE TABLE "user" (
        user_id VARCHAR(100) PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        gender CHAR,
        level VARCHAR(50)
    );
"""

song_table_create = """
    CREATE TABLE song (
        song_id VARCHAR(100) PRIMARY KEY,
        title VARCHAR(100),
        artist_id VARCHAR(100) NOT NULL,
        year VARCHAR(10),
        duration REAL
    );
"""

artist_table_create = """
    CREATE TABLE artist (
        artist_id VARCHAR(100) PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        location VARCHAR(250),
        latitude REAL,
        longitude REAL
    );
"""

time_table_create = """
    CREATE TABLE time (
        start_time TIMESTAMP PRIMARY KEY,
        hour INTEGER,
        day INTEGER,
        week INTEGER,
        month INTEGER,
        year INTEGER,
        weekday INTEGER
    );
"""

# STAGING TABLES

staging_events_copy = (
    """
    COPY "event_staging" from '{}'
    credentials 'aws_iam_role={}'
    format as json '{}'
    region 'us-west-2';
"""
).format(
    config["S3"]["LOG_DATA"], config["IAM_ROLE"]["ARN"], config["S3"]["LOG_JSONPATH"]
)

staging_songs_copy = (
    """
    COPY "song_staging" from '{}'
    credentials 'aws_iam_role={}'
    json 'auto'
    region 'us-west-2';
"""
).format(config["S3"]["SONG_DATA"], config["IAM_ROLE"]["ARN"])

# FINAL TABLES
songplay_table_insert = """
    INSERT INTO songplay (
        start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
    )
    SELECT DISTINCT
        TIMESTAMP 'epoch' + event.ts/1000 * INTERVAL '1 second' AS start_time,
        event.user_id, event.level, song.song_id, song.artist_id, event.session_id, event.location, event.useragent
    FROM song_staging song 
    JOIN event_staging event
    ON song.title = event.title
    AND song.artist_name = event.artist_name
    AND song.duration = event.length;
"""

user_table_insert = """
    INSERT INTO "user" (
        user_id, first_name, last_name, gender, level
    )
    SELECT DISTINCT user_id, first_name, last_name, gender, level
    FROM event_staging
    WHERE user_id IS NOT NULL;
"""

song_table_insert = """
    INSERT INTO song (
        song_id, title, artist_id, year, duration
    )
    SELECT DISTINCT song_id, title, artist_id, year, duration
    FROM song_staging
    WHERE song_id IS NOT NULL;
"""

artist_table_insert = """
    INSERT INTO artist (
        artist_id, name, location, latitude, longitude
    )
    SELECT DISTINCT 
        artist_id, artist_name, artist_location, artist_latitude, artist_longitude
    FROM song_staging
    WHERE artist_id IS NOT NULL;
"""

time_table_insert = """
    INSERT INTO time (
        start_time, hour, day, week, month, year, weekday
    )
    WITH time_converted AS (
        SELECT
            DISTINCT TIMESTAMP 'epoch' + ts/1000 * INTERVAL '1 second' AS start_time
        FROM event_staging
        WHERE ts IS NOT NULL
    )
    SELECT
        start_time AS start_time,
        extract(hour from start_time),
        extract(day from start_time),
        extract(week from start_time),
        extract(month from start_time),
        extract(year from start_time),
        extract(weekday from start_time)
    FROM time_converted;
"""

# QUERY LISTS
create_table_queries = [
    staging_events_table_create,
    staging_songs_table_create,
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
]
drop_table_queries = [
    staging_events_table_drop,
    staging_songs_table_drop,
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [
    songplay_table_insert,
    user_table_insert,
    song_table_insert,
    artist_table_insert,
    # time_table_insert,
]
