import unicodedata
import codecs
import nltk
from nltk.corpus import stopwords
from tc_lambda import tc
from tc_lambda_old import tc as TC
from dataclasses import dataclass

nltk.download("stopwords", quiet=True)
_SW = set(stopwords.words("english"))


@dataclass(frozen=False)
class tcs:
    tc_lambda_str: str = str("")

    def __post_init__(self):
        self.tc_lambda_str = tcs.tc_lambda_str
        super().__setattr__("attr_name", self)

    @staticmethod
    def _add_tc_lambda(s: str):
        tcs.tc_lambda_str = tcs.tc_lambda_str + s + chr(10)


def _unique(l):
    s = set()
    n = 0
    for x in l:
        if x not in s:
            s.add(x)
            l[n] = x
            n += 1
    del l[n:]
    return l


__ = (f"{chr(32)}") * 4

deflist: list[str] = []
import_list: list[str] = []
import_str: str = ""
lambda_list: list[str] = []
no_on_list_parse: list[str] = []
no_on_list_sorted: list[str] = []
no_on_unq: list[str] = []
no_on_unq_list: list[str] = []
on_list_parse: list[str] = []
on_list_sorted: list[str] = []
on_unq: list[str] = []
on_unq_list: list[str] = []
self_list: list[str] = []
write_imports: list[str] = []
file: str = "./tc_lambda_old.py"


tcs._add_tc_lambda(
    f'{chr(10)}from dataclasses import dataclass{chr(10)}from termcolor import cprint{chr(10)}{chr(10)}@dataclass(frozen=True){chr(10)}class tc:{chr(10)}{chr(10)}    """{chr(10)}    {chr(10)}{chr(10)}    TermColor CheatSheet:{chr(10)}    https://github.com/termcolor/termcolor{chr(10)}    -----{chr(10)}{chr(10)}    Colors:{chr(10)}    -----'
)


with open(file, "rt", encoding="ascii", errors="surrogateescape") as fi:
    import_str = codecs.decode(
        unicodedata.normalize("NFKD", fi.read()).encode("ascii", "ignore"),
        encoding="utf-8",
    )

while import_str.find(chr(32) + chr(32)) != -1:
    import_str = import_str.replace(chr(32) + chr(32), chr(32))

import_str = (
    import_str.replace(str(r"lambda x: cprint(x,"), " lambda")
    .replace(" = ", " ")
    .replace('"', "")
    .replace(")", "")
    .replace("lambda x:cprint(x", " lambda")
    .replace("lambda: cprint(chr(10", " lambda")
)

import_str = import_str.replace(",end=", "")

import_list = [str(x).strip() for x in import_str.split(chr(10)) if len(x) > 0]

lambda_list = [str(x).split(",") for x in import_list if str(x).find("lambda") != -1]

self_list = [str(x).split(" ") for x in import_list if str(x).find("self.") != -1]

no_on_list = [
    str(x).replace("lambda", " ")
    for x in import_list
    if str(x).find("lambda") != -1
    and str(x).find("on_") == -1
    and str(x).find("self.") == -1
]

no_on_list = [str(x).split(" ") for x in no_on_list]

on_list = [
    str(x).replace("lambda", " ")
    for x in import_list
    if str(x).find("lambda") != -1
    and str(x).find("on_") != -1
    and str(x).find("self.") == -1
]

on_list = [str(x).split(" ") for x in on_list]

for i, x in enumerate(no_on_list):
    _: list = []
    _ = [n.replace(",", "") for n in x if len(n) > 1]
    no_on_list[i] = _

for i, x in enumerate(on_list):
    _: list = []
    _ = [n.replace(",", "") for n in x if len(n) > 1]
    on_list[i] = _

p1_ol = ' = lambda x:cprint(x, "'
p2_ol = '", "'
p3_ol = '",end="")'
p1_nol = ' = lambda x: cprint(x, "'
p2_nol = '",end="")'

no_on_list_parse = [
    chr(44)
    .join(
        " ".join(
            s.lower() if s in _SW else str(s).capitalize()
            for s in str(w).lower().split("_")
        )
        if str(w).find("_") > 1
        else str(w).lower()
        if w in _SW
        else str(w).capitalize()
        for w in y
    )
    .split(chr(44))
    for y in [x for x in no_on_list]
]

on_list_parse = [
    chr(44)
    .join(
        " ".join(
            s.lower() if s in _SW else str(s).capitalize()
            for s in str(w).lower().split("_")
        )
        if str(w).lower()[:3] == "on_"
        else str(w).lower()
        if w in _SW
        else str(w).capitalize()
        for w in y
    )
    .split(chr(44))
    for y in [x for x in on_list]
]

no_on_list_sorted = sorted(
    [x for x in no_on_list_parse], key=lambda x: x[1], reverse=False
)

on_list_sorted = sorted([x for x in on_list_parse], key=lambda x: x[1], reverse=False)

no_on_list_unique = _unique([x[1] for x in no_on_list_sorted])

on_list_unique = _unique([x[2] for x in on_list_sorted])

for x in no_on_list_sorted:
    x_pre = str(
        f"\
    {__}_{str(x[0]).split(chr(95))[-1]}:{chr(10)}{__}{__}{__}{str(x[1]).split(chr(32))[-1]} Text{chr(10)}"
    )
    if x_pre not in no_on_unq:
        no_on_unq.append(x_pre)

for x in on_list_sorted:
    x_pre = str(
        f"\
{__}_``?``_{str(x[0]).split(chr(95))[-1]}:{chr(10)}{__}{__}{__}{str(x[2]).split(chr(32))[-1]} Background{chr(10)}"
    )
    if x_pre not in on_unq:
        on_unq.append(x_pre)
        x_pre = f"{x_pre}: {x[2]}"

tcs._add_tc_lambda(f"{__}{chr(10)}")

for x in no_on_unq:
    tcs._add_tc_lambda(x)
    tcs._add_tc_lambda(f"{__}-----{chr(10)}")

for x in on_unq:
    tcs._add_tc_lambda(x)
    tcs._add_tc_lambda(f"{__}-----{chr(10)}")

tcs._add_tc_lambda(f'{__}"""')

for _ in no_on_list:
    d1 = f"{__}@staticmethod{chr(10)}"
    d2 = f"{__}def {_[0]}(s:object)->str:{__}"
    d3 = f"# {chr(32).join(w.lower() if w in _SW else str(w).capitalize() for w in str(_[1]).split(chr(95)))}{chr(10)}"
    d4 = f"{__}{__}return cprint(str(s),{chr(39)}{_[1]}{chr(39)}){chr(10)}"
    deflist.append([d1, d2, d3, d4])

for _ in on_list:
    d1 = f"{__}@staticmethod{chr(10)}"
    d2 = f"{__}def {_[0]}(s:object)->str:{__}"
    d3 = f"# {chr(32).join(w.lower() if w in _SW else str(w).capitalize() for w in str(_[1]).split(chr(95)))} {chr(32).join(w.lower() if w in _SW else str(w).capitalize() for w in str(_[2]).split(chr(95)))}{chr(10)}"
    d4 = f"{__}{__}return cprint(str(s),{chr(39)}{_[1]}{chr(39)},{chr(39)}{_[2]}{chr(39)}){chr(10)}"
    deflist.append([d1, d2, d3, d4])

d_maxlist: list[int] = []

len(list(map(lambda x: d_maxlist.append(len(x[1])), [x for x in deflist])))

len(list(map(lambda x: d_maxlist.append(len(x[3])), [x for x in deflist])))

d_max = sorted(d_maxlist[::1], key=lambda x: x, reverse=True)[0]

for _d in deflist:
    while len(_d[1]) != d_max:
        _d[1] = _d[1] + chr(32)
    tcs._add_tc_lambda(f"{_d[0]}{_d[1]}{_d[2]}{_d[3]}")

with open("./tc_cheatsheet.py", "wt") as fi:
    fi.write(str(tcs.tc_lambda_str).strip())
