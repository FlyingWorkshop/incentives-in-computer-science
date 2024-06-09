# Two-Sided Matching

After medical school, med students start their internship called a
"residency". Each (prospective) doctor has preferences over hospitals
and each hospital has preferences over doctors. How should doctors and
hospitals be matched?

The biggest difference between residency matching and dorms is that we
now have two sided preferences. Another difference: dorm assignments are
all through Stanford's centralized system, but there is nothing stopping
doctors and hospitals from matching on their own as an outside option.

```{index} Match
```
```{prf:definition} Match
:label: match
Consider a two-sided matching market with $I$
being participants on one side and $J$ being participants on the other
side. Each $i \in I$ has preferences over $J$ and each $j \in J$ has
preferences over $I$. A match $M$ is a function $I \cup J \to I \cup J$
where $M(i) \in J$ is $i$'s match, $M(i) = i$ if $i$ is unmatched; and
$M(j) \in I$ is $j$'s match, $M(j) = j$ if $j$ is unmatched.
```

```{index} Blocking Pair
```
```{prf:definition} Blocking Pair
:label: blocking-pair
Given a match $M$, the pair (doctor $i$, hospital $j$) forms a blocking pair if they prefer each other to
their assignment in $M$.
```

```{index} Stable Matching
```
```{prf:definition} Stable Matching
:label: stable-matching
A matching $M$ is stable if there are no blocking pairs. Equivalently, for every unmatched pair $(i,j)$ it
must be true that either:
-   Doctor $i$ prefers Hospital $M(i)$ over Hospital $j$ or;
-   Hospital $j$ prefers Doctor $M(j)$ over Doctor $i$.
```

## Deferred Acceptance

Main idea behind this algorithm: try to match each doctor to their
favorite choice. If there ever is a blocking pair, switch the matching.
In practice, each hospital accepts more than one doctor. For now, we
assume that each hospital only has one spot (but the algorithm and
results can be extended into the multiple spots case).

```{index} Deferred Acceptance
```
```{prf:algorithm} Deferred Acceptance
:label: deferred-acceptance
While there is an unmatched doctor $i$:

1.  Try to match doctor $i$ with the next-favorite hospital $j$ in their
    list;

2.  If hospital $j$ does not yet have a doctor then hospital $j$ and
    doctor $i$ (tentatively) match and both are happy with this match;

3.  Else-if hospital $j$ is already matched with doctor $i'$ and prefers
    their current match $i'$ to doctor $i$, then doctor $i$ remains
    unmatched;

4.  Else-if hospital $j$ is already matched with doctor $i'$ and prefers
    doctor $i$ to their current match $i'$, then doctor $i$ and hospital
    $j$ match making them both happier off while doctor $i'$ is now
    unmatched.
```

For an example, consider applying deferred acceptance to matching
students to universities. Suppose there were three universities,
Stanford (S), the University of Michigan (M), and Tsinghua (T). Also,
suppose there are three students, Alex (A), Bill (B), and Carl (C).
Suppose students have preferences 

$$
\begin{aligned}
	A: S \succ M \succ T \\
	B: S \succ T \succ M \\
	C: M \succ T \succ S
\end{aligned}
$$ 

and universities have preferences 

$$
\begin{aligned}
	S: B \succ C \succ A \\
	M: A \succ C \succ B \\
	T: A \succ B \succ C
\end{aligned}
$$

In the first round, Alex and Bill both apply to
Stanford. Stanford prefers Bill (to Carl) to Alex so Bill's application
is tentatively accepted. Alex is rejected, and removes Stanford from his
preference list. Only Carl applies to Michigan, so Carl's application is
also tentatively accepted. In the second round, only Alex needs to apply
again, and Alex applies to Michigan. Now, Michigan compares Alex with
Carl (from round one) and likes Alex more, so Alex is now tentatively
accepted and Carl is rejected. As such, Carl strikes Michigan from his
list of acceptable universities. In the third round, Carl applies to
Tsinghua. This is the only application Tsinghua has received, so it is
tentatively accepted. In the next round, there are no rejected students
so no new applications are made. As such, the algorithm finishes. This
process can be summarized in the following table, where green denotes
tentative acceptance and red denotes rejection.

|     | $1$                                  | $2$                                  | $3$                                  |
|-----|--------------------------------------|--------------------------------------|--------------------------------------|
| $A$ | <span style="color:red">S</span>     | <span style="color:green"> M </span> | <span style="color:green"> M </span> |
| $B$ | <span style="color:green"> S </span> | <span style="color:green"> S </span> | <span style="color:green"> S </span> |
| $C$ | <span style="color:green"> M </span> | <span style="color:red"> M </span>   | <span style="color:green"> T </span> |

```{prf:theorem} Runtime of Deferred Acceptance
Deferred Acceptance runs in $O(n^2)$ time.
```

```{prf:proof}
Each iteration of the while loop takes $O(1)$ time. At every
iteration, each doctor proposes to a new hospital. As no doctor and
hospital ever try to match more than one, there are $n^2$ possible
(doctor, hospital) pairs so there are at most $n^2$ iterations. Thus,
overall runtime is $O(n^2)$. 
```

```{prf:theorem} DA is stable
The deferred acceptance algorithm outputs a complete stable matching.
```

```{prf:proof}
 The theorem follows from the following three claims:

1.  At every iteration, the current match is stable with respect to
    non-free doctors and hospitals.

2.  Once a hospital is matched, it remains matched (but possibly to a
    different doctor) until the end of the algorithm

3.  At the end of the algorithm, every doctor and hospital is matched.

**Claim one.** Towards a contradiction, suppose $(d,h)$ is a blocking
pair. Thus, $d$ is currently matched to a hospital worse than $h$. This
implies that $d$ already tried to match with $h$. There are two cases:
either $h$ refused $d$, or $h$ initially matched with $d$ but left them
later. In either case, $h$ is currently matched with a doctor better
than $d$ so $(d,h)$ cannot be a blocking pair.

**Claim two.** Clear from the algorithm: only way for a matched hospital
to change is if there is a better doctor that proposes to them, in which
case they will match with the better doctor.

**Claim three.** Towards a contradiction, suppose $(d,h)$ is free. At
the end of the algorithm $d$ must have proposed to $h$ already, so $h$
must either be matched with $d$ or a doctor better than $d$. In either
case, $(d,h)$ thus cannot be free. 
```

```{prf:theorem} Efficiency of Stable Matchings
Every stable matching is Pareto-optimal.
```

```{prf:proof}
Suppose $A$ is stable and let $B$ be any other matching.
Consider a doctor-hospital pair matched in $B$ but not matched in $A$.
By stability of $A$, either the doctor or hospital (or both) prefers
their match under $A$ to their match under $B$. 
```

There are many possible stable matchings that are possible, but which is
best?

```{prf:theorem} Proposing Optimality
The matching returned by doctor-proposing Deferred Acceptance is doctor-optimal.
```

As a corollary of this result, we have:

```{prf:theorem} Proposing Strategyproofness
Doctor-proposing Deferred Acceptance is strategyproof for doctors.
```

On the other hand, hospitals are not quite as happy with
doctor-proposing deferred acceptance.

```{prf:theorem} Receiving Non-Optimality
The matching returned by
doctor-proposing Deferred Acceptance is the worst stable matching for hospitals.
```

```{prf:theorem} Receiving Non-Strategyproofness
It is not always best for hospitals to truthfully reveal their preferences.
```

## Deferred Acceptance in Practice

Historically, residency matches proceeded as follows:

-   In the 1950's, National Resident Match Program used a
    deferred-acceptance like algorithm. At this time, there were very
    few female or openly gay doctors.

-   In the 1960's, there were more couples that want to be near each
    other. As such, doctors no longer have ranked preferences over
    hospitals: individual preferences now also depends on what your
    partner's outcome is.

-   In the 1980's, negative results were developed:

    1.  A stable matching may not even exist;

    2.  This matching problem is a $NP$-complete computational problem.

-   In the 1990's, an extension of the Deferred Acceptance algorithm
    that resolved the couples issue was put into practice.

How do hospitals rank doctors?

-   Interviews: but this process is costly, as doctors still need to
    strategize over which doctors to interview.

-   Standardized tests: maybe not anymore, since the main test (USMLE)
    changed to pass-fail.

-   Safety choices: hospitals might list some "safety" doctors, but
    using safety choices is never safer for hospitals (this is provably
    true).

```{prf:theorem} No Improvements from Safety Choices
Hospitals
misreporting preferences by moving their $i$th preferred doctor to a
higher position cannot help with matching with doctor of rank $i$ or
better.
```

```{prf:proof}
Until doctor $i$ tries to match with this hospital, the
manipulation has no effect. After doctor $i$ tries to match with this
hospital, they can only be replaced by someone better. As such, either
this hospital would have gotten doctor $i$ anyways, or this hospital is
stuck with doctor $i$ opposed to someone better. 
```

Why do hospitals still use safety picks?

-   Hospitals don't know this theorem.

-   Reputation/ego: hospitals publish a "number needed to fill" number,
    the lowest rank in a hospital's list of a doctor matched to the
    hospital.

Another situation where two-sided matching comes up is in college
admissions: students apply and colleges decide who to accept. In the US,
application fees and the time it takes to write applications restricts
how many applications a student can submit. In other countries, there is
a single standardized test that determines admissions.

Even when there is no outside option, deferred acceptance is fast to run
and is used to match packets to servers.