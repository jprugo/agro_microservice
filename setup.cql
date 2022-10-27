CREATE KEYSPACE agro_gwtsas WITH replication = {'class': 'NetworkTopologyStrategy', 'datacenter1': '3'}  AND durable_writes = true;

USE agro_gwtsas;
    
CREATE TABLE model (
         id int PRIMARY KEY,
         t_ext double,
         t_suelo double,
         h_ext double,
         h_suelo double,
         luz double,
         bateria boolean,
         v_ent double,
         date timestamp
);