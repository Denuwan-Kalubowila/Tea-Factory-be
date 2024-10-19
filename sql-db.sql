CREATE TYPE user_role AS ENUM ('admin', 'manager', 'supervisor');

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    role user_role DEFAULT 'supervisor',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a custom sequence for user IDs
CREATE SEQUENCE custom_user_id_seq
    START WITH 1000  -- Starting value
    INCREMENT BY 1;  -- Increment step

-- Create the users table with a custom auto-increment user_id
CREATE TABLE users (
    user_id INT DEFAULT nextval('custom_user_id_seq') PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    role user_role DEFAULT 'supervisor',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE SEQUENCE custom_route_id_seq
    START WITH 500  
    INCREMENT BY 1; 


CREATE TABLE route (
    route_id INT DEFAULT nextval('custom_route_id_seq') PRIMARY KEY,
    route_name VARCHAR(50) UNIQUE NOT NULL,
    distance INT NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO route (route_name, distance, password)
VALUES 
('Madala', 15, 'madala_tea_002'),
('Dumbara', 25, 'dumbara_tea_004'),
('Eheliyagoda', 40, 'eheliyagoda_tea_003'),
('Idangoda', 32, 'idangoda_tea_006'),
('Keenagawila', 18, 'keenagahawila_tea_007');

CREATE SEQUENCE custom_check_id_seq
    START WITH 100  
    INCREMENT BY 1; 


CREATE TABLE check_route (
    checked_id INT DEFAULT nextval('custom_check_id_seq') PRIMARY KEY,
    route_id INT NOT NULL,
    quantity INT NOT NULL,
    prod INT NOT NULL,
    reject INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_route
        FOREIGN KEY (route_id)
        REFERENCES route(route_id)
        ON DELETE CASCADE
);

ALTER TABLE suply_tea
ADD COLUMN route_id INT NOT NULL,
ADD CONSTRAINT fk_route
    FOREIGN KEY (route_id)
    REFERENCES route(route_id)
    ON DELETE CASCADE;


INSERT INTO suply_tea (supplier_id, leaf_id, quantity,route_id) VALUES
( 601, 1, 50,503),
(602, 2, 100,501),
( 600, 1,200,504),
(601, 1,20,503),
(604, 2,50,502),
(602, 1, 125, 501);

















