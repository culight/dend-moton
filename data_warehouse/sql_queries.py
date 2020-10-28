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
        sessionId VARCHAR(250),
        itemInSession VARCHAR(100),
        userid VARCHAR(100),
        artist_name VARCHAR(100),
        auth VARCHAR(100),
        firstName VARCHAR(50),
        lastName VARCHAR(50),
        gender VARCHAR(10),
        length VARCHAR(100),
        level VARCHAR(50),
        location VARCHAR(250),
        method VARCHAR(50),
        page VARCHAR(100),
        registration VARCHAR(250),
        title VARCHAR(250),
        status VARCHAR(100),
        ts VARCHAR(250),
        userAgent VARCHAR(250)
    );
"""

staging_songs_table_create = """ 
    CREATE TABLE song_staging (
        num_songs INTEGER,
        artist_id VARCHAR(100),
        artist_name VARCHAR(100),
        song_id VARCHAR(100),
        title VARCHAR(250),
        duration FLOAT,
        year VARCHAR(10)
    );
"""

songplay_table_create = """
    CREATE TABLE songplay (
        songplay_id INTEGER PRIMARY KEY NOT NULL,
        start_time DATE,
        user_id INTEGER NOT NULL,
        level VARCHAR(10),
        song_id INTEGER NOT NULL,
        artist_id INTEGER NOT NULL,
        session_id INTEGER NOT NULL,
        location VARCHAR(50),
        user_agent VARCHAR(50)
    );
"""

user_table_create = """
    CREATE TABLE "user" (
        user_id INTEGER PRIMARY KEY NOT NULL,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        gender CHAR,
        level INTEGER
    );
"""

song_table_create = """
    CREATE TABLE song (
        song_id INTEGER PRIMARY KEY NOT NULL,
        title VARCHAR(100),
        artist_id INTEGER NOT NULL,
        year INTEGER,
        duration REAL
    );
"""

artist_table_create = """
    CREATE TABLE artist (
        artist_id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(50) NOT NULL,
        location VARCHAR(50),
        latitude REAL,
        longitude REAL
    );
"""

time_table_create = """
    CREATE TABLE time (
        start_time TIMESTAMP PRIMARY KEY NOT NULL,
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
songplay_table_insert = (
    """INSERT INTO songplay VALUES ({}) ON CONFLICT (songplay_id) DO NOTHING;"""
)
songplay_table_cols = (
    "songplay_id",
    "start_time",
    "user_id",
    "level",
    "song_id",
    "artist_id",
    "session_id",
    "location",
    "user_agent",
)

user_table_insert = (
    """ INSERT INTO songplay VALUES ({}) ON CONFLICT (user_id) DO NOTHING;"""
)
user_table_cols = ("user_id", "first_name", "last_name", "gender", "level")

song_table_insert = """INSERT INTO song VALUES ({}) ON CONFLICT (song_id) DO NOTHING;"""
song_table_cols = ("song_id", "title", "artist_id", "year", "duration")

artist_table_insert = (
    """INSERT INTO artist VALUES ({}) ON CONFLICT (artist_id) DO NOTHING;"""
)
artist_table_cols = ("artist_id", "name", "location", "latitude", "longitude")

time_table_insert = (
    """INSERT INTO time VALUES ({}) ON CONFLICT (start_time) DO NOTHING;"""
)
time_table_cols = ("start_time", "hour", "day", "week", "month", "year", "weekday")

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
    (songplay_table_insert, songplay_table_cols),
    (user_table_insert, user_table_cols),
    (song_table_insert, song_table_cols),
    (artist_table_insert, artist_table_cols),
    (time_table_insert, time_table_cols),
]
