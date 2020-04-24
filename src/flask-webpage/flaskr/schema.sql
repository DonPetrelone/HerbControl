DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE ranges (
  airTempHighDanger INTEGER NOT NULL,
  airTempHighWarning INTEGER NOT NULL,
  airTempGood INTEGER NOT NULL,
  airTempLowWarning INTEGER NOT NULL,
  airTempLowDanger INTEGER NOT NULL,
  airHumHighDanger INTEGER NOT NULL,
  airHumHighWarning INTEGER NOT NULL,
  airHumGood INTEGER NOT NULL,
  airHumLowWarning INTEGER NOT NULL,
  airHumLowDanger INTEGER NOT NULL,
  soilMoistHighDanger INTEGER NOT NULL,
  soilMoistHighWarning INTEGER NOT NULL,
  soilMoistGood INTEGER NOT NULL,
  soilMoistLowWarning INTEGER NOT NULL,
  soilMoistLowDanger INTEGER NOT NULL
);

CREATE TABLE values (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  soilMoisture INTEGER,
  airTemperature INTEGER,
  airHumidity INTEGER,
  date TEXT
);

INSERT INTO user VALUES (1, 'herbs', 
  'pbkdf2:sha256:150000$aKzKX7W5$0c3413e97ca81b2257bc61587a6a7a87f8ff95a35cd6c36acafc946a867d0142');
