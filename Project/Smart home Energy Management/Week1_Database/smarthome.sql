CREATE DATABASE smarthome_db;
use smarthome_db;
CREATE TABLE rooms (
    room_id INT PRIMARY KEY,
    room_name VARCHAR(50)
);

CREATE TABLE devices (
    device_id INT PRIMARY KEY,
    device_name VARCHAR(50),
    room_id INT,
    status VARCHAR(10),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE energy_logs (
    log_id INT PRIMARY KEY,
    device_id INT,
    timestamp DATETIME,
    energy_kwh FLOAT,
    FOREIGN KEY (device_id) REFERENCES devices(device_id)
);

INSERT INTO rooms VALUES (101, 'Living Room'), (102, 'Bedroom'), (103, 'Kitchen');

INSERT INTO devices VALUES 
(1, 'Smart Bulb', 101, 'ON'),
(2, 'AC Unit', 101, 'OFF'),
(3, 'Heater', 102, 'ON'),
(4, 'TV', 103, 'OFF');

INSERT INTO energy_logs VALUES
(1, 1, '2025-09-29 08:00:00', 0.2),
(2, 1, '2025-09-29 09:00:00', 0.3),
(3, 2, '2025-09-29 10:00:00', 1.5),
(4, 3, '2025-09-29 08:30:00', 0.7),
(5, 4, '2025-09-29 11:00:00', 0.9);

DELIMITER //
CREATE PROCEDURE GetRoomUsagePerDay(IN input_date DATE)
BEGIN
    SELECT r.room_name, SUM(e.energy_kwh) AS total_energy
    FROM energy_logs e
    JOIN devices d ON e.device_id = d.device_id
    JOIN rooms r ON d.room_id = r.room_id
    WHERE DATE(e.timestamp) = input_date
    GROUP BY r.room_name;
END //
DELIMITER ;

CALL GetRoomUsagePerDay('2025-09-29');