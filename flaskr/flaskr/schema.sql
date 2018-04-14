-- Below script creates a table 'entries' in sqlite3 database supplied with Python 3 --

drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);