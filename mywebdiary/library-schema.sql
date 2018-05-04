-- copy the below command and execute in local venv (View > Tool Window > Terminal to create the database - cd mywebdiary
-- sqlite3 library.db < library-schema.sql

drop table if exists country;
create table country (
    id integer primary key autoincrement,
    name text not null
);

drop table if exists author;
create table author (
    id integer primary key autoincrement,
    country_id integer,
    name text not null
);

drop table if exists book;
create table book (
    id integer primary key autoincrement,
    author_id integer,
    name text not null,
    isbn text
);