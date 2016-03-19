#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Aleksandr Jashhuk, Zoer, R5AM'
 
import sqlite3 as lite
import sys


#  tables
# qa_question               
# qa_answer                 
# qa_question_likes

'''
CREATE TABLE "qa_question_likes" (
    "id" integer NOT NULL PRIMARY KEY,
    "question_id" integer NOT NULL,
    "user_id" integer NOT NULL REFERENCES "auth_user" ("id"),
    UNIQUE ("question_id", "user_id")
);
CREATE INDEX "qa_question_likes_25110688" ON "qa_question_likes" ("question_id");
CREATE INDEX "qa_question_likes_6340c63c" ON "qa_question_likes" ("user_id");
'''

'''
CREATE TABLE "qa_answer" (
    "id" integer NOT NULL PRIMARY KEY,
    "text" text NOT NULL,
    "added_at" datetime NOT NULL,
    "question_id" integer NOT NULL UNIQUE REFERENCES "qa_question" ("id"),
    "author_id" integer NOT NULL REFERENCES "auth_user" ("id")
);
CREATE INDEX "qa_answer_e969df21" ON "qa_answer" ("author_id");
'''

'''
CREATE TABLE "qa_question" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(255) NOT NULL,
    "text" text NOT NULL,
    "added_at" datetime NOT NULL,
    "rating" integer NOT NULL,
    "author_id" integer NOT NULL REFERENCES "auth_user" ("id")
);
CREATE INDEX "qa_question_e969df21" ON "qa_question" ("author_id");
'''
 
qa_question_data= (
		    (1, 'question 0', 'text 0', '2016-03-17 20:13:21.123456', 0, 1),
		    (2, 'question 1', 'text 1', '2016-03-17 20:13:22.455754', 1, 1),
		    (3, 'question 2', 'text 2', '2016-03-17 20:13:23.234567', 2, 1),
		    (4, 'question 3', 'text 3', '2016-03-17 20:13:24.345678', 3, 1),
		    (5, 'question 4', 'text 4', '2016-03-17 20:13:25.456789', 4, 1),
		    (6, 'question 5', 'text 5', '2016-03-17 20:13:26.567890', 5, 1),
		    (7, 'question 6', 'text 6', '2016-03-17 20:13:27.678901', 6, 1),
		    (8, 'question 7', 'text 7', '2016-03-17 20:13:28.789012', 7, 1),
		    (9, 'question 8', 'text 8', '2016-03-17 20:13:29.890123', 8, 1),
		    (10, 'question 9', 'text 9', '2016-03-17 20:13:30.901234', 9, 1),
		    (11, 'question 10', 'text 10', '2016-03-17 20:13:31.012345', 10, 1),
		    (12, 'question 11', 'text 11', '2016-03-17 20:13:32.123456', 11, 1),
		    (13, 'question 12', 'text 12', '2016-03-17 20:13:33.234567', 12, 1),
		    (14, 'question 13', 'text 13', '2016-03-17 20:13:34.345678', 13, 1),
		    (15, 'question 14', 'text 14', '2016-03-17 20:13:35.456789', 14, 1),
		    (16, 'question 15', 'text 15', '2016-03-17 20:13:36.567890', 15, 1),
		    (17, 'question 16', 'text 16', '2016-03-17 20:13:37.678901', 16, 1),
		    (18, 'question 17', 'text 17', '2016-03-17 20:13:38.789012', 17, 1),
		    (19, 'question 18', 'text 18', '2016-03-17 20:13:39.890123', 18, 1),
		    (20, 'question 19', 'text 19', '2016-03-17 20:13:40.901234', 19, 1),
		    (21, 'question 20', 'text 20', '2016-03-17 20:13:41.012345', 20, 1),
		    (22, 'question 21', 'text 21', '2016-03-17 20:13:42.123456', 21, 1),
		    (23, 'question 22', 'text 22', '2016-03-17 20:13:43.234567', 22, 1),
		    (24, 'question 23', 'text 23', '2016-03-17 20:13:44.345678', 23, 1),
		    (25, 'question 24', 'text 24', '2016-03-17 20:13:45.456789', 24, 1),
		    (26, 'question 25', 'text 25', '2016-03-17 20:13:46.567890', 25, 1),
		    (27, 'question 26', 'text 26', '2016-03-17 20:13:47.678901', 26, 1),
		    (28, 'question 27', 'text 27', '2016-03-17 20:13:48.789012', 27, 1),
		    (29, 'question 28', 'text 28', '2016-03-17 20:13:49.890123', 28, 1),
		    (30, 'question 29', 'text 29', '2016-03-17 20:13:50.901234', 29, 1),
		    (31, 'question last', 'text', '2016-03-17 20:133:52.622587', 0, 1),
)
 
qa_answer_data= (
		    (1, 'answer 0', '2016-03-17 20:13:55.123456', 5, 1),
		    (2, 'answer 1', '2016-03-17 20:13:55.143456', 5, 1),
		    (3, 'answer 2', '2016-03-17 20:13:55.153456', 5, 1),
		    (4, 'answer 3', '2016-03-17 20:13:55.163456', 5, 1),
		    (5, 'answer 4', '2016-03-17 20:13:55.173456', 5, 1),
		    (6, 'answer 5', '2016-03-17 20:13:55.183456', 5, 1),
		    (7, 'answer 6', '2016-03-17 20:13:55.193456', 3, 1),
		    (8, 'answer 7', '2016-03-17 20:13:55.203456', 3, 1),
		    (9, 'answer 8', '2016-03-17 20:13:55.213456', 3, 1),
		    (10, 'answer 9', '2016-03-17 20:13:55.223456', 3141592, 1),
) 
 
con = lite.connect('db.sqlite3')
 
with con:
    cur = con.cursor()
    cur.execute("delete from qa_question where 1;")	# очистить таблицу
    cur.execute("delete from qa_answer where 1;")
    cur.executemany("INSERT INTO qa_question VALUES(?, ?, ?, ?, ?, ?)", qa_question_data)
    cur.executemany("INSERT INTO qa_answer VALUES(?, ?, ?, ?, ?)", qa_answer_data)
