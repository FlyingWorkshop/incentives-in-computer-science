# P2P File-sharing Dilemma

Napster (1999-2001) had free file-sharing. People were happy with free
music but producers were unhappy because they could not get profits.
Around $40-60\%$ of all college dorm traffic was Napster. It was shut
down for copyright infringement.

From 2000 onwards, Gnutella provided a similar service but used
decentralized peer-to-peer (P2P) file-sharing. Much harder to shut down.

P2P file-sharing rely on users uploading content for sharing. A large
fraction of users are free-riders: people who only download but don't
upload at all. 2000: around 65% of users were free-riders, growing to
85% in the next few years. It is important to incentivizing uploads.

We can model this as a game. Two players, each a user of Gnutella. Each
player can either upload or free-ride. Payoffs are $-1$ for uploading,
$+3$ for downloading. Payoffs are as follows:

|             |  Upload  | Free-ride |
|-------------|:--------:|:---------:|
|   Upload    |   $2,2$  |   $-1,3$  |
|  Free-ride  |   $3,-1$ |   $0,0$   |


The outcome that maximizes the two players' payoff is for both to
upload.[^1] However, free-riding is a dominant strategy for each player,
so the dominant strategy Nash equilibrium is for both players to
free-ride leading to the socially worst payoffs of $(0,0)$.

## Repeated Games

What happens if we iterate the game $n$ times, and both players seek to
maximize total payoff across all iterations? One modeling choice:
whether or not agents can or cannot commit to future behavior is
important.

```{index} Subgame Perfect Nash Equilibrium
```
```{prf:definition} Subgame Perfect Nash Equilibrium
:label: subgame-perfect-nash-equilibrium
A Subgame Perfect Nash Equilibrium is a Nash Equilibrium that is also a
Nash Equilibrium at any subgame of the original game.
```

Intuitively, this definition just means that agent cannot commit to
suboptimal future behavior. Alternatively, it is a Nash equilibrium that
is valid by backwards induction.

```{prf:remark}
In this context, it means:

-   On day $n$, agents will play Nash equilibrium.

-   On day $n-1$, agents will evaluate their actions today assuming
    everyone plays Nash eq tomorrow and play Nash eq today.

-   So on and so forth.
```

What is the subgame perfect equilibrium of the repeated game?[^2]

-   In the $n$th iteration, free-riding is the dominant strategy so both
    players free-riding will be played.

-   In the $n-1$th iteration, both players will free-ride anyways in the
    future so free-riding today is still dominant.

-   By induction, free-riding is dominant in every iteration.

## Repeated Games with Discounting

Same setting as before, but after ever iteration there is a probability
$p$ for the game to stop.

-   the network gets shut down because of a lawsuit

-   you or your peer gets disconnected.

This is equivalent to modeling infinite repetitions with a discounted
future

-   there is some interest or inflation rate that decreases the value of
    future payoffs

-   people subjectively value the future less than how much they value
    today.

**Grim trigger strategy**: if there was ever a time where the other
player free-rides, then free-ride forever. Otherwise, upload.

Then, the other player's optimal strategy is either to always upload or
never upload.

-   Expected utility from always uploading is
    $2 + 2(1-p) + 2(1-p)^2 + \cdots = \frac{2}{p}$.

-   Expected utility from never uploading is
    $3 + 0(1-p) + 0(1-p)^2 + \cdots = 3$.

Thus, the other player always uploads whenever $p < 2/3$ and both
players playing grim trigger is a subgame perfect Nash equilibrium.

```{prf:remark}
Note that always uploading for both players is NOT a Nash equilibrium as
either player has a profitable deviation to always free-ride. Observe
that the Nash equilibrium of both players using grim-trigger is
strategically different but outcome equivalent.
```

For any run of the game, the number of iterations will be some number
$n$. But we proved earlier that for any $n$, the unique SPNE is for both
players to never upload. What changed? Players no longer know what $n$
is, so the logic of backwards induction no longer holds.

In practice, grim trigger is not very useful: what happens if there was
an accident and one person's connection was down? Not a stable solution
concept.

**Tit for Tat**: In stage one, upload. In all future stages, do whatever
the opponent did in the previous stage.

If one player commits to playing tit for tat, then the best response for
the other player is to always upload when $p < 2/3$ and free-ride
otherwise.

## BitTorrent Strategies

BitTorrent main P2P protocol for file-sharing (almost 30% of all upload
traffic). Users organized into swarms sharing the same file. A
decentralized tracker coordinates active uses in the swarm. Each file is
broken into pieces and all pieces are needed to complete a file.

**Default Strategy**:

-   Every 15-30 minutes, users contacts the tracker and requests a new
    random subset of swarm peers. Number of known peers grows over time.

-   Each user attempts to download from its peers.

-   Each user has $s$ slots and allocates $1/s$-fraction of upload
    bandwidth to each slot.

-   $s-1$ peers to receive a slot chosen using a variant of tit-for-tat:
    prioritize peers that sent you the most data ($s-1$ as the last slot
    is reserved fr pity uploads to random peers for optimistic
    unchoking.)

-   For each peer, priority given to uploading rare pieces.

**BitThief Strategy**:

-   Never upload anything.

-   Ask tracker for peers much more frequently so number of peers grows.

**BitTyrant Strategy**: send data to peers who *will* send you the most
data, not who *has* sent you the most data.

-   For each peer $j$, estimate amount of upload $u_j$ so $j$ unchokes
    you.

-   For each peer $j$\< estimate speed of download $d_j$ if $j$ unchokes
    you

-   Prioritize sending as much data as possible to peer with maximum
    $d_j/u_j$.

[^1]: But this would create an externality on content creators, which is
    outside the scope of this model.

[^2]: Formally speaking, this is the unique subgame-perfect Nash
    equilibrium.