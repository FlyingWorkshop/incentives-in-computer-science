# Proof-of-Work Blockchains

```{prf:definition}
A digital signature consists of the following:

1.  a public key and a secret key;

2.  a signature function sign;

3.  a verification function verify.

To show agreement with statement $x$, set
$y \leftarrow \mathrm{sign}(x,\mathrm{secret\_key})$. Anyone with the public key can then
$\mathrm{verify}(x,y, \mathrm{public\_key})$ to make sure the person with the secret key
agreed with $x$.
```

```{prf:definition}
A hash function $H$ such that given some input $a$, it is easy to
compute $H(a)$ but given some output $b$, it is difficult to compute
$H^{-1}(b)$.
```

In general, the fastest way to "invert" a cryptographic hash function is
to randomly try inputs. To get $a$ such that $H(a)$ agrees with $b$ for
the first $k$ bits requires $2^k$ tries.

Consider Alice transferring \$1 to Bob. If done through a bank or other
centralized institution, the intermediary can verify that Alice does
indeed have \$1 to give to Bob. However, can this transfer be done
without a bank?

Bob may require Alice to verify that the \$1 exists and is transferred.
One way Alice may do this is to provide a history of where the \$ has
been for Bob to track Alice's history of payments and make sure Alice
has not already spent the dollar.

```{prf:definition}
A ledger is an ordered history of payments. A decentralized ledger is
not controlled by any one entity and can continue to work even if a bank
is hacked (Robinhood, etc.). Consensus occurs when all entities agree
that a transaction happened.
```

Ledgers are used to verify ownership of capital. In the early 1980's,
Byzantine protocols (BFT's) can reach consensus if a certain fraction
(around $1/2$ to $2/3$) of actors are honest. However, who can join?

```{prf:definition}
A network is permissionless if anyone can join or exit at any time.
```

While this is a nice property to have, verification relying on a
majority of users is useless as anyone can simply create more copies of
themselves to obtain an artificial majority. Alternatively, votes can be
tied to more concrete things:

-   Proof of Work: 1 cpu equals one vote;

-   Proof of Stake: 1 coin equals one vote;

-   Proof of Space: 1 bit equals one vote.

## (Simplified) Bitcoin Protocol

Ledger is constructed as a chain of blocks. Each block contains:

1.  Some account of payments or transfers;

2.  A cryptographic hash of the previous block;

3.  A *nonce*.

What is a nonce? A nonce for a block is valid if the hash for a new
block (which includes information about payments, hash of previous
block, and nonce) has $k$ leading zeros. In general,

$$\mathbb{P}({\text{nonce is valid}}) = \frac{\text{number of hashes tried}}{2^k}.$$

A nonce is one way to establish Proof of Work: it proves that a lot of
hashes were tried (and some luck was involved). Miners compete to find
the first valid nonce and create ("mine") new blocks. Winners are
rewarded in the form of a transaction in the new block. The $k$ leading
zeros that need to match is adjusted dynamically so each block takes
around $10$ minutes to mine in expectation.

To verify a single payment from Alice to Bob in block $b_t$:

1.  Verify that Alice has signed the payment using Alice's public key;

2.  Verify that Alice has received this \$1 in some previous block;

3.  Verify that Alice has not spent the \$1 in some previous block.

To verify an entire block:

1.  Verify all payments individually;

2.  Verify that $b_t$ correctly hashes $b_{t-1}$;

3.  Verify the nonce.

For Alice to send money to Bob, a signed transaction is sent to all
miners. Then, Alice and Bob wait for the next block to be mined.

What happens if two miners find different nonces for a new block at the
same time? Two new blocks could be made and there is no longer
consensus. In this case, the standard protocol is to extend the longest
chain available: if block $b_t$ and $\hat{b}_t$ both extend $b_{t-1}$
but $b_t$ has a chain to $b_{t+n}$ while $\hat{b}_t$ has a chain that
goes to $\hat{b}_{t+m}$ for $m < n$\< then extend $b_t$ over
$\hat{b}_t$.

## Incentive Issues with Big Miners

Original idea (2000's): computing power would be distributed about
equally over all people so each individual miner has a small fraction of
total power. However, emergent trends in the 2010's disincentivized
this:

1.  Rise of corporations taking over major computing power (the cloud);

2.  Crypto-specific hardware that is much more efficient (and
    expensive);

3.  Cheaper energy that miners might have access to;

4.  Creation of mining pools where professional miners organize to
    reduce variance in gains from mining.

Recall the longest chain rule: if one miner has access to more than half
of computing resources, they can take advantage of this to "overwrite"
blocks they don't like by forcing a fork in the chain. For instance,
Alice can pay Bob and encode that in a block that is overwritten as a
result of a fork, causing the payment to not actually go through.

Even with $\alpha < 1/2$ of computing power, Alice can try to carry out
the same attack and rely on luck: if Alice can mine two blocks before
any other miner extends the blockchain to the block where Bob gets paid,
Alice successfully avoids needing to pay Bob. Probability this succeeds
is $\alpha^2$. As such, best practice is to wait $d > 1$ blocks before
accepting payment.

## Selfish Mining

Suppose there is a selfish miner who seeks to break the system.
Furthermore, suppose their connection is so fast that all longest-chain
ties are broken in their favor. What can they do? Consider the following
strategy:

-   Mine blocks.

-   If block is mined, do not reveal the new block, but mine follow-ups
    to that block.

-   If another miner mines the next block, reveal the block you have
    already mined.

Nothing is lost by waiting before revealing blocks: since ties are
broken in favor of the selfish miner, their block is still the block
that goes through. However, there is some benefit to them: the rest of
the network wastes time on mining a block that eventually becomes
orphaned. If the selfish miner has a fraction $\alpha$ of computing
power, their *effective* relative hashrate is
$\frac{\alpha}{1-\alpha} > \alpha$ as for every block they mine, other
honest miners waste a block.

What if ties were always broken against the selfish miner? In this case,
the selfish miner risks losing their additional (hidden) progress in
case of a tie. However, what if the selfish miner can mine two blocks in
a row to ensure no ties occur? Selfish mining can be profitable in this
case if $\alpha > 1/3$ opposed to the previous $\alpha > 1/2$.

This effect becomes more pronounced if the honest miners then respond to
the selfish miner's actions: if honest miners know the selfish miner is
always going to "win", they might leave the blockchain (to save energy
or mine other blockchains), leaving the selfish miner with an even
larger portion of hashrate.

## Big Miners in Practice

In 2014: GHash.io controlled more than 51% of computing power but did
not execute attacks. Instead, they encouraged miners to leave to prevent
the value of bitcoin from dropping. For smaller coins with lower total
hash rate, the issue is larger since less computational power is needed
to achieve majority control. Furthermore, attackers may care less about
the value od smaller coins. The 51% attack happened multiple times to
"Ethereum Classic".