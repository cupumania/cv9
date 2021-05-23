# cv9
cv9 test bed

**Q1 ANSWEAR**
I used octoparse dan webautomation for solved this matter.

As for octoparse this is a desktop prgram you must be install
and for webautomation is a web base program.
Both are free for limited fiture and must be register.



Q2 ANSWEAR 
-----------
precondition:
- I used MySQL v5.7 for windows
- Launch the MySQL Command-Line Client with this:
  mysql -u pepen -p
- type the password

1. Create database with this code at mysql command line:
  CREATE DATABASE _cv9_test;

2. Activated the newly database:
  use _cv9_test;

3. Create table users:
CREATE TABLE users (
  user_id INT NOT NULL,
  email VARCHAR(50) NOT NULL,
  password VARCHAR(40) NOT NULL,
  name VARCHAR(50) NOT NULL,
  token VARCHAR(64),
  token_created_at TIMESTAMP NULL DEFAULT NULL,
  token_updated_at TIMESTAMP NULL DEFAULT NULL,
  created_at TIMESTAMP NULL DEFAULT NULL,
  updates_at TIMESTAMP NULL DEFAULT NULL,
  PRIMARY KEY(user_id)
);

4. Create table user_balance:
CREATE TABLE user_balance (
  balance_id INT NOT NULL,
  user_id INT NOT NULL,
  institution_name ENUM ('BCA','BNI','MANDIRI','BRI'),
  entry_type ENUM ('DEBIT', 'CREDIT'),
  entry_decription TEXT,
  created_at TIMESTAMP NOT NULL,
  PRIMARY KEY(balance_id),
  FOREIGN KEY(user_id) REFERENCES users(user_id)
);

3. Query for Q2a:
SELECT user_id,token,(token_updated_at-token_created_at) AS token_expires FROM users WHERE user_id=1;

4. Query for Q2b:
SELECT a.user_id,name,institution_name,entry_type FROM users a
LEFT JOIN user_balance b ON a.user_id = b.user_id
GROUP BY institution_name, user_id

Open the files *.py with IDLE Python and running
