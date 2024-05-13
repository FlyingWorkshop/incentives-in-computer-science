# Market Equilibrium

Previously, we studied situations with no transfers:

1.  If Stanford housing auctioned rooms, the distribution would look
    much different.

2.  It is illegal in all countries (except Iran) to buy organs.

3.  Hospitals and students matching with money is subject to anti-trust
    laws.

However, there are issues to restricting markets to operating without
money.

1.  Can only work with ordinal opposed to cardinal preferences.

2.  Underground markets may arise (college admissions scandals, black
    markets for kidneys).

3.  Could be issues with permissions (entering donor lists multiple
    times using bots to try to get a match earlier).

```{prf:definition}
We have covered four types of game equilbiria:

-   Nash

-   Correlated

-   Stackelberg

-   Subgame Perfect Equilibrium (SPE)

Today, we begin covering *market equilibria*.
```

```{prf:definition}
There are two main ways to model utility:

-   Cardinal: assigns some numeric value to how much someone likes
    something.

-   Ordinal: comparison-based, only assigns some order.

Cardinal utilities tell us more (we can always extract ordinal utilities
from cardinal utilities, but not the other way around) but humans think
more in terms of ordinal rankings. Cardinal utilities are also easier to
work with when doing expected utility calculations and can be normalized
to be in terms of (usually but not always) money.
```

```{prf:definition}
There are two types of goods:

-   Fungible goods have many interchangeable units for sale.

-   Idiosyncratic goods are unique.

Many goods are somewhere in between: rides on ride-sharing apps are
fungible in terms of how the driver doesn't matter too much, but can
also be idiosyncratic in terms of caring about where you go.
```

```{prf:definition}
From economics,

-   A demand curve plots the total quantity of a good consumers are
    willing to buy at all price levels.

-   A supply curve plots the total quantity of a good firms are willing
    to sell at all price levels.

By tradition, price is plotted on the $y$-axis and quantity is plotted
on the $x$-axis.
```

```{prf:remark}
In general, demand is downward sloping (higher quantity demanded as
price decreases) and supply is upwards sloping (lower quantity supplied
as price decreases). However, this is not always the case (different
market structures like a monopoly, weird classes of goods).
```

```{prf:definition}
The price where the supply and demand curves meet is called the market
clearing price. At this price, the quantity demanded is equal to
quantity demanded so all interested buyers and sellers can transact (and
hence clear the market).
```

## Unit-Demand Market Model

Setting:

1.  $m$ different (idiosyncratic) goods for sale;

2.  $n$ different buyers that will each purchase at most one good (they
    have unit demand);

3.  Buyer $i$ as value $v_{i,j}$ for purchasing good $j$;

4.  If buyer $i$ pays $p_j$ to acquire good $j$, then their payoff is
    
    $$U_{i,j} = v_{i,j} - p_j;$$

5.  If buyer $i$ doesn't purchase any good, normalize outside utility to be zero: 

    $$U_{i, \varnothing} = 0.$$

The solution concept we will use:

```{prf:definition}
A competitive equilibrium is a price vector $p = (p_1,...,p_m)$ and a
matching $M: \{1,2,...,n\} \to \{1,2,...,m\}$ of buyers to goods such
that:

1.  Each buyer is matched with their favorite good given prices $p$: for
    all $i,j$ we have 
    
    $$v_{i,M(i)} - p_{M(i)} > v_{i,j} - p_j;$$

2.  If no buyer is matched with good $j$ then $p_j = 0$;

3.  Buyer $i$ is unmatched if for all goods $j$, we have
    $v_{i,j} - p_j < 0$.
```

```{prf:remark}
Conditions (1) and (3) implies that buyer $i$ is unmatched if *and only
if* for all goods $j$, we have $v_{i,j} - p_j < 0$. Then, this stronger
condition is equivalent to individual rationality: for all buyers $i$,

$$v_{i,M(i)} - p_i \geq 0.$$

```

In addition to equilibrium, we also care about welfare:

```{prf:definition}
The social welfare of an allocation $M$ is the sum of buyers' values:

$$U(M) = \sum_i v_{i,M(i)}.$$

```

```{prf:remark}
Prices are not included because the total cost to buyers is equal to
total profit of sellers.
```

## Properties of Competitive Equilibrium

```{prf:theorem}
If $(p,M)$ is a competitive equilibrium, then $M$ is a matching that
maximizes social welfare: if $M'$ is any matching, we have

$$\sum_i v_{i,M(i)} \geq \sum_i v_{i,M'(i)}.$$
```

```{prf:proof}
 By the definition of competitive equilibrium, we know


$$\sum_i (v_{i,M(i)}-p_{M(i)}) \geq \sum_i (v_{i,M'(i)}-p_{M'(i)})$$

as
$v_{i,M(i)}-p_{M(i)} \geq v_{i,M'(i)}-p_{M'(i)}$ for all $i$. Then,
$\sum_i p_{M(i)} = \sum_i p_{M'(i)}$ as $M,M'$ are just permutations so
we get 

$$\sum_i v_{i,M(i)} \geq \sum_i v_{i,M'(i)}.$$ 
```

```{prf:theorem}
In the unit-demand market model with finite prices and finite
increments, there will always exist a competitive equilibrium.
```

```{prf:remark}
In more nuanced models, competitive equilibrium does not necessarily
exist.
```

```{prf:proof}
 We will construct a Deferred Acceptance with Prices algorithm
that gets us to competitive equilibrium. For each buyer, construct a
list of all (good, price) options ordered by utility (we can truncate
this list by not including anything worse than (receive nothing, pay
nothing), which is always an option). At each iteration of the
algorithm, every unmatched buyer whose next-favorite option is $(j,p)$
proposes price $p$ to good $j$. Then, good $j$ tentatively accepts $p$
(in the deferred acceptance sense) if it is higher than the prices it
was previously offered. This algorithm will always terminate by the same
reasoning as why deferred acceptance always terminates. The resulting
match and prices when this algorithm terminates is a competitive
equilibrium:

1.  Every buyer is matched with their favorite (good, price) pair as any
    other pair must have led to the buyer being rejected at some
    previous stage.

2.  Each unmatched good has a price of zero as a good is unmatched if
    and only if it was never proposed to.

 
```

```{prf:remark}
DA with prices runs in $O(n \cdot m \cdot k)$ time where $k$ is the
number of price increments.
```

```{prf:proposition}
Deferred acceptance with prices is strategyproof and optimal for buyers.
```

```{prf:proof}
 Follows directly from the same reasoning used to analyze
deferred acceptance. 
```