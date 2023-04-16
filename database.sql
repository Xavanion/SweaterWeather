CREATE TABLE IF NOT EXISTS responder(num INTEGER AUTOINCREMENT, emails TEXT, area TEXT);
INSERT INTO responder VALUES (gamer@gmail.com, Lawrence);
INSERT INTO responder VALUES (sigma@gmail.com, London);
INSERT INTO responder VALUES (alpha@gmail.com, Tokyo);
INSERT INTO responder VALUES (beta@gmail.com, Lawrence);

SELECT * from responder WHERE area=Lawrence;