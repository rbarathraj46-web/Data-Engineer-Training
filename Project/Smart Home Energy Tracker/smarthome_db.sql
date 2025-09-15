CREATE DATABASE smarthome_db;
USE smarthome_db;
CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_name VARCHAR(100) NOT NULL
);
CREATE TABLE devices (
    device_id INT AUTO_INCREMENT PRIMARY KEY,
    device_name VARCHAR(100) NOT NULL,
    room_id INT,
    status ENUM('ON', 'OFF') DEFAULT 'OFF',
    power_rating_watts INT,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);
CREATE TABLE energy_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    device_id INT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    energy_consumed_kwh DECIMAL(10,3),
    FOREIGN KEY (device_id) REFERENCES devices(device_id)
);

INSERT INTO rooms (room_name) VALUES 
('Living Room'),
('Bedroom'),
('Kitchen');

INSERT INTO devices (device_name, room_id, status, power_rating_watts) VALUES
('Smart TV', 1, 'ON', 120),
('Lamp', 1, 'OFF', 40),
('Air Conditioner', 2, 'ON', 1500),
('Fridge', 3, 'ON', 200);

INSERT INTO energy_logs (device_id, timestamp, energy_consumed_kwh) VALUES
(1, '2025-09-15 08:00:00', 0.3),
(2, '2025-09-15 09:00:00', 0.05),
(3, '2025-09-15 09:30:00', 1.2),
(4, '2025-09-15 10:00:00', 0.8);

INSERT INTO devices (device_name, room_id, status, power_rating_watts) 
VALUES ('Heater', 2, 'OFF', 1000);

select * from devices;
select * from devices WHERE device_id = 3;
UPDATE devices SET status = 'ON' WHERE device_id = 2;

CREATE PROCEDURE GetDailyRoomUsage(IN input_date DATE)

    SELECT r.room_name, 
           DATE(e.timestamp) AS log_date,
           SUM(e.energy_consumed_kwh) AS total_kwh
    FROM energy_logs e
    JOIN devices d ON e.device_id = d.device_id
    JOIN rooms r ON d.room_id = r.room_id
    WHERE DATE(e.timestamp) = input_date
    GROUP BY r.room_name, DATE(e.timestamp);

CALL GetDailyRoomUsage('2025-09-15');

