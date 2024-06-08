# Proof of Stake

Continuing the analysis of big miners, proof-of-work or longest chain
protocols leads to fragile incentive structures. Luckily, the benefit is
that pools or miners with high portion of computing power want the value
of a coin to go up. However, this argument falls apart if mining
hardware can be repurposed or if the blockchain is small.

In proof of work (PoW), hash power is used as a proxy of how much a
miner cares about a blockchain. But why use a proxy?

At each iteration of a vanilla proof of stake (PoS) protocol,

1.  A random coin is sampled;

2.  owner of that coin is asked to create the next block.

Intuitively, people with a lot of coins care about continued success of
the blockchain, while people with few coins are unlikely to be asked to
create the next block. PoS has more robust incentives and reduces
competition through computing power (which is good for the environment).

Mining PoS is computationally cheap, but still requires servers with a
robust connection. In practice, over half of servers are hosted by
Amazon (which means it's not quite decentralized, but if Amazon goes
down the world is half over anyways).

## Cryptographic Preliminaries

```{prf:definition}
Deterministic function that you can share code for, but looks like a
random function for computationally bounded algorithms.
```

```{prf:remark}
For the purposes of this class, we will treat pseudo-random functions as
"cryptographic black magic".
```

```{prf:definition}
A function $f$ that is similar to a Hash function (given $a$, it is easy
to verify that $f^{-1}(a) = b$) such that parallelization does not help
speed up how long it takes to find $a$.
```

```{prf:definition}
Prevents people from changing responses ex-post. Inputs: a secret $x$
and a random string $r$.

Protocol:

1.  In this period, one agent sends $c = \mathrm{commit}(x,r)$;

2.  In the next period, they send $x,r$.

Guarantees:

1.  Any other agent can verify that $c = \mathrm{commit}(x,r)$;

2.  But it is computationally intractable to ind $x',r'$ such that
    $c = \mathrm{commit}(x',r')$.
```

How to introduce randomness in a decentralized, permissionless,
strategyproof consensus protocol? Some possible approaches are:

1.  Ask the $t$th miner to choose the $(t+1)$th miner at random;

    -   Not strategy proof: the $t$th miner could choose themselves.

2.  Pseudo-Random function of entire $t$th block;

    -   Still not strategy-proof.

3.  External event like stock prices or the weather;

    -   Not decentralized (have to agree on what external event) and not
        strategyproof (stock prices are manipulable).

4.  Some decentralized coin-flipping protocol;

    -   Not permissionless.

Some other issues with PoS protocols:

1.  Nothing-at-Stake: in PoW, there theoretically should only be an
    incentive to extend the longest change. However, in PoS miners can
    try (for free) to extend every block;

    -   Doesn't work for PoW since tie-breaking is based on
        computational power, not randomness.

2.  Predictability Attacks: one possible way to generate
    pseudo-randomness is to use a pseudo-random function of the first
    block and the current block. However, miners might be able to
    predict when it's their turn to create blocks allowing for
    double-spending attacks.

    -   Very difficult to predict who mines the next block in PoW
        protocols.

3.  Long range attack: attacker buys almost all coins at time $t$ and
    then sell all coins at time $t+1$. By some time $t+k$, buyers are
    satisfied and pay attackers off chain so attackers are no longer
    staked. Attacker can fork a chain from $b_t$ in which they still own
    all the coins and can mine much faster.

    -   Information about who gets to mine the next block is a function
        of the block in PoS, but who gets to mine the next block is
        independent of block in PoW. Thus, rewriting the history doesn't
        change how much computing resources you have.

## Approaches to Implementing Proof-of-Stake

1.  Slashing: fining coins from miners that misbehave.

    -   Mitigates the noting-at-stake problem by slashing miners that
        produce blocks pointing to conflicting blocks;

    -   However, this needs other miners to vote on who is misbehaving;

    -   Network issues might look like misbehavior (potentially is fine
        since network issues also cause loss of blocks in PoW);

    -   Miners need to place slashable coins in escrow so they can't
        spend it before it gets slashed (capital inefficiency).

2.  RANDAO: multi-agent randomness. Agents select a secret random bit
    and send each other commitments. Then, actual bits are sent and
    verified, and output is a function of all agents' bits. Then, only
    one truly random agent is sufficient for the output to be random.

3.  Verifiable Delay Functions: randomness is a VDF of a random event,
    like stock prices. Then, even if a miner wants to manipulate stock
    prices, the VDF means that they do not know how to manipulate
    prices.

4.  Byzantine coin-flipping Protocols: select random coin instead of a
    random attack time. Byzantine fault-tolerant (BFT) protocols can
    reach consensus on random bits. Technically not permissionless, but
    even more technically PoS protocols are also not permissionless
    (coins are permission). These protocols may also be challenging to
    scale.

    -   Can randomly select a committee of active Byzantine generals;
        then each committee selects the next committee using a Byzantine
        protocol.

    -   Requires participants to be online (can slash participants that
        are offline for too long).

5.  Finality/Checkpoints: in pure permissionless longest chain, agents
    are never 100% sure that the chain they are currently seeing is
    really the longest chain out there. For some transactions, waiting
    to transact with bitcoins is prudent, but maybe not feasible for
    other transactions. If 2/3 of holders agree (using BFT) on a block,
    consider it final. Treat final blocks as new genesis blocks.
    Mitigates long-range attacks if attackers selling their stake takes
    longer than the gap between checkpoints.

6.  Staking: network participants lock a stake which corresponds to how
    likely they are chosen to create the next block. Receive fees for
    each time they create a block.

    -   Aligns incentives of miners with cryptocurrency;

    -   Prevents sybil attack: can't change the amount of money clones
        have;

    -   Stakes can be slashed;

    -   Raises money for blockchain startups.

    Why run own miner if you can lend someone your coins and have them
    mine for you? Still receive rewards proportional to the number of
    coins owned, convenient, and funds are still liquid. However, the
    delegee might have warped incentives: if they get slashed, it's
    still your coins that are being lost.