# Prediction Markets and Information Cascades

```{figure} ../images/ox.jpg
:name: school-choice
:height: 400px

Muskox *(Ovibos moschatus)* male, Dovrefjell National Park, Norway. Photo from Charles J. Sharp on [Wikipedia](https://en.wikipedia.org/wiki/Muskox).
```

```{prf:example}
How much does an Arctic Musk Ox weigh? At a country fair, the average of
all guesses turned out to be correct. This example motivates using "the
wisdom of the crowd". Why might asking a crowd be good?

1.  Different people might have different perspectives or biases that
    balance out in a large crowd;

    -   Elections

2.  Information may be fundamentally distributed

    -   State of a group project
```

Even in these instances, it is important to consider incentives: people
might have an incentive to lie on polls due to social desirability, etc.

```{prf:example}
Prediction market hosted by the University of Iowa. For \$1, a better
can buy a bundle of a $D$-contract and an $R$-contract where a
$D$-contract pays \$1 if a democrat wins and an $R$-contract pays \$1 if
a republican wins (so trades are zero-sum). Then, betters can trade via
a continuous limit order book.
```

```{index} Spread
```
```{prf:definition} Spread
:label: spread
Let $\mathrm{Bid}$ denote the highest buy order and $\mathrm{Ask}$ denote the lowest sell
order. Then, buy and sell orders arrive at any time and trade whenever a
new buy order is greater than $\mathrm{Ask}$ or if a new sell order is less than
$\mathrm{Bid}$. The house (market) keeps any surplus from trade. Define the
$\mathrm{Spread}$ at any point in time to be $\mathrm{Ask}-\mathrm{Bid}$. Any order that induces a
trade upon arrival is called a Marketable order, while any order that
does not induce a trade upon arrival is called a Resting order.
```

We can interpret the price of a $D$ or $R$ contract as the probability
of a $D$ or $R$ win to aggregate the market's beliefs. At equilibrium
prices, the number of $D$ contracts is equal to the number of $R$
contracts and the total budget of predictors who think $D$ is more
likely to win over $p_D$ is equal to the total budget of predictors who
think $R$ is more likely to win over $p_R$

## Liquidity in Prediction Markets

One challenge in some prediction markets is large bid-ask spreads. This
leads to poor information aggregation. Why might spreads be large?

```{index} Liquidity Providers
```
```{prf:definition} Liquidity Providers
:label: liquidity-providers
People who buy low now and sell high later without caring about the
final realization. Liquidity providers leave bid/ask resting orders on
the order book that other investors can buy/sell with at any time. When
liquidity providers buy and sell, they earn their spread.
```

In general, competition between liquidity providers drives spread down.
Providing liquidity seems like a good deal, but prices can change.

```{prf:theorem}
If the market has already aggregated all available public information,
there is no point in trading.
```

It turns out this result still holds with private information:

```{prf:theorem}
If the market has already aggregated all available public information,
there are no further trades even if some individuals have private
information.
```

```{prf:proof}
 Suppose someone has private information that leads to them
wanting a trade. Then, no one would want to be the other person in the
trade since trades are zero-sum so if the person with private
information expects to make a profit, anyone that trades with them must
be making an expected loss. 
```

## Information Cascades

Information aggregation is a dynamic process. To model this:

1.  There are $n$ ordered agents $1,2,...,n$;

2.  Going in sequence, agent $i$:

    1.  Observes a private signal;

    2.  Observes others' actions but not others' signals;

    3.  Chooses some action.

```{prf:example}
Suppose an urn has red and blue balls, Either $2/3$ balls are red and
$1/3$ are blue, or $2/3$ are blue and $1/3$ are red. Participants draw a
ball and observe its color (with replacement to avoid probability
issues), then sequentially guess if there are more blue or red balls. If
the first two players draw a blue ball and guess that there are more
blue balls, then even if someone in the future draws a red ball, they
still will guess blue. This leads to an information cascade where
players past the third ignore their information and blindly trust
players one and two.

Suppose in truth, there are $2/3$ red balls and $1/3$ blue balls. Three
cases of what happens in the first two rounds:

1.  Correct cascade:
    $\mathbb{P}({\mathrm{Red}, \mathrm{Red}}) = \frac{2}{3} \cdot \frac{2}{3} = \frac{4}{9}$;

2.  Wrong cascade:
    $\mathbb{P}({\mathrm{Blue}, \mathrm{Blue}}) = \frac{1}{3} \cdot \frac{1}{3} = \frac{1}{9}$;

3.  No cascade:
    $\mathbb{P}({\mathrm{Red}, \mathrm{Blue} \text{ or } \mathrm{Blue}, \mathrm{Red}}) = \frac{2}{3} \cdot \frac{1}{3} +\frac{1}{3} \cdot \frac{2}{3} = \frac{4}{9}$.

Then, the probability of a correct cascade is four times likelier than a
wrong cascade, so even with infinitely many samples there's a $20\%$
chance of the crowd guessing completely wrong.
```

```{prf:example}
1.  Two pricing algorithms for the same book led to a spiral of
    misinforming one another, leading to textbooks priced at $20$
    million.

2.  On 5/6/2010, stock markets lost around one trillion of value but
    mostly recovered in 36 minutes. Official theory: one trader
    allegedly caused the crash by trading from their parents' garage.
```

## Legal Issues of Prediction Markets

In general, trading in prediction markets is essentially gambling which
is mostly illegal in the United States (outside of Las Vegas). The IEM
was granted a special exception by the Commodity Futures Trading
Commission subject to some constraints (limited to 1000 trades, \$500
per trader). Other prediction markets have been forced to shut down.

However, "naked shots" can be legally bought for billions on Wall
Street.