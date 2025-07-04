# RENs

Given a hypergraph $H=(V,E)$, and a subset of nodes $U \subseteq V$, a <b>R</b>ooted Hypergraph <b>E</b>go-<b>N</b>etwork (<b>REN</b>) is the resulting collection of hyperedges $\phi(U) \subseteq E$ in $H$ rooted on the set of nodes $U$. Here, rooted indicates that nodes in $U$ have certain relationships with the hyperedges obtained by $\phi(U)$, e.g., the nodes are contained in the hyperedges. A REN intuitively captures the local neighborhood of the node set $U$ according to a chosen definition of proximity of inclusion. Indeed, different choices of $\phi$, and thus of the chosen definition of proximity of inclusion, yield different types of RENs.

## Repository content

- jupyter notebook for generating the figures of the work: <i> Generalizing Hypergraph Ego-Networks and their Temporal Stability </i>, by Francesco Cauteruccio, Salvatore Citraro, Andrea Failla, and Giulio Rossetti, accepted @ ASONAM2025;
- .py with basic utils for building RENs.
