-- Date: 2024-03-09 09:37:49
-- Author: Timo Feucht
-- Create the database and tables for the distributed systems project

-- -----------------------------------------------------

-- Tabelle `topic`
CREATE TABLE IF NOT EXISTS `topic`
(
    `T-ID` INTEGER PRIMARY KEY,
    `name` TEXT NOT NULL
);

-- Tabelle `solutions`
CREATE TABLE IF NOT EXISTS `solutions`
(
    `S-ID`           INTEGER PRIMARY KEY,
    `a`              TEXT NOT NULL,
    `b`              TEXT NOT NULL,
    `c`              TEXT NOT NULL,
    `correct_answer` TEXT NOT NULL,
    `explanation`    TEXT,
    CHECK (`correct_answer` IN ('a', 'b', 'c'))
);

-- Tabelle `questions`
CREATE TABLE IF NOT EXISTS `questions`
(
    `Q-ID`     INTEGER PRIMARY KEY,
    `S-ID`     INTEGER NOT NULL,
    `T-ID`     INTEGER NOT NULL,
    `level`    INTEGER NOT NULL,
    `question` TEXT    NOT NULL,
    CHECK (`level` >= 1 AND `level` <= 10),
    FOREIGN KEY (`T-ID`) REFERENCES `topic` (`T-ID`),
    FOREIGN KEY (`S-ID`) REFERENCES `solutions` (`S-ID`)
);

-- Tabelle `user`
CREATE TABLE IF NOT EXISTS `user`
(
    `U-ID`  INTEGER PRIMARY KEY,
    `level` INTEGER NOT NULL
        CHECK (`level` >= 1 AND `level` <= 10)
);

-- Tabelle `answered_questions`
CREATE TABLE IF NOT EXISTS `answered_questions`
(
    `U-ID`   INTEGER NOT NULL,
    `Q-ID`   INTEGER NOT NULL,
    `answer` BOOLEAN NOT NULL,
    PRIMARY KEY (`U-ID`, `Q-ID`),
    CONSTRAINT `U-ID-Constraint` FOREIGN KEY (`U-ID`) REFERENCES `user` (`U-ID`) ON DELETE CASCADE,
    CONSTRAINT `Q-ID-Constraint` FOREIGN KEY (`Q-ID`) REFERENCES `questions` (`Q-ID`) ON DELETE CASCADE
--     FOREIGN KEY (`U-ID`) REFERENCES `user` (`U-ID`),
--     FOREIGN KEY (`Q-ID`) REFERENCES `questions` (`Q-ID`)
);


-- Thema `Geographie` in `topic` einfuegen
INSERT INTO topic (`T-ID`, `name`)
VALUES (1, 'Geographie');

-- Angenommen, `Geographie` erhaelt die `T-ID` 1, fuegen wir Fragen und Loesungen ein
-- Bitte beachten Sie, dass die `S-ID` und `Q-ID` Werte manuell angepasst werden muessen, falls sie automatisch generiert werden

-- Loesungen einfuegen
INSERT INTO solutions (`S-ID`, `a`, `b`, `c`, `correct_answer`, `explanation`)
VALUES (1, 'Asien', 'Europa', 'Afrika', 'a',
        'Asien ist der groeßte Kontinent sowohl nach Flaeche als auch nach Bevoelkerung.'),
       (2, 'Amazonas', 'Nil', 'Jangtse', 'b', 'Der Nil ist mit etwa 6.650 km der laengste Fluss der Erde.'),
       (3, 'Mount Everest', 'K2', 'Zugspitze', 'a',
        'Der Mount Everest ist mit einer Hoehe von 8.848 Metern der hoechste Berg der Erde.'),
       (4, 'Russland', 'Kanada', 'China', 'a', 'Russland ist das flaechenmaeßig groeßte Land der Welt.'),
       (5, '5', '4', '3', 'b',
        'Es gibt 4 Ozeane: den Atlantik, den Pazifik, den Indischen Ozean und den Arktischen Ozean.'),
       (6, 'Sahara', 'Gobi', 'Antarktische Wueste', 'c', 'Die Antarktische Wueste ist die groeßte Wueste der Welt.'),
       (7, 'Vatikanstadt', 'Monaco', 'Nauru', 'a', 'Vatikanstadt ist der kleinste unabhaengige Staat der Welt.'),
       (8, 'China', 'Indien', 'USA', 'b', 'Indien ist nach China das bevoelkerungsreichste Land der Welt.'),
       (9, 'Tansania, Ruanda, Burundi, die Demokratische Republik Kongo, Uganda, Kenia, Äthiopien, Eritrea, Suedsudan, Sudan und Ägypten', 'Schweiz, Liechtenstein, Österreich, Deutschland, Frankreich und den Niederlanden', 'Peru, Kolumbien und Brasilien', 'a',
        'Der Nil durchfließt zahlreiche Laender Afrikas und ist bekannt fuer seine historische Bedeutung.'),
       (10, 'Atlantik', 'Indischer Ozean', 'Pazifik', 'c', 'Der Pazifik ist der groeßte Ozean der Erde.');

-- Fragen einfuegen und auf Loesungen verweisen
INSERT INTO questions (`Q-ID`, `S-ID`, `T-ID`, `level`, `question`)
VALUES (1, 1, 1, 1, 'Welches ist der groeßte Kontinent?'),
       (2, 2, 1, 2, 'Welcher ist der laengste Fluss der Erde?'),
       (3, 3, 1, 5, 'Welches ist der hoechste Berg der Erde?'),
       (4, 4, 1, 1, 'Welches ist das flaechenmaeßig groeßte Land der Welt?'),
       (5, 5, 1, 2, 'Wie viele Ozeane gibt es auf der Erde?'),
       (6, 6, 1, 5, 'Welches ist die groeßte Wueste der Welt?'),
       (7, 7, 1, 3, 'Welches ist der kleinste unabhaengige Staat der Welt?'),
       (8, 8, 1, 4, 'Welches Land ist nach China das bevoelkerungsreichste?'),
       (9, 9, 1, 5, 'Durch welche Laender fließt der laengste Fluss der Erde?'),
       (10, 10, 1, 1, 'Welcher ist der groeßte Ozean der Erde?');