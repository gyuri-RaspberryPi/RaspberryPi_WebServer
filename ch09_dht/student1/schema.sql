create table if not exists dht_record (
    id          int      not null auto_increment,
    temperature decimal(4,1) not null,
    humidity    int      not null,
    created_at  datetime not null default current_timestamp,
    primary key (id)
);
