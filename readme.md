# sPoNgEgArIfY

### A simple text maninpulation cli

## Usage
```app.py [-h] [--text TEXT] [--clipboard] [--surround SURROUND] (--spongegar | --leet)```

## Options:
`-t`: The text to manipulate. If not provided, contents of the keyboard will be used
`-c` will copy the output to the clipboard
`-s [argument]` will surround the text. eg: `-t "hello" -s'--++==' -sp` will yield `--++== hElLo ==++--` 
## Modes:
`--spongegar` or `-sp` will format to alternating upper and lowercase. Eg: input of `may i speak to the manager` yields `mAy i sPeAk tO ThE MaNaGeR`.

`--leet` or `-l` will format to leet-speak. Eg: input of `may i speak to the manager` yields `m4¥ 1 5p34|< 7Ø 7h3 m4n463r`