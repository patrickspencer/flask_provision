/*
 * run the following command:
 * sudo -u postgres psql -U postgres -d okapi_db -a -f provision.sql
 */
CREATE DATABASE okapi_db;
CREATE USER okapi WITH PASSWORD 'password';
ALTER ROLE okapi SET client_encoding TO 'utf8';
ALTER ROLE okapi SET default_transaction_isolation TO 'read committed';
ALTER ROLE okapi SET timezone TO 'UTC';
ALTER ROLE "okapi" WITH LOGIN;
GRANT ALL PRIVILEGES ON DATABASE okapi_db TO okapi;
