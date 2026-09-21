create table if not exists memo (
    id         int          not null auto_increment,
    content    varchar(200) not null,
    created_at datetime     not null default current_timestamp,
    primary key (id)
);
