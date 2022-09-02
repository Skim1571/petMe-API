-- settings.sql
CREATE DATABASE petme;
CREATE USER petmeuser WITH PASSWORD 'petMe';
GRANT ALL PRIVILEGES ON DATABASE petme TO petmeuser;