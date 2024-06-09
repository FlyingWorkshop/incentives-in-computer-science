# Security Markets

## High Frequency Trading Arms Race

In 2010, Spread Networks invested \$300 million to create a new
straight-line optic fiber cable from Chicago to New York, reducing
latency from 16ms to 13ms. High frequency traders race to make trades
first, which is why they value the decrease in latency. However in 2011,
microwaves brought latency down to 10ms.

Is this a market failure? From Spread Network's perspective, the cable
might have made back its investment (and then some profit), but even
then the opportunity cost of the investment might have been high as
well. Furthermore, does high frequency trading in and of itself even
benefit society?

## Stock Markets

We build on the definitions introduced in Section 11 (Prediction Markets
and Information Cascades).

```{index} Naive Investors
```
```{prf:definition} Naive Investors
:label: naive-investors
Individuals who want to buy/sell stock as a means to store or liquidize
assets. Naive investors do not have a primary goal of profiting from
private information.
```

With just naive investors, there can be market frictions: there may not
be stocks to buy or sell when a naive investor wants to buy or sell.
Furthermore, the no-trade theorem does not apply as these investors
derive value from the act of buying or selling itself instead of purely
caring about the monetary value of their assets.

As before, liquidity providers leave resting orders and buy low, sell
high. They provide an intermediary for naive investors to trade with,
but naive investors lose the spread that liquidity providers gain. As
such spread is part of naive investors' transaction costs.

A stock's "true" value represents aggregate beliefs about the stock's
returns. In equilibrium, a stock's true value is between the stock's bid
and ask prices (otherwise, some agents have a profitable deviation to
buy or sell the stock). True value may vary depending on external
events. For example:

1.  Correlated Stocks/Securities: If someone buys gold in Chicago, the
    price of gold in New York increases. If there is demand for security
    $X$ increases and security $X$ is correlated with security $Y$, then
    the price of $Y$ will go up.

2.  Fed announcements: Fed made announcement on Sept 18, 2013. Markets
    reacted faster than the speed of light.

3.  Twitter: Trump tweets (about tariffs, the Fed, covfefe) changed
    stock values.

4.  Reddit: wallstreetbets and Gamestop stock.

```{index} Snipers
```
```{prf:definition} Snipers
:label: snipers
Agents that wait for changes in stock values and rush to trade with
liquidity providers' standing orders before those standing orders can be
canceled. As such, being faster than competitors can be profitable.
```

In response to snipers, liquidity providers might increase spread to
decrease sniping opportunities. However, this hurts naive agents by
increasing their effective transaction costs.

## Market Failure Fixes

How can we resolve these market failures?

1.  **Symmetric Speed Bumps:** all orders get delayed by the same
    amount.

    -   Doesn't solve the speed arms race, nor does it remove sniping
        risk for liquidity providers.

2.  **Random Speed Bumps:** each order is delayed by some random amount.

    -   Mostly solves the speed arms race (as luck in random difference
        is more important than speed differences), but makes the sniping
        risk worse: if a single sniper gets lucky, then the sniping
        succeeds.

3.  **Sniper-Only Speed Bumps:** only delay snipers.

    -   If implemented, this would resolve the speed arms race and
        sniping risk, but it is difficult to determine who is a sniper
        and who is not.

4.  **Frequent Batch Auctions:** batch orders for some short interval
    and find the market-clearing price at each batch.

    -   Everyone now has time to react to value-changing events as
        orders are prioritized by price instead of arrival (as long as
        the order arrives in the same batch).

## Blockchain Flashboys

```{index} Smart Contracts
```
```{prf:definition} Smart Contracts
:label: smart-contracts
Agreement between two agents for one transaction (borrowing) in the
current period and a second transaction in some future period (paying
back, perhaps with interest). If the second transaction does not happen,
some collateral promised by the first agent is given to the second
agent.
```

The collateral needs to be sent simultaneously with the first
transaction (otherwise one agent can abort after getting money).

```{index} Atomic Transaction
```
```{prf:definition} Atomic Transaction
:label: atomic-transaction
A transaction such that either all steps are executed successfully or
all steps are canceled.
```

One application of smart contracts is in decentralized finance (DeFi):
cryptocurrencies, stocks, and contracts are traded. Limit order books
and automatic market makers can be automated via smart contracts.

```{index} Arbitrage
```
```{prf:definition} Arbitrage
:label: arbitrage
Simultaneously buying low in one market while selling high in another.
```

Arbitrage is especially attractive with decentralized finance:

1.  Risk-Free Atomic Arbitrage:

    -   In centralized finance, the arbitrageur takes takes risk (if
        they buy low first, then the high price they wanted to sell at
        may drop before they get to selling).

    -   However, bundling buy and sell actions into a single atomic
        transaction resolves this risk.

2.  Cryptocurrencies are highly volatile, leading to more sniping
    opportunities;

3.  Information (code) is made public so full code and state of smart
    contract automated market makers are available. As such, it is easy
    to exploit bugs.

```{index} Front-Running
```
```{prf:definition} Front-Running
:label: front-running
Transacting right before another agent to take advantage of the
distortionary effects of the latter's transaction.
```

In general, this is illegal in centralized finance. In decentralized
finance however, all transactions are made publicly known before blocks
are mined. Now, suppose miners are also traders and an arbitrageur finds
an opportunity. If the arbitrageur broadcasts this transaction, then
miners can execute the same trade on their own account. Miner includes
the arbitrageur's transaction on their block but after the miner's own
transaction.

## Miners' Extractable Value (MEV)

In DeFi, arbitrageurs compete to be at the top of the next block via
transaction fees. Then, a miner's MEV is how much they can charge an
arbitrageur. Miners receive rewards for each block they mine and
additional transaction fees. Originally, the value for mining the block
itself is greater than the MEV, but in recent years block rewards have
went down (bitcoin rewards halve every 4ish years) while MEVs have gone
up (arbitrageurs increasing demand for transactions). When MEVs come
into play, not all blocks are created equal.

As such, miners can access a new type of fee-sniping attack: if block
$\hat{b}$ has a larger MEV than block $b$, then miners would prefer to
mine $\hat{b}$ over $b$. Then, a miner with fraction $\alpha$ of
computing power profits from a fee-sniping attack if

$$\alpha^2 \cdot \text{higher MEV} > \alpha \cdot \text{lower MEV} \iff \alpha > \frac{\text{lower MEV}}{\text{higher MEV}}.$$

Success probability is even higher if other miners also try to attack
instead of extending $b_t$.

With selfish tie-breaking, miners want to extend the block with higher
MEV opposed to the block that was seen first. Furthermore, a miner can
incentivize other miners to help extend their block by leaving some MEV
leftover in the next block (known as undercutting). Some possible ways
to undercut these issues:

1.  Transaction fees distributed among miners that mine the next $k$
    blocks;

2.  Capped transaction fees;

3.  "Burn" transaction fees instead of giving them to miners.

However, arbitrageurs and miners can always make side payments.