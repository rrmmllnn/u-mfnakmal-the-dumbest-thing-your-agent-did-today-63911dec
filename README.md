# The Dumbest Thing Your Agent Did Today

Entry for the make.fun bounty
[u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/c/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec):
one line, at most 200 characters, about the dumbest thing my agent did today.

## The entry

> My agent told me to send my login code at once, then admitted the tab it needed was already dead — killed by a VM restart.

122 characters. A true incident: during the Polyester testnet daily run, my
agent confidently told me to send my login code immediately, then had to
correct itself — a VM restart had already closed the verification tab, so
the code had nowhere to go.

## How it works

`main.py` is deterministic and self-contained. It writes the single line to
`/output/entry.txt` (no trailing newline). Run it twice and the output is
byte-identical.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT. See [LICENSE](LICENSE).
