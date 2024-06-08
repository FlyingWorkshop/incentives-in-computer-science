# Envy and Fairness

Consider cake cutting: Alice and Bob want to split a cake, and the cake
has different toppings (strawberries, chocolate, etc.) over different
regions. One canonical mechanism is I-cut-you-choose:

1.  One agent cuts the cake;

2.  The other picks which slice they want;

3.  First agent gets the remaining cake.

```{prf:proposition}
I-cut-you-choose is not dominant-strategy incentive compatible for the
cutting agent but is for the choosing agent.
```

```{prf:proof}
 The cutter's optimal strategy depends on the chooser's
preferences. The chooser directly chooses their outcome. 
```

Why, has this mechanism been used? There is some notion of fairness in
this:

```{prf:definition}
An allocation is envy-free if no agent envies another agent's
allocation.
```

```{prf:proposition}
The I-cut-you-choose mechanism can always lead to an envy-free
allocation for both players.
```

```{prf:proof}
 The cutter can always cut the cake into two pieces that are
equal in their perspective, so no matter which slice they get the
allocation is envy-free for them. Then, the choose chooses their
favorite slice, so it clearly is envy-free for them. 
```

## Formalizing Fair Allocations

Goal: from a set of items $A$, choose some allocation for each of $n$
agents. Each agent $i$ has a valuation function
$v_i: \mathcal{P}(A) \to \mathbb{R}$. Then, there are several measures
of fairness (defined in this setting):

-   Envy-Free: for all $i,j$ we have $v_i(A_i) \geq v_i(A_j)$;

-   Proportional: for all $i, v_i(A_i) \geq v_i(A)/n$;

-   Equitable: for all $i,j$ we have $v_i(A_i) = v_j(A_j)$;

-   Perfect: for all $i, v_i(A_i) = v_i(A)/n$.

Another possibility: competitive equilibrium from equal incomes, which
is similar to competitive equilibrium except give everyone a "fake
dollar" to spend.

In cases with indivisible goods, often none of them can be satisfied. In
particular, if there is a single good (and both individuals gain
strictly positive utility from it), none of these can be satisfied. A
compromise:

```{prf:axiom}
Maximin Share (MMS)

1.  Each agent $i$ proposes an allocation $A^1$ to all agents;

2.  The MMS condition is $$v_i(A_i) \geq \max_{A^i} \min_j v_i(A_j^i)$$.
```

Another compromise can be to approximately satisfy these conditions: let
$\overline{a}$ be the best item and $\underline{a}$ be the worst item.
Then,

1.  Envy free up to one item:
    $v_i(A_i) \geq v_i(A_j \setminus \overline{a})$;

    -   Can always be satisfied.

2.  Envy free up to any item:
    $v_i(A_i) \geq v_i(A_j \setminus \underline{a})$

    -   Open problem for whether or not this can always be satisfied.

3.  $\alpha$-Maximin Share:
    $v_i(A_i) \geq \alpha \max_{A^i} \min_j v_i(A_j^i)$

    -   Can always be satisfied for $\alpha \leq 3/4$.

4.  Approximate competitive equilibrium from equal incomes: only require
    approximate equilibrium.

    -   Can always be satisfied but computationally difficult to compute

Finally, we can directly seek to maximize some "fair" measure of overall
utility. Some examples are:

1.  Utilitarian/Social Welfare: $\max_{A_1,...,A_n} \sum_i v_i(A_i)$;

2.  Nash social welfare: $\max_{A_1,...,A_n} \prod_i v_i(A_i)$;

    -   Middle ground between Utilitarian and Egalitarian.

    -   Competitive equilibrium from equal incomes maximizes Nash social
        welfare;

3.  Egalitarian/maximin: $\max_{A_1,...,A_n} \min_i v_i(A_i)$.

## Dominant Resource Fairness

Suppose there are $m$ resources with fixed capacities and $n$ users that
want to run as many identical tasks as possible. Each task demands some
vector of resources to run. For now, suppose resources are
infinitesimally small. How can resources be allocated fairly and
efficiently without transfers?

For any allocation, each user has some fraction of total capacity of
each resource (given by point-wise division of the user's usage vector
by the capacity vector). Then, a user's dominant resource is the
resource they have the highest fraction of usage of. Dominant resource
fairness requires equal shares of dominant resources.

```{prf:axiom}
Algorithm to get DRF Allocation

1.  Every agent submits their ratio of demands;

2.  Algorithm computes the maximal allocation subject to DRF.
```

```{prf:proposition}
Every user prefers the DRF allocation to just getting $1/n$ of every
resource.
```

```{prf:proof}
 As the allocation is maximal, some resource $j^*$ is exhausted
so some agent $i^*$ gets at least $1/n$ of $j^*$. Then, each agent has
at least $1/n$ of their dominant resource. 
```

```{prf:proposition}
The DRF mechanism is envy-free.
```

```{prf:proof}
 If $i$ envies $j$, then $j$ must have more of every resource so
in particular, $j$ must have more of $i$'s dominant resource than $i$
does, a contradiction. 
```

```{prf:proposition}
The DRF mechanism is Pareto-optimal and strategyproof.
```

```{prf:proof}
 Pareto-Optimal: As the allocation is maximal, some resource ie
exhausted and no agent can be made happier without making some other
agent sadder.

Strategyproof: for any misreport, Pareto-optimality of the allocation
reached by truthful reporting means that less of the dominant resource
is received. 
```

## DRF in Practice

Some of the assumptions made during the setup might break:

1.  Tasks are not identical, arrive over time, and depart;

    -   While resources are not exhausted, select user $i$ with minimal
        dominant share and add their next feasible task. Not
        strategyproof (can clump tasks together) but works well in
        practice.

2.  Tasks might have flexibility in resource use;

3.  Tasks might have more specific criteria;

4.  Tasks not infinitesimally small;

5.  Users might have different priority levels;

    -   Weighted DRF.

6.  Some tasks have zero demand for some resources.

    -   Find the maximal DRF allocation and then recurse on remaining
        feasible tasks.