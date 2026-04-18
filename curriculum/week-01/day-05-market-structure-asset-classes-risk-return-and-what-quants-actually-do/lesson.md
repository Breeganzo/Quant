# Week 01 Fri: Market structure, asset classes, risk, return, and what quants actually do

**Estimated time:** 4 hours

## Study Blocks
- Block 1 (45 min): Understand what markets are and who participates.
- Block 2 (60 min): Learn major asset classes and return drivers.
- Block 3 (45 min): Map core risk types and why implementation matters.
- Block 4 (60 min): Clarify quant roles: buy-side, sell-side, risk, strats, and investment banking.
- Block 5 (30 min): Code table-building and interview drill.

## Why It Matters In Quant
You need a mental map of markets before learning pricing, forecasting, and strategy research.

## Learning Overview
A lot of confusion in early quant learning comes from knowing formulas without knowing the market context they belong to. This day fixes that.

The goal is not to master every asset class in one day. The goal is to build a clean mental map of markets, roles, and why quants are paid to solve specific problems.

## Core Concepts
### Market structure
- Simple explanation: Markets match buyers and sellers. Prices move because participants update beliefs, manage risk, or need liquidity.
- Technical depth: Market structure includes venues, order types, liquidity conditions, and how trades are executed.
- Finance example: A highly liquid index future behaves very differently from a small illiquid stock.

### Asset classes and risk drivers
- Simple explanation: Different instruments are moved by different forces: earnings for equities, rates for bonds, macro and flows for FX, supply and demand for commodities.
- Technical depth: Each asset class has distinct payoff structures, liquidity patterns, and risk exposures.
- Finance example: An equity drawdown, a bond duration shock, and an FX carry unwind are different risk stories.

### Buy-side, sell-side, and investment banking
- Simple explanation: Buy-side manages money and seeks returns. Sell-side serves clients, prices products, runs trading desks, and manages bank-side exposures. Investment banking is more deal-oriented than model-oriented.
- Technical depth: Buy-side quants focus more on alpha, portfolio construction, and PnL. Sell-side quants often support pricing, structuring, risk, execution, and desk infrastructure.
- Finance example: A hedge fund researcher testing a factor signal and a bank derivatives quant calibrating an options model are both quants, but their incentives and workflows differ.

## Worked Examples
- Equity example: stock returns depend on earnings, valuation, macro sensitivity, and sentiment.
- Bond example: price sensitivity to rates is linked to duration and convexity.
- Transaction costs matter more in high-turnover strategies because gross edge is repeatedly eaten by spread and slippage.

## Practice Questions With Answers
### Question: Why is investment banking not the same as quant trading?
Answer: Investment banking is centered on deals, capital raising, valuation, and client execution, while quant trading focuses on models, risk, pricing, and systematic decision making.

### Question: What is one major risk driver for fixed income?
Answer: Interest rates and the shape of the yield curve are central drivers, along with credit risk for credit products.

### Question: Why do transaction costs matter more in short-horizon strategies?
Answer: Because frequent trading causes costs to accumulate and can easily overwhelm a small raw edge.

## Coding Task
Build a markdown table in a notebook comparing 5 asset classes, their return drivers, and their main risks.

## Daily Interview Drill
### Q: What is the clearest difference between buy-side and sell-side quant work?
A: Buy-side is more directly tied to alpha and portfolio performance, while sell-side is more tied to pricing, client support, structuring, execution, and desk risk.

### Q: Why should a quant understand market structure early?
A: Because signals only matter if they can actually be implemented in the market without unrealistic assumptions.

## Reflection Question
Which part of finance feels most interesting right now: markets, trading, risk, or pricing?

## Completion Checklist
- I completed each study block or consciously rescheduled it.
- I rewrote the key formulas or concepts from memory.
- I finished the coding lab and checked the output.
- I added at least one item to the error log if something was unclear.
- I practiced at least one interview answer aloud.
