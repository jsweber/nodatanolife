create table user(
	user_id int auto_increment primary key,
    username varchar(45) not null,
    password_hash varchar(128),
    telephone varchar(45),
    email varchar(45),
    gender int,
    index(email)
);