# Market Failures

The assumption we previously made was that free markets naturally
converge to an optimal outcome. However, this clearly is not always the
case: market failures arise when markets fail to converge to an optimal
outcome.

## Externalities and Public Goods

```{prf:definition}
:label: externality
**Externalities** are side effects on individuals other than the buyer
or seller.
```

```{prf:definition}
:label: public-goods
**Public goods** are goods that are accessible and usable by
everyone but not owned by anyone.
```

For example:

-   The environment is a public good, and activities that harm the
    environment (plane tickets) have negative externalities.

-   WiFi bandwidth is a public good, and one person's usage imposes a
    negative externality of slower connections on others.

Two possible solutions.

1.  Pigouvian tax: a tax on transactions proportional to the externality
    they generate. (e.g., carbon, bags, cigarettes)

2.  Coasian bargaining: auction off public goods and rely on the Coarse
    Theorem to achieve social efficiency.[^1]

[^1]: '91 Nobel prize.

## Transaction Costs

Also known as market frictions. Sometimes, transactions themselves can
be costly to execute leading to mutually beneficial transactions not
being made. For example:

-   Agent one has a boat worth $9,900$ to them and agent two is willing
    to pay $10,000$.

-   Agent one can sell the boat to agent two and both would be happier
    off.

-   However, if there is a $9\%$ sales tax on boats, this transaction
    would not occur.

Transaction costs do not necessarily have to be monetary:

-   A hungry student is willing to buy an apple for $10$ while other
    students have applies worth $1$ to them.

-   Other students can sell the apple to the hungry student and both
    would be better off.

-   However, there are *time/information costs* for the hungry student to
    run around and ask other students if they have an apple on them.

Computers, especially the Internet and search have done a lot to reduce transaction cost (e.g., Lyft, Venmo, Tinder). 

## Market Thickness

```{prf:definition}
:label: thick
Informally, a thick market has many buyers, a thin market has few buyers. 
```

A market is thick (thin) if there are many (few) buyers and sellers.
In thick markets, sellers and buyers have lots of options which makes
prices close to competitive equilibrium. In thin markets, there are few
buyers and if buyers come they face monopoly prices. Thick markets
generate welfare-maximizing outcomes while thin markets do not.

Why are monopolies bad? Monopoly quantity sold is lower than quantity
sold in competitive equilibrium; prices are higher and consumer surplus
is lower.

First welfare theorem holds with reserve prices to cover costs. However,
sellers setting reserve prices is not {prf:ref}`strategyproof <strategyproof_label>`.

```{prf:proof}
 If reserve prices are nonbinding, then sellers can increase
reserve prices by $\epsilon > 0$ and still sell. If prices are binding,
then the good is sold at the reserve price which is equal to cost and
the seller makes zero profit. Assuming the necessary assumptions,
sellers can increase reserve prices by $\epsilon$ and make strictly
positive profit, which is a profitable deviation. 
```

Some ways to get around this:

-   As markets become far from monopoly, it converges to a
    seller-strategyproof mechanism (*strategyproof-in-the-large*).
    However, this requires fungible goods in a thick market.

-   If the seller doesn't know buyers' valuations, then it is difficult
    for sellers to set a reserve price. However, sellers collect lots of
    data.

How can markets be thickened?

-   Encourage buyers and sellers to join and stay;

-   Merge markets (larger kidney donation markets have typically led to
    better outcomes);

-   Batch transactions: wait a bit for more buyers and sellers to join
    before running transactions (e.g., ride-share, kidney exchange).

## Timing Issues

### Market Unraveling 

*Committing to contracts too early*

In certain markets, one side has incentives to
make matches earlier and earlier (to get good students before
competitions hire them). As a result, before introduction of the
centralized matching mechanism for matching doctors and residencies even
first year med students would be matched. However, whether or not a
first year med student and a residency would be a good match is a bad
predictor of whether or not the student and the residency is still a
good match four years later.

### Exploding Offers
Job offers that require a very short response
time. In markets where one side needs to look for other candidates if
turned down, short response times can arise. Amplified when:

-   if there is a limited time window for transactions due to regulatory
    issues;

-   if one side of the market can't absorb variance in the number of
    matches received.

### Impatience

The third timing issue is not waiting for a market to clear. APPIC rules for psychologists in
the 1970-1990's:

-   All transactions must occur on selection day;

-   Exploding offers are not allowed.

In theory, the result should be similar to Deferred Acceptance. In
practice, employers didn't want to propose to candidates who might
cancel right before the deadline leading to earlier and earlier "safe"
commits.

### Solutions 

How to resolve timing issues? Centralized matching systems will help.
However, setting timing rules often fail due to incentives to violate
rules being too strong ("Would you like to visit my hospital \[wink
wink\]"?) Rules/norms that allow for accepting and then reneging from
exploding offers removes the incentives to cheat and make exploding
offers.

```{seealso}
Notes on market stability from [ECON 136: Market Design](https://flyingworkshop.github.io/market-design/book/stability-order-unraveling.html?highlight=exploding+offers).
```

## Information Asymmetries

```{prf:definition} Information Asymmetry
:label: info_asym_label
Informally, the seller knows something that the buyer doesn't.
```

Sellers know more about the quality of goods than buyers. As such,
buyers might buy a good that they thought was worth it, but later find
out that the good is worse than expected. For example, the market for
lemons:

-   Market for used cars, some good and some bad.

-   Buyers willing to pay more for good cars than bad cars but do not
    know which type of car is which.

-   Sellers willing to sell bad cars for less and do know which car is
    which.

-   Let $g \in [0,1]$ be the fraction of cars in the market that are
    good.

-   Let $h \leq g$ be the fraction of cars that are in good condition
    and also for sale.

One bad equilibrium: only bad cars are sold at a low price and high cars
aren't worth being sold at that low price.

One good equilibrium: if the portion of good cars is high enough, then
the expected value of a car and hence price of a car is high enough to
sustain good cars being sold.

Other examples where asymmetric information comes up:

-   Health insurance: buyers know private information about their health
    status, sellers want to sell insurance to healthier individuals.

-   Clickbait: content creators know if a link is clickbait or not while
    users do not. Creators what to maximize clicks, users want to avoid
    clickbait.

```{prf:definition} Moral Hazard
A moral hazards occur when there is an incentive for an agent to risks, because
they do not bear the full costs of their actions. For example, insurance might encourage
risky behavior.
``` 

```{prf:example}
:nonumber: true
As a fun (potentially apocryphal) example, Stanford used to give out free bike helmets to freshmen; however,
they reportedly stopped doing so because the rate of bike crashes increased, presumably because the helmets
emboldened new bikers to take more risks.
```

```{prf:definition} Adverse Selection
**Adverse selection**: situations where only the low quality
goods/lemons stay in the market.
```

Possible solutions:

-   Provide more information to both sides (mandatory disclosures,
    reputation systems);

-   Disallow use of information (universal health care, anti-insider
    trading regulations);

-   Filter out lemons (require warranties).