CREATE TABLE IF NOT EXISTS Frequent_Visitor (
            Id INT NOT NULL UNIQUE,
            First_Name CHAR(25) NOT NULL,
            Last_Name CHAR(25),
            Relation CHAR(25),
            Last_Visited DATETIME,
            No_of_Visits INT NOT NULL,
            Album_Path CHAR(25)
        ); 