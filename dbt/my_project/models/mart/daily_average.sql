{{config(
    materialized= 'table',
)}}

select
    city,
    date(weather_time_local) as date,
    round(avg(temperature)::numeric, 2) as avg_temperature,
    round(avg(wind_speed)::numeric, 2) as avg_wind_speed,
    round(avg(pressure)::numeric, 2) as avg_pressure,
    round(avg(humidity)::numeric, 2) as avg_humidity
from {{ref('stg_weather_data')}}
group by 
    city,
    date(weather_time_local)
order by 
    city,
    date(weather_time_local)

