create table if not exists counter (
    id         int      not null auto_increment,
    num        int      not null,
    created_at datetime not null default current_timestamp,
    primary key (id)
);
