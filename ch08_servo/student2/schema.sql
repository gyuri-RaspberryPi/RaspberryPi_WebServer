create table if not exists servo_record (
    id         int      not null auto_increment,
    pin        int      not null,
    angle      int      not null,
    created_at datetime not null default current_timestamp,
    primary key (id)
);
