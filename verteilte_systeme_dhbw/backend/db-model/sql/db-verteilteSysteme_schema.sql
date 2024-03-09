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
    CONSTRAINT `U-ID` FOREIGN KEY (`U-ID`) REFERENCES `user` (`U-ID`) ON DELETE CASCADE,
    CONSTRAINT `Q-ID` FOREIGN KEY (`Q-ID`) REFERENCES `questions` (`Q-ID`) ON DELETE CASCADE
--     FOREIGN KEY (`U-ID`) REFERENCES `user` (`U-ID`),
--     FOREIGN KEY (`Q-ID`) REFERENCES `questions` (`Q-ID`)
);
