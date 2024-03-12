-- Thema `Geographie` in `topic` einfuegen
INSERT INTO topic (`T_ID`, `name`)
VALUES (1, 'Geographie');

-- Angenommen, `Geographie` erhaelt die `T_ID` 1, fuegen wir Fragen und Loesungen ein
-- Bitte beachten Sie, dass die `S_ID` und `Q_ID` Werte manuell angepasst werden muessen, falls sie automatisch generiert werden

-- Loesungen einfuegen
INSERT INTO solutions (`S_ID`, `a`, `b`, `c`, `correct_answer`, `explanation`)
VALUES (1, 'Asien', 'Europa', 'Afrika', 'a',
        'Asien ist der groesste Kontinent sowohl nach Flaeche als auch nach Bevoelkerung.'),
       (2, 'Amazonas', 'Nil', 'Jangtse', 'b', 'Der Nil ist mit etwa 6.650 km der laengste Fluss der Erde.'),
       (3, 'Mount Everest', 'K2', 'Zugspitze', 'a',
        'Der Mount Everest ist mit einer Hoehe von 8.848 Metern der hoechste Berg der Erde.'),
       (4, 'Russland', 'Kanada', 'China', 'a', 'Russland ist das flaechenmaessig groesste Land der Welt.'),
       (5, '5', '4', '3', 'b',
        'Es gibt 4 Ozeane: den Atlantik, den Pazifik, den Indischen Ozean und den Arktischen Ozean.'),
       (6, 'Sahara', 'Gobi', 'Antarktische Wueste', 'c', 'Die Antarktische Wueste ist die groesste Wueste der Welt.'),
       (7, 'Vatikanstadt', 'Monaco', 'Nauru', 'a', 'Vatikanstadt ist der kleinste unabhaengige Staat der Welt.'),
       (8, 'China', 'Indien', 'USA', 'b', 'Indien ist nach China das bevoelkerungsreichste Land der Welt.'),
       (9, 'Tansania, Ruanda, Burundi, die Demokratische Republik Kongo, Uganda, Kenia, Äthiopien, Eritrea, Suedsudan, Sudan und Ägypten', 'Schweiz, Liechtenstein, Österreich, Deutschland, Frankreich und den Niederlanden', 'Peru, Kolumbien und Brasilien', 'a',
        'Der Nil durchfliesst zahlreiche Laender Afrikas und ist bekannt fuer seine historische Bedeutung.'),
       (10, 'Atlantik', 'Indischer Ozean', 'Pazifik', 'c', 'Der Pazifik ist der groesste Ozean der Erde.');

-- Fragen einfuegen und auf Loesungen verweisen
INSERT INTO questions (`Q_ID`, `S_ID`, `T_ID`, `level`, `question`)
VALUES (1, 1, 1, 1, 'Welches ist der groesste Kontinent?'),
       (2, 2, 1, 2, 'Welcher ist der laengste Fluss der Erde?'),
       (3, 3, 1, 5, 'Welches ist der hoechste Berg der Erde?'),
       (4, 4, 1, 1, 'Welches ist das flaechenmaessig groesste Land der Welt?'),
       (5, 5, 1, 2, 'Wie viele Ozeane gibt es auf der Erde?'),
       (6, 6, 1, 5, 'Welches ist die groesste Wueste der Welt?'),
       (7, 7, 1, 3, 'Welches ist der kleinste unabhaengige Staat der Welt?'),
       (8, 8, 1, 4, 'Welches Land ist nach China das bevoelkerungsreichste?'),
       (9, 9, 1, 5, 'Durch welche Laender fliesst der laengste Fluss der Erde?'),
       (10, 10, 1, 1, 'Welcher ist der groesste Ozean der Erde?');
