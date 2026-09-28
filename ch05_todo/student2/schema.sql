create table if not exists todo (
    id         int          not null auto_increment,
    content    varchar(200) not null,
    is_done    tinyint(1)   not null default 0,
    created_at datetime     not null default current_timestamp,
    primary key (id)
);
