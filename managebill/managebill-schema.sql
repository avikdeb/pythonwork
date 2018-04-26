-- copy the below command and execute in local venv (View > Tool Window > Terminal to create the database - cd managebill
-- sqlite3 managebill.db < managebill-schema.sql

drop table if exists user;
create table user (
    id integer primary key autoincrement,
    username text not null,
    password text not null,
    firstname text not null,
    lastname text not null,
    email text not null,
    mobile text not null,
    adminflag integer not null
);

drop table if exists paymentstatus;
create table paymentstatus (
    id integer primary key autoincrement,
    status text not null
);

drop table if exists useraudit;
create table useraudit (
    id integer primary key autoincrement,
    userid integer,
    createdby integer not null,
    createdon text not null,
    updatedby integer not null,
    updatedon text not null
);

drop table if exists melectricitybill;
create table melectricitybill (
    id integer primary key autoincrement,
    fromdate text not null,
    todate text not null,
    unitsconsumed integer not null,
    billamount real not null,
    amountpostduedate real not null,
    duedate text not null,
    lastdate text not null,
    paymentstatusid integer
);