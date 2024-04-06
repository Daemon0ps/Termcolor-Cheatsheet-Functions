from termcolor import cprint
from mss.linux import MSS as mss
import cv2
import io
import mss.tools
import numpy as np


clr_d: dict = {
    "_bk": "black",
    "_r": "red",
    "_g": "green",
    "_y": "yellow",
    "_b": "blue",
    "_m": "magenta",
    "_c": "cyan",
    "_w": "white",
    "_lgr": "light_grey",
    "_dg": "dark_grey",
    "_lr": "light_red",
    "_lg": "light_green",
    "_ly": "light_yellow",
    "_lb": "light_blue",
    "_lm": "light_magenta",
    "_lc": "light_cyan",
    "_obk": "on_black",
    "_or": "on_red",
    "_og": "on_green",
    "_oy": "on_yellow",
    "_ob": "on_blue",
    "_om": "on_magenta",
    "_oc": "on_cyan",
    "_ow": "on_white",
    "_olgr": "on_light_grey",
    "_odg": "on_dark_grey",
    "_olr": "on_light_red",
    "_olg": "on_light_green",
    "_oly": "on_light_yellow",
    "_olb": "on_light_blue",
    "_olm": "on_light_magenta",
    "_olc": "on_light_cyan",
    "black": "_bk",
    "red": "_r",
    "green": "_g",
    "yellow": "_y",
    "blue": "_b",
    "magenta": "_m",
    "cyan": "_c",
    "white": "_w",
    "light_grey": "_lgr",
    "dark_grey": "_dg",
    "light_red": "_lr",
    "light_green": "_lg",
    "light_yellow": "_ly",
    "light_blue": "_lb",
    "light_magenta": "_lm",
    "light_cyan": "_lc",
    "on_black": "_obk",
    "on_red": "_or",
    "on_green": "_og",
    "on_yellow": "_oy",
    "on_blue": "_ob",
    "on_magenta": "_om",
    "on_cyan": "_oc",
    "on_white": "_ow",
    "on_light_grey": "_olgr",
    "on_dark_grey": "_odg",
    "on_light_red": "_olr",
    "on_light_green": "_olg",
    "on_light_yellow": "_oly",
    "on_light_blue": "_olb",
    "on_light_magenta": "_olm",
    "on_light_cyan": "_olc",
}

tc_list: list[str] = [
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "light_grey",
    "dark_grey",
    "light_red",
    "light_green",
    "light_yellow",
    "light_blue",
    "light_magenta",
    "light_cyan",
]


def imcb(image):
    def cb(img: np.array, tol: int = 20) -> list:
        mask = img > tol
        if img.ndim == 3:
            mask = np.array(mask).all(3)
        m, n = mask.shape
        mask0, mask1 = mask.any(0), mask.any(1)
        cs, ce = mask0.argmax(), n - mask0[::-1].argmax()
        rs, re = mask1.argmax(), m - mask1[::-1].argmax()
        return [rs, re, cs, ce]

    imgrey = np.array(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    ci = cb(imgrey, tol=40)
    return image[ci[0] : ci[1], ci[2] : ci[3]]


def _ss_txt(s):
    with mss.mss() as sct:
        monitor_number = 2
        mon = sct.monitors[monitor_number]
        monitor = {
            "top": mon["top"] + 1324,  # px from the top
            "left": mon["left"] + 2,  # 160,  # px from the left
            "width": 600,
            "height": 24,
            "mon": monitor_number,
        }
        sct_img = sct.grab(monitor)
        buf = io.BytesIO(mss.tools.to_png(sct_img.rgb, sct_img.size, output=None))
        buf.seek(0)
        cvimg = np.uint8(
            cv2.imdecode(np.asarray(bytearray(buf.read())), cv2.IMREAD_UNCHANGED)
        )
        img = imcb(cvimg)
        cv2.imwrite(f"e:/tc_colors/{s}.png", img)


def _clr_print():
    for tct in tc_list:
        cprint(str(tct), str(tct))
        cprint(str(tct), str(tct))
        _ss_txt(tct[0])
    for tct0 in tc_list:
        tct0 = str(f"on_{tct0}")
        for tct1 in tc_list:
            cprint(str(f"{tct1}---{tct0}"), tct1, tct0)
            cprint(str(f"{tct1}---{tct0}"), tct1, tct0)
            _ss_txt(tct[0])


tc_list = sorted(tc_list[::1], key=lambda x: x, reverse=False)

# _clr_print()

if __name__ == "__main__":
    github_clr: list[str] = []
    github_clr.append(
        rf"# [Termcolor](https://github.com/termcolor/termcolor) Shorthand Functions{chr(10)}Termcolor Cheatsheet Functions. Shorthand functions for printing in color.{chr(10)}All printing is done with `(,end='')` so `chr(10)` mult be appended or prepended.{chr(10)}{chr(10)}1.  **tc_shorthand.py**{chr(10)}      This is the actual shorthand module itself.{chr(10)}{chr(10)}2.  **tc_lamnbda_contructor.py**{chr(10)}      This is what I used to parse the former `tc_lambda_old.py` module that I was using for shorthand Termcolor functions.{chr(10)}{chr(10)}3.  **tc_lambda_old.py**{chr(10)}      The old functions/lambdas{chr(10)}    {chr(10)}https://github.com/termcolor/termcolor{chr(10)}{chr(10)}-----{chr(10)}{chr(10)}## Colors:"
    )
    max_tc = sorted(tc_list[::1], key=lambda x: len(x), reverse=True)[0]
    print(max_tc)
    max_len = len(
        str(
            rf'{chr(96)}{chr(96)}{chr(96)}_{clr_d[max_tc]}{clr_d[str(f"on_{max_tc}")]}k:{chr(96)}{chr(96)}{chr(96)}  ***{max_tc} Text on {max_tc} Background***'
        )
    )
    print(max_len)
    bklf: str = f"  - {chr(96)}{chr(96)}{chr(96)}_bklf:{chr(96)}{chr(96)}{chr(96)}  ***Black on Black + LF/chr(10)***"
    github_clr.append(bklf + chr(10))
    github_clr.append("|          TC_FUNC          |          COLORS          |")
    github_clr.append("| :------------------------ | :----------------------- |")
    for clr0 in tc_list:
        clr_img = cv2.imread(str(rf"e:/tc_colors/{clr0}.png"), cv2.IMREAD_ANYCOLOR)
        func_text: str = rf"| {chr(96)}{chr(96)}{chr(96)}{clr_d[clr0]}{chr(96)}{chr(96)}{chr(96)} :   ***{clr0} Text***"
        while len(func_text) < max_len:
            func_text = func_text + chr(32)
        func_text = func_text + "| "
        img_link: str = rf"![](./colors/{clr0}.png)"
        github_clr.append(func_text + img_link)
    for clr1 in tc_list:
        for clr0 in tc_list:
            clr_img = cv2.imread(
                str(rf'e:/tc_colors/{clr0}---{str(f"on_{clr1}")}.png'),
                cv2.IMREAD_ANYCOLOR,
            )
            func_text: str = rf'| {chr(96)}{chr(96)}{chr(96)}_{clr_d[clr0]}{clr_d[str(f"on_{clr1}")]}{chr(96)}{chr(96)}{chr(96)} :   ***{clr0} Text on {clr1} Background***'
            while len(func_text) < max_len:
                func_text = func_text + chr(32)
            func_text = func_text + "| "
            img_link: str = rf'![](./colors/{clr0}---{str(f"on_{clr1}")}.png)'
            github_clr.append(func_text + img_link)
    with open("e:/tc_colors/github_func_text.txt", "wt") as fi:
        fi.write(chr(10).join(ft for ft in github_clr))
