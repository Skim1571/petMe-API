-- settings.sql
CREATE DATABASE petme;
CREATE USER petmeuser WITH PASSWORD 'petme';
GRANT ALL PRIVILEGES ON DATABASE petme TO petmeuser;