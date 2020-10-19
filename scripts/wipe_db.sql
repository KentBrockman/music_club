/* Clean out music_club tables and reset the sequence
Runs against SQLite only... */ 

DELETE FROM music_club_comment;
DELETE FROM music_club_albumreview;
DELETE FROM music_club_albumsubmission;
DELETE FROM music_club_album;

UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='music_club_album';
UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='music_club_albumsubmission';
UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='music_club_albumreview';
UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='music_club_comment';