SELECT q.q_id
FROM questions AS q
INNER JOIN answered_questions AS a
ON q.q_id = a.q_id
WHERE a.u_id = u
AND q.level = n
AND a.answer = false;

-- select all questions that have not been answered by a user with n = user_id and n = level
SELECT q.q_id FROM questions AS q WHERE q.level = n EXCEPT SELECT a.q_id FROM answered_questions AS a WHERE a.u_id = u;

-- select all questions that have been answered false (a.answer = false) by a user with n = user_id
SELECT q_id FROM answered_questions WHERE answer = false AND u_id = 1;
-- select all questions that have been answered false (a.answer = false) by a user with n = user_id and n = level
SELECT q.q_id FROM questions AS q INNER JOIN answered_questions AS a ON q.q_id = a.q_id WHERE a.answer=false AND a.u_id=1 AND q.level=1;

-- select question and solution for a q_id
SELECT q.q_id, q.level, q.question, s.a, s.b, s.c, s.correct_answer, t.name FROM questions AS q INNER JOIN solutions AS s ON q.s_id = s.s_id INNER JOIN topics AS t ON q.t_id = t.t_id WHERE q.q_id = 1;
