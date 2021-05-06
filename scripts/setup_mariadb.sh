
service mysql start

DATABASE=MentorMatching
USER=mmDev
PW=MentorMatching!@

mysql -e "CREATE DATABASE ${DATABASE} /*\!40100 DEFAULT CHARACTER SET utf8 */;"
mysql -e "CREATE USER ${USER}@localhost IDENTIFIED BY '${PW}';"
mysql -e "GRANT ALL PRIVILEGES ON ${DATABASE}.* TO '${USER}'@'localhost';"
mysql -e "FLUSH PRIVILEGES;"