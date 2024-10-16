{{ config(
    materialized='table'  
) }}

WITH raw_data AS (
    SELECT
        channel_title,
        channel_username,
        message_Id,  -- Corrected typo
        message,
        date,
        media_path
    FROM
        {{ ref('task2') }}  
),

cleaned_data AS (
    SELECT
        channel_title,
        channel_username,
        message_Id,  -- Corrected typo
        message,
        date,
        media_path
    FROM
        raw_data
    WHERE
        message IS NOT NULL  
        AND date IS NOT NULL  
),

messages_with_length AS (
    SELECT
        channel_title,
        channel_username,
        message_Id,  -- Corrected typo
        message,
        date,
        media_path,
        LENGTH(message) AS message_length 
    FROM
        cleaned_data
),

channel_message_counts AS (
    SELECT
        channel_username,
        COUNT(*) AS message_count,
        MIN(date) AS first_message_date,  -- Get the first message date
        MAX(date) AS last_message_date     -- Get the last message date
    FROM
        cleaned_data
    GROUP BY
        channel_username
),

enriched_messages AS (
    SELECT
        m.channel_title,
        m.channel_username,
        m.message_Id,  -- Corrected typo
        m.message,
        m.date,
        m.media_path,
        LENGTH(m.message) AS message_length,
        EXTRACT(YEAR FROM m.date) AS message_year,  
        EXTRACT(MONTH FROM m.date) AS message_month,  
        c.message_count,
        c.first_message_date,
        c.last_message_date
    FROM
        messages_with_length m
    LEFT JOIN
        channel_message_counts c
    ON
        m.channel_username = c.channel_username  
)


SELECT *
FROM enriched_messages 
