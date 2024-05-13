# Single-Unit Auctions

Auctions are useful in many situations. For instance, if the price of a
good is unknown (a market for this product, for one reason or another,
might not converge to some equilibrium price) auctions can be useful for
price discovery. For instance:

1.  Monopolies (wireless spectrum auctions);

2.  Niche products (rare used items on eBay);

3.  Product with very specific attributes (ad auctions).

Another situation where auctions are useful is when buyers have the
computational power and patience to bid:

1.  Expensive items (wireless spectrum);

2.  Automated bidders (ad auctions).

There are many interactions between auctions and CS:

1.  Auctions fund a lot of computer scientists (ad auctions);

2.  Fast auctions require algorithmic bidders (ad auctions);

3.  Complex auctions require algorithmic auctioneers.

## Case of One Buyer

Motivation: digital goods. Suppose there is a pool of users subscribed
to a free product. What price should be charged to maximize revenue?

Aggregating users' willingness to pay induces a demand curve for the
good. Then, revenue is equal to the price multiplied by the number of
people with willingness to pay more than that price.

Roger Myerson (1981) showed that given some demand curve $D$, there is a
formula $p(D)$ that maximizes revenue. This is the profit maximizing
price.[^1]

Another motivation: ad auctions with specialized advertisers so only one
advertiser wants each ad spot. Sellers do not know exactly how much an
advertiser is willing to pay, but have prior beliefs over the buyer's
value. In this interpretation, the prior over values can be taken as a
demand curve.

## Case of Multiple Buyers

**Model**:

1.  There is a set of bidders $I$ with each bidder $i$ having a value
    $v_i$ for getting the item.

2.  Each bidder knows their own value, the seller does not know bidders'
    values but has some prior belief over values.

3.  Bidder $i$'s payoff while paying $p_i$ is $v_i - p_i$ if they get
    the item and $-p_i$ otherwise.

We will focus on sealed-bid auctions:

```{prf:axiom}
First-Price Auction

1.  Each bidder submits a bid $b_i$, which is unobserved by other
    bidders;

2.  Highest bidder $i^* = \arg\max_{i \in I}\{b_i\}$ gets the item and
    pays $b_{i^*}$.
```

Immediately, bidders will bid lower than their value $v_i$: for all
$i \in I$ we have that $b_i < v_i$ in equilibrium. Intuitively, we
expect bids to grow up as competition increases.

```{prf:axiom}
All-Pay Auction

1.  Each bidder submits a bid $b_i$, which is unobserved by other
    bidders;

2.  Highest bidder $i^* = \arg\max_{i \in I}\{b_i\}$ gets the item;

3.  *Every* bidder $i \in I$ pays $b_i$.
```

Not used to auctions things in practice, but used to model other
situations (interest groups donating to a politician, animals hunting
for food). In this model, bidders will still bid lower than their value
and will generally bid lower than their first-price value.

```{prf:axiom}
Second-Price Auction

1.  Each bidder submits a bid $b_i$, which is unobserved by other
    bidders;

2.  Highest bidder $i^* = \arg\max_{i \in I}\{b_i\}$ gets the item and
    pays the second highest price $\max_{i \neq i^*} b_i$.
```

```{prf:theorem}
Second-price auctions are strategyproof ao truthful bidding is a
dominant strategy and hence everyone bidding truthfully is an
equilibrium.
```

```{prf:proof}
 Fix all bids of other people $b_j$ for $j \neq i$. We will show
that bidding $b_i = v_i$ is optimal for bidder $i$. Let

$$b^{(-i)} = \max_{j \neq i} b_j.$$ 

There are two cases:

1.  If $v_i < b^{(-i)}$ then $i$ prefers to not win than to pay
    $b^{(-i)}$ so any $b_i < b^{(-i)}$ is optimal. In particular,
    $b_i = v_i$ is an optimal bid.

2.  If $v_i > b^{(-i)}$ then $i$ prefers to win and pay $b^{(-i)}$ than
    not winning. Thus, any $v_i > b^{(-i)}$ is optimal and in
    particular, $b_i = v_i$ is an optimal bid.

 
```

```{prf:theorem}
The second price auction is individual rational in equilibrium: if
$b_i = v_i$ for all $i$, then $v_i - p_i \geq 0$ for all $i$.
```

```{prf:proof}
 If $i$ doesn't win, then their payoff is $0$. If they do win,
then the price they pay is upper bounded by their valuation, so
$v_i - p_i \geq v_i - v_i = 0$. 
```

```{prf:theorem}
In equilibrium, the second price auction allocates the good to the
bidder with the highest value.
```

```{prf:proof}
 In equilibrium, $v_i = b_i$ for all $i$ so
$\arg\max_i b_i = \arg\max_i v_i$. 
```

## Revenue Maximization

```{prf:example}
Suppose $A$ values the good at $1$ and $B$ values the good at $2$. In a
second price auction, both bid truthfully and $B$ wins at a price of
$1$. In a first price auction, the unique equilibrium is $A$ bids $1$
and $B$ bids $1 + \epsilon$ and revenue is $1+\epsilon$ which is
basically equivalent to $1$.
```

To analyze the case with uncertainty and Bayesian agents, we need to
define a new notion of equilibrium.

```{prf:definition}
A Bayesian Nash Equilibrium is a strategy profile such that each player
is maximizing their own payoff with respect to the posterior belief
generated by others' strategies.
```

```{prf:example}
Suppose $A$ and $B$ both have values drawn uniformly from $[0,1]$. In a
second price auction, expected payoff is
$\mathbb{E}\left[\min\{v_A,v_B\}|v_A,v_B \sim Uni[0,1]\right] = 1/3.$ In
a first price auction, the equilibrium is $b_A = v_A/2, b_B = v_B/2$ and
in expectation, revenue is

$$\mathbb{E}[{\max\{b_A,b_B\}}] = \mathbb{E}[{\max\{v_A,v_B\}/2}] = 1/3.$$
```

It turns out that these auctions generate the same revenue:

```{prf:theorem}
At equilibrium, expected payments are fully determined by the auction's
allocation rule.
```

```{prf:corollary}
Taking the auction's allocation rule to be the one that gives the item
to the bidder with the highest bid, first, second, and all-pay auctions
generate the same revenue in Bayes-Nash Equilibria.
```

It is not always the case that auctions always give the good to the
max-value bidder:

1.  There can be overbidding in second price auctions ($A$ bids $v_B+1$,
    $B$ bids $0$ is an equilibrium but doesn't give the good to the
    max-value bidder if $v_A < v_B$);

2.  In an all-pay auction, there can be equilibria where the highest
    value bidder does not get the item;

3.  In auctions with reserve prices, it could be the case that no bidder
    gets the item.

[^1]: In the case of $n$ buyers and each drawing a value from $D$
    independently, the revenue-maximizing auction is a second price
    auction with reserve price $p(D)$.