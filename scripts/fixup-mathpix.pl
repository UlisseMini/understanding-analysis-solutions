#!/usr/bin/env perl

my $exerciseNumber = 0;
my $insideEnum = 0;

sub endExercise {
  if ($insideEnum) { print "}\n"; $insideEnum = 0; }
  print <<EOF;
\\end{exercise}
\\begin{solution}
\\TODO
\\end{solution}
EOF
}

sub beginExercise {
  if ($exerciseNumber > 0) { endExercise; }
  $exerciseNumber += 1;

  # handle edgecase: Exercise 1.2.3 (a) should not be \begin{exercise}[a]
  s/\(a\)/\n(a)/;

  # convert Exercise 1.2.3 (foo) -> \begin{exercise}[foo]
  s/^Exercise \d\.\d\.\d+( \(([^\)]+)\))?\./\\begin{exercise}[$2]\n/;
  s/\\begin{exercise}\[\]/\\begin{exercise}/;
}

while (<>) {
  # $3. 4.5$ -> 3.4.5
  # way harder then it should be
  if (/\$([\d\. ]+)\$/) {
    my $a = $1; my $b = $1; $b =~ s/ //g; s/\$\Q$a\E\$/$b/;
  }

  if (/^Exercise/) { beginExercise; }

  if (s/^\(a\) /\\enum {\n\\item /m) { $insideEnum = 1; }
  s/^\(\w\) /\\item /gm;

  print $_;
}

if ($exerciseNumber > 0) { endExercise; }
