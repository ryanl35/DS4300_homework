drop schema if exists foodpool;

create schema foodpool;

use foodpool;


create table communities
(
zipcode			VARCHAR(5)		UNIQUE,
comm_name		VARCHAR(50),

    CONSTRAINT communities_pk
		PRIMARY KEY (zipcode)
);

create table users
(
user_id		INT		UNIQUE	AUTO_INCREMENT,
user_name	VARCHAR(40),
verified	CHAR(1),
zipcode		VARCHAR(5),

    CONSTRAINT user_pk
		PRIMARY KEY(user_id),
    CONSTRAINT user_fk_communities
		FOREIGN KEY (zipcode)
		REFERENCES communities (zipcode)
		ON DELETE CASCADE
);

create table posts
(
post_id		INT				UNIQUE,
food_name	VARCHAR(50),
food_descr	VARCHAR(300),
food_price	INT,
user_id		INT,

	CONSTRAINT posts_pk
		PRIMARY KEY(post_id),
    CONSTRAINT posts_fk_users
		FOREIGN KEY (user_id)
		REFERENCES users (user_id)
		ON DELETE CASCADE
);

SELECT * FROM communities;
SELECT * FROM users;
SELECT * FROM posts;




