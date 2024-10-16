{{ config(
    materialized='table'  
) }}

SELECT * FROM {{ source('public', 'task2_data') }}
