# Sponsored Search Auctions

Used to auction ad slots on websites. Model:

1.  There are $N$ slots with slot $j \in N$ having associated
    click-through rate $\alpha_j$ which is assumed to only depend on $j$
    (so for instance, quality of the ad itself does not matter);

2.  There are $M$ advertisers with advertiser $i \in M$ having a value
    of $v_i$ per click;

3.  An allocation is a function $A: N \to M$ that matches the $i$th slot
    to the $A(i)$th advertiser;

4.  Define social welfare to be 

    $$W(A) = \sum_j v_{A(j)} \alpha_j.$$

What is the optimal allocation $A$ to maximize $W$?

```{prf:axiom}
General Second Price Auction

1.  Ask each advertiser for a bid $b_i$;

2.  Assign highest bid to first slot, second highest bid to second slot,
    etc;

3.  For each slot $j$, advertiser $A(j)$ pays $b_{A(j+1)}$.
```

```{prf:remark}
With the special case of one slot $j=1$, GSP is equivalent to the second
price auction.
```

The allocation rule in step two maximizes 
$$\sum_j b_{A(j)}\alpha_j.$$
However, GSP is not strategyproof: some advertisers may prefer to win a
lower slot at an even lower price than a higher slot at a high price.

## Vickrey-Clarke-Groves Mechanism

```{prf:definition}
The externality of agent $i$ is the difference in utility for all other
agents when $i$ is present versus when $i$ is not.
```

```{prf:example}
Suppose $v_1 > v_2 > v_3$ and there are two slots. In a welfare-optimal
outcome, $1$ gets $v_1 \alpha_1$ for the top slot, $2$ gets
$v_2 \alpha_2$ for the top slot, and $3$ gets nothing. If $1$ were not
present, $2$ gets $v_2 \alpha_1$ and $3$ gets $v_3 \alpha_2$. Thus,
$1$'s externality is 

$$(v_2 \alpha_2) - (v_2 \alpha_1 + v_2 \alpha_1).$$
```

```{prf:axiom}
VCG Mechanism

1.  Ask each bidder for their valuation;

2.  Find the welfare-maximizing allocation with respect to solicited
    bids in step $1$;

3.  Allocate slots via the welfare-maximizing allocation;

4.  For each bidder $i$:

    1.  Find the allocation that maximizes welfare for all agents other
        than $i$;

    2.  Set $i$'s payment equal to the difference between how satisfied
        everyone else is when $i$ is present versus when $i$ is not.
```

```{prf:theorem}
The VCG auction is dominant strategy incentive compatible.
```

```{prf:proof}
 Bidder $i$'s payoff is 
 
$$
\begin{split}
    v_i(X) - p_i(X) &= v_i(X) + \sum_{k \neq i} b_k(X) -  \sum_{k \neq i} b_k(X^{-i}).
\end{split}
$$ 

However, $\sum_{k \neq i} b_k(X^{-i})$ does not depend on
the bid $i$ submits so $i$'s maximization problem is equivalent to
maximizing $v_i(X) + \sum_{k \neq i} b_k(X)$. Since the VCG mechanism
already chooses the socially optimal outcome, it is a dominant strategy
for all individuals to truthfully report. 
```

In the context of sponsored search auctions, the assignment rule is
still the same (highest bidder gets first slot, second highest bidder
gets second slot, etc.) but payments are different. For slot $\alpha_j$,
advertiser $A(j)$ pays 

$$\sum_{k > j} b_{A(k)}(\alpha_{k-1}-\alpha_k).$$

Another nice property of VCG auctions is that it is envy-free:

```{prf:definition}
An assignment $(A,p)$ consisting of an allocation rule and prices is
envy-free if for all advertisers $i,j$, advertiser $i$ does not envy
advertiser $j$: $i$'s utility is (weakly) greater than $i$'s utility if
they got $j$'s slot and paid $j$'s price.
```

In the context of sponsored search auctions, this means that

$$\alpha_{A^{-1}(i)}(v_i-p_i) \geq \alpha_{A^{-1}(j)}(v_i-p_j)$$

 for all $i,j \in M$.

## Unnatural Equilibria

```{prf:example}
Suppose there is a single item and there are two bidders with
$v_A = 10, v_B = 9$. One equilibrium is $b_A = 7, b_B = 100$. Then, $B$
wins the auction and pays $\$7$. This is an equilibrium (exercise for
the reader to check this).
```

While no bidder has a profitable deviation, this outcome is not envy
free: $A$ would rather get $B$'s outcome than their current outcome.
Adding the envy free requirement gets the following:

```{prf:theorem}
There is a correspondence between the following:

-   Envy-free equilibria of the GSP action;

-   Competitive market equilibria;

-   Stable matchings between buyers and (price,good) pairs.
```

As such, we can get two immediate corollaries:

-   We can efficiently find equilibria using deferred acceptance with
    prices.

-   The buyer-optimal (seller-worst) equilibrium corresponds to VCG
    payments.

## GSP vs VCG in Practice

History:

-   In late 1990's: Overture runs first price auctions;

-   Early 2000's: Google, Yahoo, Bing start running GSP auctions;

-   Late 2000's: Facebook runs auctions using VCG;

-   Late 2010's: Google switches back to first price auctions.

Why the switch back to first price auctions? Many advertisers
participate in different auctions using the same bids, and given fixed
bids a first price auction makes more money than GSP, which makes more
money than VCG.

Another trend: auctions are sensitive to bidder collusion.

-   2005: Bidding software must be authorized by search engine (easy to
    prevent collusion);

-   Early 2010's: most ad bidding is through a small number of agencies
    (bad for competition and revenue);

-   Late 2010's: ML based auto-bidders on Google, Bing, etc.

What about now? General move away from explicit auction rules:

-   Auction details are highly optimized and hard to understand (a lot
    of things are ML);

-   Big tech companies often know vales better than bidders (so they
    provide in-house bidders);

-   Advertisers exploit the fact that different companies have to
    compete (less incentive to explain rules).