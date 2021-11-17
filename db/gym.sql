DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS instructional_events;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    dob DATE NOT NULL,
    email VARCHAR(255) NOT NULL,
    gender VARCHAR(255)
);

CREATE TABLE instructional_events (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    time TIMESTAMP NOT NULL,
    duration INT NOT NULL,
    capacity INT NOT NULL,
    min_age INT,
    gender VARCHAR(255)
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id),
    instructional_event_id INT REFERENCES instructional_events(id)
);
