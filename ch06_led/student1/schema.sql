create table if not exists led_record (
    id         int        not null auto_increment,
    pin        int        not null,
    is_on      tinyint(1) not null,
    created_at datetime   not null default current_timestamp,
    primary key (id)
);
