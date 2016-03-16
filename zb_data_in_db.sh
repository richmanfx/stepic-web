#!/bin/sh

# Внесение проверочных данных в базу

mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_question(title, text, rating, author_id) VALUES ('title1', 'question1', 2, 1)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_question(title, text, rating, author_id) VALUES ('title2', 'question2', 4, 1)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_question(title, text, rating, author_id) VALUES ('title3', 'question3', 6, 1)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_question(title, text, rating, author_id) VALUES ('title4', 'question4', 8, 1)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_question(title, text, rating, author_id) VALUES ('title5', 'question5', 10, 1)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_question(title, text, rating, author_id) VALUES ('title6', 'question6', 12, 2)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_question(title, text, rating, author_id) VALUES ('title7', 'question7', 14, 2)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_question(title, text, rating, author_id) VALUES ('title8', 'question8', 16, 2)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_question(title, text, rating, author_id) VALUES ('title9', 'question9', 18, 2)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_question(title, text, rating, author_id) VALUES ('title10', 'question10', 20, 2)"

mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_answer(text, question_id, author_id) VALUES ('answer1',1,1)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_answer(text, question_id, author_id) VALUES ('answer1',1,1)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_answer(text, question_id, author_id) VALUES ('answer1',1,1)"

mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_answer(text, question_id, author_id) VALUES ('answer2',2,2)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_answer(text, question_id, author_id) VALUES ('answer2',2,2)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_answer(text, question_id, author_id) VALUES ('answer2',2,2)"
                                                                                                             
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_answer(text, question_id, author_id) VALUES ('answer3',3,3)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_answer(text, question_id, author_id) VALUES ('answer3',3,3)"
mysql -p2468 -u root -e "use ask_db; insert into ask_db.qa_answer(text, question_id, author_id) VALUES ('answer3',3,3)"
