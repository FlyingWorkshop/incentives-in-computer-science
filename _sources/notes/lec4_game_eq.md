# Equilibria in Games

In the mechanisms so far (except hospitals in Deferred Acceptance),
agents had dominant strategies (best responses regardless of others'
actions).Today, we analyze what agents should do when there is no
dominant strategy.

```{prf:example}
Kicker can kick left or right. Goalie can jump left or right. Probabilities of scoring are in the following table:

|             | Kick Left | Kick Right |
|-------------|:---------:|:----------:|
| Jump Left   |   $0.5$   |   $0.8$    |
| Jump Right  |   $0.9$   |   $0.2$    |


If the kicker kicks left, the goalie wants to jump left. But then, the
kicker would want to kick right. Repeating this reasoning, there is no
pure strategy equilibrium.
```

```{prf:proof}
*Solution.* Assume we have: kick left/right with probability $0.6,0.4$
and jump left/right with probability $0.7,0.3$. Then the expected change
to get a goal kicking left and kicking right are both $0.62$. Expected
chance to let a goal in jumping left and jumping right are both $0.62$.
As such, neither the kicker nor the goalie has an incentive to deviate
from their mixed strategies. 
```

```{index} Pure Strategy
```
```{prf:definition} Pure Strategy
:label: pure-strategy
A pure strategy fully specifies how a player will play a game. Similar
to a policy in RL and sequential decision making.
```

```{index} Strategy Set
```
```{prf:definition} Strategy Set
:label: strategy-set
A player's strategy set is the set of pure strategies available to a
player
```

```{index} Mixed Strategy
```
```{prf:definition} Mixed Strategy
:label: mixed-strategy
A mixed strategy is a probability distribution over pure strategies.
```

```{index} Nash Equilibrium
```
```{prf:definition} Nash Equilibrium
:label: nash-equilibrium
A profile of (possibly randomized) strategies such that no player has
any profitable deviation keeping the other players' strategies fixed.
Equivalently, a pair of (possibly randomized) strategies, such that
neither player has an incentive to deviate.
```

## Equilibrium in 2-Player Zero-sum Games

Assumptions: (1) $2$ players and (2) the sum of payoffs for players one
and two is always equal to zero (zero-sum game).

Let $S_1$ denote player one's strategy space and let $S_2$ denote player
two's strategy space. Also, let $u(s_1,s_2)$ denote player one's payoff
(so player two's payoff is $-u$). Then, player one solves

$$\max_{s_1 \in S_1} \min_{s_2 \in S_2} u(s_1,s_2)$$ 

while player two solves 

$$
\min_{s_2 \in S_2} \max_{s_1 \in S_2} -u(s_1,s_2).
$$

```{prf:theorem}
In a two player zero-sum game, the max-min payoff for player one is
equal to the Nash equilibrium payoff, which is equal to the min-max
payoff for player two (von Neumann, 1928).
```

```{prf:proof}
 Comes from linear programming and duality (similar to the
equivalence between max-flow and min-cut from 161). Can also be derived
from the Min-Max Theorem of VNM. 
```

## Aside: Max-Min Strategies

For more, see presentation from KLB at UCB.

```{index} Extensive Form Game
```
```{prf:definition} Extensive Form Game
:label: extensive-form-game
Extensive form games have the following:

-   Game Node: possible current states of the game.

-   Game Tree: graph representing which game nodes are reachable from
    which other game nodes.

-   Information Set: all game nodes consistent with/indistinguishable
    from my current node given my information.
```

Even though linear programming is "fast", it's not so nice in actual
play.

```{prf:example}
Consider "Heads Up" two player poker. There are $10^161$ states which
would be impossible to compute explicitly. Due to incomplete
information, it does not suffice to only compute what happens at the
current state (since my beliefs about what my opponents will do depends
on their beliefs of what hand I have, which includes off-path
possibilities).

**Insight 1: blueprint.** Can use 50TB space to store a single
approximation strategy ($10^13$ states). Use this approximation strategy
to play the current hand.

**Insight 2: regret minimization.** Define regret to be the payoff lost
from not taking some action in hindsight. The regret minimization
algorithm plays the game repeatedly, updating strategy so

$$\frac{\text{regret}}{\text{number of games}} \to 0.$$

```

```{prf:theorem}
In two-player zero-sum games, both players using regret minimization
converges to Nash equilibrium.
```

## Nash Equilibrium in (non-zero sum) Games

Suppose the goalie tries to maximize the probability of a save minus the
probability of a goal, so they goalie's payoffs are now

|             | Kick Left | Kick Right |
|-------------|:---------:|:----------:|
| Jump Left   |  $-0.1$   |  $-0.8$    |
| Jump Right  |  $-0.9$   |   $0.4$    |


Good news:

```{prf:theorem}
In every finite game there exists a Nash equilibrium in possibly
degenerate mixed strategies.
```

Bad news:

-   Not equal to max-min/min-max payoffs;

-   Not unique;

-   Not approached by regret minimization;

-   Intractable to compute, even approximately;

-   Some mixed strategy equilibria don't make sense.

```{prf:example}
Two people do a group project. Grades are assigned as follows:

1.  You send $x \in \{2,\dots,99\}$ and your partner sends $y$ from the
    same set.

2.  Assign grades by:

    -   If $x = y$ then your grade is $x$;

    -   If $x < y$ then your grade is $\min \{x,y\}+2$;

    -   If $x > y$ your grade is $\min \{x,y\}-2$.

Unique Nash equilibrium: $x = y = 2$. Game theorists call this the
"Traveler's Dilemma Game."
```

```{prf:example}
Consider two cars arriving at an intersection. Payoffs are:

|       |   Go     |  Wait  |
|-------|----------|--------|
|  Go   | $(-99,-99)$ | $(1,0)$ |
| Wait  |   $(0,1)$   | $(0,0)$ |


-   Two asymmetric equilibria: (Go, Wait) and (Wait, Go).

-   Symmetric equilibrium: Both go with one percent chance and wait with
    one percent chance.

-   Correlated Equilibrium: (Go, Wait) with fifty percent chance and
    (Wait, Go) with fifty percent chance.
```

```{index} Correlated Equilibrium
```
```{prf:definition} Correlated Equilibrium
:label: correlated-equilibrium
A correlated distribution of actions that every player would rather
follow (e.g., a stop light)
```

Good news about correlated equilibria:

-   Can be computed efficiently (through linear programming or regret
    minimization).

-   If everyone runs regret minimization, play converges to the set of
    correlated equilibria (cannot converge to a correlated equilibrium
    itself without a correlating device).

Bad news:

-   Just like Nash eq, sometimes it's not unique or doesn't make sense.

-   Not an equilibrium without a correlating device.

What happens if there is commitment? EG intersection game except the
opponent is a dog who will always play go. Then, you will always choose
to wait for the dog to go first.

```{index} Stackelberg Equilibrium
```
```{prf:definition} Stackelberg Equilibrium
:label: stackelberg-equilibrium
Strategy profile (Leader's strategy, Follower's strategy) such that

1.  Follower's strategy is optimal given Leader's strategy;

2.  Payoff is optimal for leader among all pairs satisfying $\#1$.[^1]
```

```{prf:remark}
The Leader's strategy may be a sub-optimal response to follower's
strategy. However, commitment power means that the leader's Stackelberg
Equilibrium is greater than their utility in any correlated equilibrium.
Finally, the follower's strategy is deterministic without loss of
generality (so there exists an efficient linear programming alg to solve
this).
```

```{prf:example}
Defenders commit to defense strategy (and is a leader); attackers can
plan attack after observing defenders' strategies. Some settings:

-   Airport security

-   Infrastructure

-   Cyber-security

-   Anti-Poaching
```

[^1]: Strong vs Weak Stackelberg: which way we break follower
    indifference against or for the leader.