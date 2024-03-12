-- Date: 2024-03-09 09:37:49
-- Author: Timo Feucht
-- Create the database and tables for the distributed systems project

-- -----------------------------------------------------

-- Tabelle `topic`
CREATE TABLE IF NOT EXISTS `topic`
(
    `T_ID` INTEGER PRIMARY KEY,
    `name` TEXT NOT NULL
);

-- Tabelle `solutions`
CREATE TABLE IF NOT EXISTS `solutions`
(
    `S_ID`           INTEGER PRIMARY KEY,
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
    `Q_ID`     INTEGER PRIMARY KEY,
    `S_ID`     INTEGER NOT NULL,
    `T_ID`     INTEGER NOT NULL,
    `level`    INTEGER NOT NULL,
    `question` TEXT    NOT NULL,
    CHECK (`level` >= 1 AND `level` <= 10),
    FOREIGN KEY (`T_ID`) REFERENCES `topic` (`T_ID`),
    FOREIGN KEY (`S_ID`) REFERENCES `solutions` (`S_ID`)
);

-- Tabelle `user`
CREATE TABLE IF NOT EXISTS `user`
(
    `U_ID`  INTEGER PRIMARY KEY,
    `level` INTEGER NOT NULL
        CHECK (`level` >= 1 AND `level` <= 10)
);

-- Tabelle `answered_questions`
CREATE TABLE IF NOT EXISTS `answered_questions`
(
    `U_ID`   INTEGER NOT NULL,
    `Q_ID`   INTEGER NOT NULL,
    `answer` BOOLEAN NOT NULL,
    PRIMARY KEY (`U-ID`, `Q_ID`),
    CONSTRAINT `U_ID` FOREIGN KEY (`U_ID`) REFERENCES `user` (`U_ID`) ON DELETE CASCADE,
    CONSTRAINT `Q_ID` FOREIGN KEY (`Q_ID`) REFERENCES `questions` (`Q_ID`) ON DELETE CASCADE
--     FOREIGN KEY (`U_ID`) REFERENCES `user` (`U_ID`),
--     FOREIGN KEY (`Q_ID`) REFERENCES `questions` (`Q_ID`)
);
