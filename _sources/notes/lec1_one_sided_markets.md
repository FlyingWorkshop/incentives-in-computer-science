# One-Sided Matching

Model:
- there are $n$ students, each with some preference over residences
- there are $m$ dorms, each with some capacity

We want to assign students to dorms. One possible solution is to
maximize the sum of utilities:

```{prf:axiom} Utility Maximization

1.  Create a bipartite graph with one side being students and the other side being residencies with with edges from students to dorm with edge weight equal to how much student $i$ likes dorm $j$

2.  Find the max-weight matching (i.e., [Hungarian Algorithm](https://en.wikipedia.org/wiki/Hungarian_algorithm))
```

```{question}
How does the algorithm determine how much each student likes each residency? Only the students themselves knows how much they
like each dorm, so we need to rely on students to tell the algorithm.
```

The issue: each student has an incentive to exaggerate how much they
like their favorite dorm and undercut how much they like other dorms.

As such, finding the matching that maximizes happiness was the right
solution concept, but failed to take incentives into account. Another
possible algorithm is serial dictatorship:

```{prf:axiom} Serial Dictatorship

1.  Students are sorted by some fixed order (random, seniority,
    alphabetically, etc.)

2.  Go through the list in order and each student selects their most
    preferred available dorm
```

Is this any better? There can still be students who are unhappy with their result under serial dictatorship.

```{prf:definition}
A mechanism consists of three things: a method of collecting inputs from
agents, an algorithm that acts on the inputs, and an action that is
taken based on the output of the algorithm.
```

```{prf:remark}
All three components are important: for instance, students' beliefs of
how the algorithm works or how the action is taken would affect how they
respond to the way inputs are collected.
```

## Properties of Serial Dictatorship

```{prf:definition}
:label: strategyproof_label
A mechanism is strategyproof if it is in every agent's best interest to
act truthfully.
```

```{prf:definition}
A mechanism is dominant strategy incentive compatible if it is a dominant strategy for each participant to act truthfully. In particular, this means that being truthful is a best response to any possible strategy profile of other players.
```

```{prf:theorem}
The Serial Dictatorship mechanism is dominant strategy incentive
compatible: it is in every student's best interest to choose their
favorite available dorm in their term.
```

```{prf:proof}
 Your room choice will not affect what rooms are available by
the time your turn comes. When it gets to your turn, what you choose is
what you get, so it is best to choose your favorite room among available
options. 
```

```{prf:definition}
An outcome $O'$ is a Pareto improvement over outcome $O$ if all agents
either strictly prefer $O'$ to $O$ or are indifferent between the two,
with at least one strict preference.
```

```{prf:definition}
An outcome $O$ is Pareto optimal if there are no Pareto improvements
from $O$.[^1]
```

In other words, an outcome is Pareto optimal if you can't make anyone
happier without making someone sadder.

```{prf:theorem}
The outcome under serial dictatorship (with any ordering of students) is
Pareto optimal.[^2]
```

```{prf:proof}
 Let the serial dictatorship outcome be $O$. Towards a
contradiction, suppose $O$ is not Pareto optimal, and there exists some
outcome $O'$ that is a Pareto improvement over $O$. Consider the first
student that gets a different outcome under $O$ and $O'$. Since all
students before this student are assigned the same room, the set of
available rooms for this student is the same under $O$ and $O'$.
However, the student chooses their favorite room under $O$, so the room
they receive under $O'$ must be worse. 
```

One issue with this: dictatorship can have a large affect on others.
Suppose there are ten students and the first eight have chosen rooms $1$
to $8$. Also, suppose student nine has room $9$ as their $9$th favorite
room and room $10$ as their $10$th favorite room while student ten has
room $9$ as their favorite room and room $10$ as their least favorite
room. If student nine chooses room $9$ over room $10$ they only gain a
small improvement, but student ten is now forced to pick room $10$ over
room $9$ which is a large jump in their preferences.

[^1]: Pareto Optimality must be defined with respect to particular
    preferences. As such, it is difficult to conceptualize if an outcome
    is Pareto optimal if truthful preferences are unknown.

[^2]: This result only holds if every students' preferences over dorms
    is strict (no student can be indifferent between dorms).