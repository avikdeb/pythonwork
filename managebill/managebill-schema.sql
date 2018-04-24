-- copy the below command and execute in local venv (View > Tool Window > Terminal to create the database - cd managebill
-- sqlite3 managebill.db < managebill-schema.sql

drop table if exists user;
create table user (
    userid integer primary key autoincrement,
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
    paymentstatusid integer primary key autoincrement,
    paymentstatus text not null
);

drop table if exists useraudit;
create table useraudit (
    userauditid integer primary key autoincrement,
    user_id integer,
    createdby integer not null,
    createdon text not null,
    updatedby integer not null,
    updatedon text not null
);

drop table if exists melectricitybill;
create table melectricitybill (
    melectricitybillid integer primary key autoincrement,
    billfromdate text not null,
    billtodate text not null,
    unitsconsumed integer not null,
    billamount real not null,
    billamountpostduedate real not null,
    paymentduedate text not null,
    paymentlastdate text not null,
    paymentstatus_id integer
);