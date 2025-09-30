use Smarthome_db
switched to db Smarthome_db
db.sensor_logs.insertMany([
  { device_id: 1, timestamp: ISODate("2025-09-29T08:00:00Z"), energy_kwh: 0.2 },
  { device_id: 1, timestamp: ISODate("2025-09-29T09:00:00Z"), energy_kwh: 0.3 },
  { device_id: 2, timestamp: ISODate("2025-09-29T10:00:00Z"), energy_kwh: 1.5 },
  { device_id: 3, timestamp: ISODate("2025-09-29T08:30:00Z"), energy_kwh: 0.7 },
  { device_id: 4, timestamp: ISODate("2025-09-29T11:00:00Z"), energy_kwh: 0.9 }
]);
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68dba99b8db7b27f6019c27d'),
    '1': ObjectId('68dba99b8db7b27f6019c27e'),
    '2': ObjectId('68dba99b8db7b27f6019c27f'),
    '3': ObjectId('68dba99b8db7b27f6019c280'),
    '4': ObjectId('68dba99b8db7b27f6019c281')
  }
}
db.sensor_logs.createIndex({ device_id: 1 });
device_id_1
db.sensor_logs.createIndex({ timestamp: 1 });
timestamp_1
