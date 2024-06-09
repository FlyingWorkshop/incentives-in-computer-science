# Top Trading Cycles

From before, we had two mechanisms for two different models of matching:

-   Random Serial Dictatorship for one sided matching;

-   Deferred Acceptance for two sided matching.

```{prf:remark}
Clarification: Strategyproofness is a guarantee against a single agent
deviating from a truthful strategy. It is does not say anything about
collusion. A mechanism can be strategyproof but not collusion-proof.
```

This lecture: what happens if people are already endowed with a good?
For instance, Stanford PhD students are allowed to renew housing every
year. However, they can re-enter the lottery at a low priority if they
choose not to renew. The issue: students might get a room worse than
their current room if they enter the lottery. This mechanism is not
strategyproof and leads to sub-optimal assignments.

```{index} Top Trading Cycles
```
```{prf:algorithm} Top Trading Cycles
:label: top-trading-cycles
Top Trading Cycles Input: $n$ students and $n$ rooms; each student has a
current room and preferences over all $n$ rooms.\
 \
While there are still unmatched students and rooms:

1.  Create a graph with each unmatched room being a node and each
    unmatched student being a node;

2.  Draw a directed edge from each room to the student that owns the
    room;

3.  Draw a directed edge from each student to their most preferred
    available room;

4.  Remove any cycles that form and trade along the directed edges.
```

We call this problem the *housing assignment problem with
**incumbency***.

```{index} Directed Bipartite Graph
```
```{prf:definition} Directed Bipartite Graph
:label: directed-bipartite-graph
Informally, a directed bipartite graph is a graph with directed edges
(arrows) and two disjoint groups (the two sides in a market, e.g.,
students and houses)
```

```{prf:theorem}
Top trading cycles runs in $O(n^2)$ time, where $n$ is the number of
students/rooms.
```

```{prf:proof}
 Constructing the graph takes $O(n)$ time. Drawing edges also
takes $O(n)$ time. To find cycles, we can start at any node and follow
the path traced by directed edges. Since every node has an
outward-facing directed edge and there are a finite number of nodes, we
will eventually visit some node twice; this gives a cycle.[^1] We need
to pass through at most $2n+1$ nodes so finding a cycle will take $O(n)$
time. Finally, every run of the while-loop removes at least one student
so there are $O(n)$ iterations. As such, total runtime is
$$(O(n)+O(n)+O(n)) \cdot O(n) = O(n^2).$$ 
```

```{prf:proof}
 To find all cycles, we run the strongly connected components
(SCC) algorithm.[^2] (Lemma: Every SCC with vertex $>1$ is a cycle). So
each iteration runs in $O(n)$ time. Each iteration removes $\geq 1$
students, so at most $O(n)$ iterations total. Total running time:
$O(n^2)$. 
```

```{prf:remark}
Since each of the $n$ students reports a preference list of length $n$,
input size is $n^2$ so runtime is linear in input size.
```

```{index} Individually Rational
```
```{prf:definition} Individually Rational
:label: individually-rational
A mechanism is individually rational if no agent is worse off after
participating in the mechanism.
```

```{prf:theorem}
The top trading cycles mechanism is individually rational.
```

```{prf:proof}
 A student trades their room if and only if they are getting a better room. 
```

```{prf:theorem}
Top trading cycles is strategyproof.
```

```{prf:proof}
**Claim 1:** In either run (true or strategic), if $u$ points at $v$ at
any point in the algorithm, it continues to point at $v$ until $v$ is
matched.

Define $X:=\text{first time Bee matches with either run}$.

**Claim 2:** In both runs (true and strategic), the algorithm makes the
same matches until $X$.

**Proof:** By induction. At each iteration, if the available
students/rooms from previous iterations are the same (by induction
hypothesis), and if it doesn't match Bee in that iteration, it doesn't
matter what Bee reports.

**Claim 3:** In both runs, right before $X$, Swamp is unmatched.

**Proof:** In the misreported run it is unmatched because Bee is still
unmatched, and eventually Bee matches to Swamp. Therefore by Claim 2 it
is also unmatched in the run with true preferences.

**Claim 4:** Bee matches in the strategic run before it matches in the
true run.

**Proof:** By Claim 3, right before time $X$, Swamp is still available.
Therefore Bee cannot be pointing at a worse room at time $X$. Therefore
$X$ is the time when Bee matches in the strategic run.

**Claim 5:** In both runs, at time $X$ there is a path from Swamp to
Bee.

**Proof:** In the strategic run, by Claim 4, at time $X$ Bee matches
with Swamp, therefore there must be a path from Swamp to Bee. Therefore
by Claim 2 the path is also there in the true run.

**Claim 6:** In the true run, Swamp is still available when Bee matches.

**Proof:** By Claim 1 the path from Swamp to Bee stays in the graph
until Bee matches.
```

```{prf:theorem}
The TTC allocation is Pareto-optimal.
```

```{prf:proof}
 The TTC allocation is the same as ordering students by
iteration when they form a cycle (breaking ties arbitrarily) and then
running serial dictatorship in that order as every student gets their
most preferred room at the time they form a cycle.

We know that serial dictatorship is Pareto-optimal. 
```

## Top Trading Cycles and Chains

What happens when a student graduates? They give up their old room but
do not enter the market for new rooms. Similarly, there can be new
students that do not yet have a room. Solution: combine ideas from TTC
and RSD to get "You want my house, I get your turn".

```{index} Top Trading Cycles With Chains
```
```{prf:algorithm} Top Trading Cycles With Chains
:label: top-trading-cycles-with-chains
Top Trading Cycles with Chains

1.  Process all students in random order.

2.  In student $i$'s turn, mark $i$ as visited and\...

    1.  If $i$'s top available room is unoccupied, assign that room to
        $i$ and free $i$'s old room.

    2.  Else-If the top available room is occupied by an *unvisited*
        student $j$, move $j$ before $i$ in the order.

    3.  Else-If the top available room is occupied by a *visited*
        student $j$, we have found a cycle.
```

This new mechanism still has the same nice properties: it's
strategyproof, Pareto-optimal, individual rational, and has good
runtime.

## TTC(C) in Practice

Why is TTCC not used in practice? Running it once is strategyproof, but
running it over multiple years is not. Students may try to get a popular
room that they do not like to use it to get an even more preferred room
the year after. This increases demand for perceived "popular" rooms even
more.

Another application: school choice. New Orleans Recovery School District
used TTC to assign K and 9-th grade students to schools in 2011-12. In
public schools, some students have priorities (they have a sibling at
the school or are in the district) that they can own and use to trade
for in TTC. Next year, they switched to Deferred Acceptance. Explanation
given by the board meeting was that DA is simpler to explain to parents
and students. DA also has good publicity (2012 Nobel prize).

College admissions are different: universities have preferences over
applicants that are a better fit. As such, it doesn't make much sense to
allow a Stanford admit to trade their admission for a Harvard
admittance.

Kidney transplants: over 100,000 people on the waitlist for a kidney
transplant. Most humans have two healthy kidneys and can donate one
before they die. However, there are blood type and other biological
compatibility issues so even if a patient has a willing donor, it could
be the case that the donor cannot donate to the patient.

Solution: kidney exchange, if patient $x$'s donor can donate to patient
$y$ and patient $y$'s donor can donate dto patient $x$, then the two
patient-donor pairs can swap donors. Some other concerns in this
setting:

-   Strategyproofness is less of a concern: preferences are more
    determined purely based on blood type, etc. than personal
    preferences.

-   People who are closer to death could have a higher priority.

-   Not a repeated game, won't re-donate a received kidney.

-   Stability and incentivizing people to join the central mechanism is
    more important.

However, there is a logistical challenge with long cycles: an entire
cycle has to be operated on simultaneously. If not, one donor could
change their mind or get ill and a patient who's donor has already
donated would be left without a kidney. On the other hand, long chains
are fine. Some other considerations:

-   Dynamic problem: donors and patients arrive and leave over time and
    in an uncertain manner.

-   Strategic hospitals: some hospitals might want to match kidneys
    internally (due to publicity or financial incentives). When this
    happens, the mechanism is not stable.

-   High failure probability: $93\%$ of matches actually fail (more
    compatibility issues are tested, donor illness, etc.).

-   Ethical concerns: should we prioritize any patients over another?

-   Multi-Organ exchange: trade a piece of liver for a kidney.

```{prf:practice}
More notes in the [ECON 136 course
reader](https://flyingworkshop.github.io/market-design/book/house-allocation-and-kidney-exchange.html?highlight=top+trading#top-trading-cycles).
Practice exercises
[here](https://flyingworkshop.github.io/market-design/book/practice.html).
```

[^1]: To formalize this, we can use the pigeonhole principle: take a
    path of length $2n+1$; there are a total of $2n$ nodes so at least
    one node must have been visited twice or more.

[^2]: Tarjan's algorithm runs in $O(|V| + |E|)$, but every node has
    degree at most $2$, so $|E| \leq |2V|$ and complexity is $O(n)$
    where $n = |V|$.