# Count complete solutions, ie. a \begin{solution} and \end{solution} pair with
# no todo comments inbetween.

/begin{solution}/ { todo = 0; }
/TODO/ { todo += 1; }
/end{solution}/ {
  if (todo == 0) complete += 1
  todos += todo
}

END { print complete, todos }
