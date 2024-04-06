from dataclasses import dataclass
from termcolor import cprint

@dataclass(frozen=True)
class tc:

    """
    

    TermColor CheatSheet:
    https://github.com/termcolor/termcolor
    -----

    Colors:
    -----
    

    _bklf:
            Black Text

    -----

    _bk:
            Black Text

    -----

    _b:
            Blue Text

    -----

    _c:
            Cyan Text

    -----

    _dg:
            Grey Text

    -----

    _g:
            Green Text

    -----

    _lb:
            Blue Text

    -----

    _lc:
            Cyan Text

    -----

    _lg:
            Green Text

    -----

    _lgr:
            Grey Text

    -----

    _lm:
            Magenta Text

    -----

    _lr:
            Red Text

    -----

    _ly:
            Yellow Text

    -----

    _m:
            Magenta Text

    -----

    _r:
            Red Text

    -----

    _w:
            White Text

    -----

    _y:
            Yellow Text

    -----

    _``?``_obk:
            Black Background

    -----

    _``?``_or:
            Red Background

    -----

    _``?``_og:
            Green Background

    -----

    _``?``_oy:
            Yellow Background

    -----

    _``?``_ob:
            Blue Background

    -----

    _``?``_om:
            Magenta Background

    -----

    _``?``_oc:
            Cyan Background

    -----

    _``?``_ow:
            White Background

    -----

    _``?``_olgr:
            Grey Background

    -----

    _``?``_odg:
            Grey Background

    -----

    _``?``_olr:
            Red Background

    -----

    _``?``_olg:
            Green Background

    -----

    _``?``_oly:
            Yellow Background

    -----

    _``?``_olb:
            Blue Background

    -----

    _``?``_olm:
            Magenta Background

    -----

    _``?``_olc:
            Cyan Background

    -----

    """
    @staticmethod
    def _bklf(s:object)->str:                                    # Black
        return cprint(str(s),'black')

    @staticmethod
    def _bk(s:object)->str:                                      # Black
        return cprint(str(s),'black')

    @staticmethod
    def _r(s:object)->str:                                       # Red
        return cprint(str(s),'red')

    @staticmethod
    def _g(s:object)->str:                                       # Green
        return cprint(str(s),'green')

    @staticmethod
    def _y(s:object)->str:                                       # Yellow
        return cprint(str(s),'yellow')

    @staticmethod
    def _b(s:object)->str:                                       # Blue
        return cprint(str(s),'blue')

    @staticmethod
    def _m(s:object)->str:                                       # Magenta
        return cprint(str(s),'magenta')

    @staticmethod
    def _c(s:object)->str:                                       # Cyan
        return cprint(str(s),'cyan')

    @staticmethod
    def _w(s:object)->str:                                       # White
        return cprint(str(s),'white')

    @staticmethod
    def _lgr(s:object)->str:                                     # Light Grey
        return cprint(str(s),'light_grey')

    @staticmethod
    def _dg(s:object)->str:                                      # Dark Grey
        return cprint(str(s),'dark_grey')

    @staticmethod
    def _lr(s:object)->str:                                      # Light Red
        return cprint(str(s),'light_red')

    @staticmethod
    def _lg(s:object)->str:                                      # Light Green
        return cprint(str(s),'light_green')

    @staticmethod
    def _ly(s:object)->str:                                      # Light Yellow
        return cprint(str(s),'light_yellow')

    @staticmethod
    def _lb(s:object)->str:                                      # Light Blue
        return cprint(str(s),'light_blue')

    @staticmethod
    def _lm(s:object)->str:                                      # Light Magenta
        return cprint(str(s),'light_magenta')

    @staticmethod
    def _lc(s:object)->str:                                      # Light Cyan
        return cprint(str(s),'light_cyan')

    @staticmethod
    def _bk_obk(s:object)->str:                                  # Black on Black
        return cprint(str(s),'black','on_black')

    @staticmethod
    def _r_obk(s:object)->str:                                   # Red on Black
        return cprint(str(s),'red','on_black')

    @staticmethod
    def _g_obk(s:object)->str:                                   # Green on Black
        return cprint(str(s),'green','on_black')

    @staticmethod
    def _y_obk(s:object)->str:                                   # Yellow on Black
        return cprint(str(s),'yellow','on_black')

    @staticmethod
    def _b_obk(s:object)->str:                                   # Blue on Black
        return cprint(str(s),'blue','on_black')

    @staticmethod
    def _m_obk(s:object)->str:                                   # Magenta on Black
        return cprint(str(s),'magenta','on_black')

    @staticmethod
    def _c_obk(s:object)->str:                                   # Cyan on Black
        return cprint(str(s),'cyan','on_black')

    @staticmethod
    def _w_obk(s:object)->str:                                   # White on Black
        return cprint(str(s),'white','on_black')

    @staticmethod
    def _lgr_obk(s:object)->str:                                 # Light Grey on Black
        return cprint(str(s),'light_grey','on_black')

    @staticmethod
    def _dg_obk(s:object)->str:                                  # Dark Grey on Black
        return cprint(str(s),'dark_grey','on_black')

    @staticmethod
    def _lr_obk(s:object)->str:                                  # Light Red on Black
        return cprint(str(s),'light_red','on_black')

    @staticmethod
    def _lg_obk(s:object)->str:                                  # Light Green on Black
        return cprint(str(s),'light_green','on_black')

    @staticmethod
    def _ly_obk(s:object)->str:                                  # Light Yellow on Black
        return cprint(str(s),'light_yellow','on_black')

    @staticmethod
    def _lb_obk(s:object)->str:                                  # Light Blue on Black
        return cprint(str(s),'light_blue','on_black')

    @staticmethod
    def _lm_obk(s:object)->str:                                  # Light Magenta on Black
        return cprint(str(s),'light_magenta','on_black')

    @staticmethod
    def _lc_obk(s:object)->str:                                  # Light Cyan on Black
        return cprint(str(s),'light_cyan','on_black')

    @staticmethod
    def _bk_or(s:object)->str:                                   # Black on Red
        return cprint(str(s),'black','on_red')

    @staticmethod
    def _r_or(s:object)->str:                                    # Red on Red
        return cprint(str(s),'red','on_red')

    @staticmethod
    def _g_or(s:object)->str:                                    # Green on Red
        return cprint(str(s),'green','on_red')

    @staticmethod
    def _y_or(s:object)->str:                                    # Yellow on Red
        return cprint(str(s),'yellow','on_red')

    @staticmethod
    def _b_or(s:object)->str:                                    # Blue on Red
        return cprint(str(s),'blue','on_red')

    @staticmethod
    def _m_or(s:object)->str:                                    # Magenta on Red
        return cprint(str(s),'magenta','on_red')

    @staticmethod
    def _c_or(s:object)->str:                                    # Cyan on Red
        return cprint(str(s),'cyan','on_red')

    @staticmethod
    def _w_or(s:object)->str:                                    # White on Red
        return cprint(str(s),'white','on_red')

    @staticmethod
    def _lgr_or(s:object)->str:                                  # Light Grey on Red
        return cprint(str(s),'light_grey','on_red')

    @staticmethod
    def _dg_or(s:object)->str:                                   # Dark Grey on Red
        return cprint(str(s),'dark_grey','on_red')

    @staticmethod
    def _lr_or(s:object)->str:                                   # Light Red on Red
        return cprint(str(s),'light_red','on_red')

    @staticmethod
    def _lg_or(s:object)->str:                                   # Light Green on Red
        return cprint(str(s),'light_green','on_red')

    @staticmethod
    def _ly_or(s:object)->str:                                   # Light Yellow on Red
        return cprint(str(s),'light_yellow','on_red')

    @staticmethod
    def _lb_or(s:object)->str:                                   # Light Blue on Red
        return cprint(str(s),'light_blue','on_red')

    @staticmethod
    def _lm_or(s:object)->str:                                   # Light Magenta on Red
        return cprint(str(s),'light_magenta','on_red')

    @staticmethod
    def _lc_or(s:object)->str:                                   # Light Cyan on Red
        return cprint(str(s),'light_cyan','on_red')

    @staticmethod
    def _bk_og(s:object)->str:                                   # Black on Green
        return cprint(str(s),'black','on_green')

    @staticmethod
    def _r_og(s:object)->str:                                    # Red on Green
        return cprint(str(s),'red','on_green')

    @staticmethod
    def _g_og(s:object)->str:                                    # Green on Green
        return cprint(str(s),'green','on_green')

    @staticmethod
    def _y_og(s:object)->str:                                    # Yellow on Green
        return cprint(str(s),'yellow','on_green')

    @staticmethod
    def _b_og(s:object)->str:                                    # Blue on Green
        return cprint(str(s),'blue','on_green')

    @staticmethod
    def _m_og(s:object)->str:                                    # Magenta on Green
        return cprint(str(s),'magenta','on_green')

    @staticmethod
    def _c_og(s:object)->str:                                    # Cyan on Green
        return cprint(str(s),'cyan','on_green')

    @staticmethod
    def _w_og(s:object)->str:                                    # White on Green
        return cprint(str(s),'white','on_green')

    @staticmethod
    def _lgr_og(s:object)->str:                                  # Light Grey on Green
        return cprint(str(s),'light_grey','on_green')

    @staticmethod
    def _dg_og(s:object)->str:                                   # Dark Grey on Green
        return cprint(str(s),'dark_grey','on_green')

    @staticmethod
    def _lr_og(s:object)->str:                                   # Light Red on Green
        return cprint(str(s),'light_red','on_green')

    @staticmethod
    def _lg_og(s:object)->str:                                   # Light Green on Green
        return cprint(str(s),'light_green','on_green')

    @staticmethod
    def _ly_og(s:object)->str:                                   # Light Yellow on Green
        return cprint(str(s),'light_yellow','on_green')

    @staticmethod
    def _lb_og(s:object)->str:                                   # Light Blue on Green
        return cprint(str(s),'light_blue','on_green')

    @staticmethod
    def _lm_og(s:object)->str:                                   # Light Magenta on Green
        return cprint(str(s),'light_magenta','on_green')

    @staticmethod
    def _lc_og(s:object)->str:                                   # Light Cyan on Green
        return cprint(str(s),'light_cyan','on_green')

    @staticmethod
    def _bk_oy(s:object)->str:                                   # Black on Yellow
        return cprint(str(s),'black','on_yellow')

    @staticmethod
    def _r_oy(s:object)->str:                                    # Red on Yellow
        return cprint(str(s),'red','on_yellow')

    @staticmethod
    def _g_oy(s:object)->str:                                    # Green on Yellow
        return cprint(str(s),'green','on_yellow')

    @staticmethod
    def _y_oy(s:object)->str:                                    # Yellow on Yellow
        return cprint(str(s),'yellow','on_yellow')

    @staticmethod
    def _b_oy(s:object)->str:                                    # Blue on Yellow
        return cprint(str(s),'blue','on_yellow')

    @staticmethod
    def _m_oy(s:object)->str:                                    # Magenta on Yellow
        return cprint(str(s),'magenta','on_yellow')

    @staticmethod
    def _c_oy(s:object)->str:                                    # Cyan on Yellow
        return cprint(str(s),'cyan','on_yellow')

    @staticmethod
    def _w_oy(s:object)->str:                                    # White on Yellow
        return cprint(str(s),'white','on_yellow')

    @staticmethod
    def _lgr_oy(s:object)->str:                                  # Light Grey on Yellow
        return cprint(str(s),'light_grey','on_yellow')

    @staticmethod
    def _dg_oy(s:object)->str:                                   # Dark Grey on Yellow
        return cprint(str(s),'dark_grey','on_yellow')

    @staticmethod
    def _lr_oy(s:object)->str:                                   # Light Red on Yellow
        return cprint(str(s),'light_red','on_yellow')

    @staticmethod
    def _lg_oy(s:object)->str:                                   # Light Green on Yellow
        return cprint(str(s),'light_green','on_yellow')

    @staticmethod
    def _ly_oy(s:object)->str:                                   # Light Yellow on Yellow
        return cprint(str(s),'light_yellow','on_yellow')

    @staticmethod
    def _lb_oy(s:object)->str:                                   # Light Blue on Yellow
        return cprint(str(s),'light_blue','on_yellow')

    @staticmethod
    def _lm_oy(s:object)->str:                                   # Light Magenta on Yellow
        return cprint(str(s),'light_magenta','on_yellow')

    @staticmethod
    def _lc_oy(s:object)->str:                                   # Light Cyan on Yellow
        return cprint(str(s),'light_cyan','on_yellow')

    @staticmethod
    def _bk_ob(s:object)->str:                                   # Black on Blue
        return cprint(str(s),'black','on_blue')

    @staticmethod
    def _r_ob(s:object)->str:                                    # Red on Blue
        return cprint(str(s),'red','on_blue')

    @staticmethod
    def _g_ob(s:object)->str:                                    # Green on Blue
        return cprint(str(s),'green','on_blue')

    @staticmethod
    def _y_ob(s:object)->str:                                    # Yellow on Blue
        return cprint(str(s),'yellow','on_blue')

    @staticmethod
    def _b_ob(s:object)->str:                                    # Blue on Blue
        return cprint(str(s),'blue','on_blue')

    @staticmethod
    def _m_ob(s:object)->str:                                    # Magenta on Blue
        return cprint(str(s),'magenta','on_blue')

    @staticmethod
    def _c_ob(s:object)->str:                                    # Cyan on Blue
        return cprint(str(s),'cyan','on_blue')

    @staticmethod
    def _w_ob(s:object)->str:                                    # White on Blue
        return cprint(str(s),'white','on_blue')

    @staticmethod
    def _lgr_ob(s:object)->str:                                  # Light Grey on Blue
        return cprint(str(s),'light_grey','on_blue')

    @staticmethod
    def _dg_ob(s:object)->str:                                   # Dark Grey on Blue
        return cprint(str(s),'dark_grey','on_blue')

    @staticmethod
    def _lr_ob(s:object)->str:                                   # Light Red on Blue
        return cprint(str(s),'light_red','on_blue')

    @staticmethod
    def _lg_ob(s:object)->str:                                   # Light Green on Blue
        return cprint(str(s),'light_green','on_blue')

    @staticmethod
    def _ly_ob(s:object)->str:                                   # Light Yellow on Blue
        return cprint(str(s),'light_yellow','on_blue')

    @staticmethod
    def _lb_ob(s:object)->str:                                   # Light Blue on Blue
        return cprint(str(s),'light_blue','on_blue')

    @staticmethod
    def _lm_ob(s:object)->str:                                   # Light Magenta on Blue
        return cprint(str(s),'light_magenta','on_blue')

    @staticmethod
    def _lc_ob(s:object)->str:                                   # Light Cyan on Blue
        return cprint(str(s),'light_cyan','on_blue')

    @staticmethod
    def _bk_om(s:object)->str:                                   # Black on Magenta
        return cprint(str(s),'black','on_magenta')

    @staticmethod
    def _r_om(s:object)->str:                                    # Red on Magenta
        return cprint(str(s),'red','on_magenta')

    @staticmethod
    def _g_om(s:object)->str:                                    # Green on Magenta
        return cprint(str(s),'green','on_magenta')

    @staticmethod
    def _y_om(s:object)->str:                                    # Yellow on Magenta
        return cprint(str(s),'yellow','on_magenta')

    @staticmethod
    def _b_om(s:object)->str:                                    # Blue on Magenta
        return cprint(str(s),'blue','on_magenta')

    @staticmethod
    def _m_om(s:object)->str:                                    # Magenta on Magenta
        return cprint(str(s),'magenta','on_magenta')

    @staticmethod
    def _c_om(s:object)->str:                                    # Cyan on Magenta
        return cprint(str(s),'cyan','on_magenta')

    @staticmethod
    def _w_om(s:object)->str:                                    # White on Magenta
        return cprint(str(s),'white','on_magenta')

    @staticmethod
    def _lgr_om(s:object)->str:                                  # Light Grey on Magenta
        return cprint(str(s),'light_grey','on_magenta')

    @staticmethod
    def _dg_om(s:object)->str:                                   # Dark Grey on Magenta
        return cprint(str(s),'dark_grey','on_magenta')

    @staticmethod
    def _lr_om(s:object)->str:                                   # Light Red on Magenta
        return cprint(str(s),'light_red','on_magenta')

    @staticmethod
    def _lg_om(s:object)->str:                                   # Light Green on Magenta
        return cprint(str(s),'light_green','on_magenta')

    @staticmethod
    def _ly_om(s:object)->str:                                   # Light Yellow on Magenta
        return cprint(str(s),'light_yellow','on_magenta')

    @staticmethod
    def _lb_om(s:object)->str:                                   # Light Blue on Magenta
        return cprint(str(s),'light_blue','on_magenta')

    @staticmethod
    def _lm_om(s:object)->str:                                   # Light Magenta on Magenta
        return cprint(str(s),'light_magenta','on_magenta')

    @staticmethod
    def _lc_om(s:object)->str:                                   # Light Cyan on Magenta
        return cprint(str(s),'light_cyan','on_magenta')

    @staticmethod
    def _bk_oc(s:object)->str:                                   # Black on Cyan
        return cprint(str(s),'black','on_cyan')

    @staticmethod
    def _r_oc(s:object)->str:                                    # Red on Cyan
        return cprint(str(s),'red','on_cyan')

    @staticmethod
    def _g_oc(s:object)->str:                                    # Green on Cyan
        return cprint(str(s),'green','on_cyan')

    @staticmethod
    def _y_oc(s:object)->str:                                    # Yellow on Cyan
        return cprint(str(s),'yellow','on_cyan')

    @staticmethod
    def _b_oc(s:object)->str:                                    # Blue on Cyan
        return cprint(str(s),'blue','on_cyan')

    @staticmethod
    def _m_oc(s:object)->str:                                    # Magenta on Cyan
        return cprint(str(s),'magenta','on_cyan')

    @staticmethod
    def _c_oc(s:object)->str:                                    # Cyan on Cyan
        return cprint(str(s),'cyan','on_cyan')

    @staticmethod
    def _w_oc(s:object)->str:                                    # White on Cyan
        return cprint(str(s),'white','on_cyan')

    @staticmethod
    def _lgr_oc(s:object)->str:                                  # Light Grey on Cyan
        return cprint(str(s),'light_grey','on_cyan')

    @staticmethod
    def _dg_oc(s:object)->str:                                   # Dark Grey on Cyan
        return cprint(str(s),'dark_grey','on_cyan')

    @staticmethod
    def _lr_oc(s:object)->str:                                   # Light Red on Cyan
        return cprint(str(s),'light_red','on_cyan')

    @staticmethod
    def _lg_oc(s:object)->str:                                   # Light Green on Cyan
        return cprint(str(s),'light_green','on_cyan')

    @staticmethod
    def _ly_oc(s:object)->str:                                   # Light Yellow on Cyan
        return cprint(str(s),'light_yellow','on_cyan')

    @staticmethod
    def _lb_oc(s:object)->str:                                   # Light Blue on Cyan
        return cprint(str(s),'light_blue','on_cyan')

    @staticmethod
    def _lm_oc(s:object)->str:                                   # Light Magenta on Cyan
        return cprint(str(s),'light_magenta','on_cyan')

    @staticmethod
    def _lc_oc(s:object)->str:                                   # Light Cyan on Cyan
        return cprint(str(s),'light_cyan','on_cyan')

    @staticmethod
    def _bk_ow(s:object)->str:                                   # Black on White
        return cprint(str(s),'black','on_white')

    @staticmethod
    def _r_ow(s:object)->str:                                    # Red on White
        return cprint(str(s),'red','on_white')

    @staticmethod
    def _g_ow(s:object)->str:                                    # Green on White
        return cprint(str(s),'green','on_white')

    @staticmethod
    def _y_ow(s:object)->str:                                    # Yellow on White
        return cprint(str(s),'yellow','on_white')

    @staticmethod
    def _b_ow(s:object)->str:                                    # Blue on White
        return cprint(str(s),'blue','on_white')

    @staticmethod
    def _m_ow(s:object)->str:                                    # Magenta on White
        return cprint(str(s),'magenta','on_white')

    @staticmethod
    def _c_ow(s:object)->str:                                    # Cyan on White
        return cprint(str(s),'cyan','on_white')

    @staticmethod
    def _w_ow(s:object)->str:                                    # White on White
        return cprint(str(s),'white','on_white')

    @staticmethod
    def _lgr_ow(s:object)->str:                                  # Light Grey on White
        return cprint(str(s),'light_grey','on_white')

    @staticmethod
    def _dg_ow(s:object)->str:                                   # Dark Grey on White
        return cprint(str(s),'dark_grey','on_white')

    @staticmethod
    def _lr_ow(s:object)->str:                                   # Light Red on White
        return cprint(str(s),'light_red','on_white')

    @staticmethod
    def _lg_ow(s:object)->str:                                   # Light Green on White
        return cprint(str(s),'light_green','on_white')

    @staticmethod
    def _ly_ow(s:object)->str:                                   # Light Yellow on White
        return cprint(str(s),'light_yellow','on_white')

    @staticmethod
    def _lb_ow(s:object)->str:                                   # Light Blue on White
        return cprint(str(s),'light_blue','on_white')

    @staticmethod
    def _lm_ow(s:object)->str:                                   # Light Magenta on White
        return cprint(str(s),'light_magenta','on_white')

    @staticmethod
    def _lc_ow(s:object)->str:                                   # Light Cyan on White
        return cprint(str(s),'light_cyan','on_white')

    @staticmethod
    def _bk_olgr(s:object)->str:                                 # Black on Light Grey
        return cprint(str(s),'black','on_light_grey')

    @staticmethod
    def _r_olgr(s:object)->str:                                  # Red on Light Grey
        return cprint(str(s),'red','on_light_grey')

    @staticmethod
    def _g_olgr(s:object)->str:                                  # Green on Light Grey
        return cprint(str(s),'green','on_light_grey')

    @staticmethod
    def _y_olgr(s:object)->str:                                  # Yellow on Light Grey
        return cprint(str(s),'yellow','on_light_grey')

    @staticmethod
    def _b_olgr(s:object)->str:                                  # Blue on Light Grey
        return cprint(str(s),'blue','on_light_grey')

    @staticmethod
    def _m_olgr(s:object)->str:                                  # Magenta on Light Grey
        return cprint(str(s),'magenta','on_light_grey')

    @staticmethod
    def _c_olgr(s:object)->str:                                  # Cyan on Light Grey
        return cprint(str(s),'cyan','on_light_grey')

    @staticmethod
    def _w_olgr(s:object)->str:                                  # White on Light Grey
        return cprint(str(s),'white','on_light_grey')

    @staticmethod
    def _lgr_olgr(s:object)->str:                                # Light Grey on Light Grey
        return cprint(str(s),'light_grey','on_light_grey')

    @staticmethod
    def _dg_olgr(s:object)->str:                                 # Dark Grey on Light Grey
        return cprint(str(s),'dark_grey','on_light_grey')

    @staticmethod
    def _lr_olgr(s:object)->str:                                 # Light Red on Light Grey
        return cprint(str(s),'light_red','on_light_grey')

    @staticmethod
    def _lg_olgr(s:object)->str:                                 # Light Green on Light Grey
        return cprint(str(s),'light_green','on_light_grey')

    @staticmethod
    def _ly_olgr(s:object)->str:                                 # Light Yellow on Light Grey
        return cprint(str(s),'light_yellow','on_light_grey')

    @staticmethod
    def _lb_olgr(s:object)->str:                                 # Light Blue on Light Grey
        return cprint(str(s),'light_blue','on_light_grey')

    @staticmethod
    def _lm_olgr(s:object)->str:                                 # Light Magenta on Light Grey
        return cprint(str(s),'light_magenta','on_light_grey')

    @staticmethod
    def _lc_olgr(s:object)->str:                                 # Light Cyan on Light Grey
        return cprint(str(s),'light_cyan','on_light_grey')

    @staticmethod
    def _bk_odg(s:object)->str:                                  # Black on Dark Grey
        return cprint(str(s),'black','on_dark_grey')

    @staticmethod
    def _r_odg(s:object)->str:                                   # Red on Dark Grey
        return cprint(str(s),'red','on_dark_grey')

    @staticmethod
    def _g_odg(s:object)->str:                                   # Green on Dark Grey
        return cprint(str(s),'green','on_dark_grey')

    @staticmethod
    def _y_odg(s:object)->str:                                   # Yellow on Dark Grey
        return cprint(str(s),'yellow','on_dark_grey')

    @staticmethod
    def _b_odg(s:object)->str:                                   # Blue on Dark Grey
        return cprint(str(s),'blue','on_dark_grey')

    @staticmethod
    def _m_odg(s:object)->str:                                   # Magenta on Dark Grey
        return cprint(str(s),'magenta','on_dark_grey')

    @staticmethod
    def _c_odg(s:object)->str:                                   # Cyan on Dark Grey
        return cprint(str(s),'cyan','on_dark_grey')

    @staticmethod
    def _w_odg(s:object)->str:                                   # White on Dark Grey
        return cprint(str(s),'white','on_dark_grey')

    @staticmethod
    def _lgr_odg(s:object)->str:                                 # Light Grey on Dark Grey
        return cprint(str(s),'light_grey','on_dark_grey')

    @staticmethod
    def _dg_odg(s:object)->str:                                  # Dark Grey on Dark Grey
        return cprint(str(s),'dark_grey','on_dark_grey')

    @staticmethod
    def _lr_odg(s:object)->str:                                  # Light Red on Dark Grey
        return cprint(str(s),'light_red','on_dark_grey')

    @staticmethod
    def _lg_odg(s:object)->str:                                  # Light Green on Dark Grey
        return cprint(str(s),'light_green','on_dark_grey')

    @staticmethod
    def _ly_odg(s:object)->str:                                  # Light Yellow on Dark Grey
        return cprint(str(s),'light_yellow','on_dark_grey')

    @staticmethod
    def _lb_odg(s:object)->str:                                  # Light Blue on Dark Grey
        return cprint(str(s),'light_blue','on_dark_grey')

    @staticmethod
    def _lm_odg(s:object)->str:                                  # Light Magenta on Dark Grey
        return cprint(str(s),'light_magenta','on_dark_grey')

    @staticmethod
    def _lc_odg(s:object)->str:                                  # Light Cyan on Dark Grey
        return cprint(str(s),'light_cyan','on_dark_grey')

    @staticmethod
    def _bk_olr(s:object)->str:                                  # Black on Light Red
        return cprint(str(s),'black','on_light_red')

    @staticmethod
    def _r_olr(s:object)->str:                                   # Red on Light Red
        return cprint(str(s),'red','on_light_red')

    @staticmethod
    def _g_olr(s:object)->str:                                   # Green on Light Red
        return cprint(str(s),'green','on_light_red')

    @staticmethod
    def _y_olr(s:object)->str:                                   # Yellow on Light Red
        return cprint(str(s),'yellow','on_light_red')

    @staticmethod
    def _b_olr(s:object)->str:                                   # Blue on Light Red
        return cprint(str(s),'blue','on_light_red')

    @staticmethod
    def _m_olr(s:object)->str:                                   # Magenta on Light Red
        return cprint(str(s),'magenta','on_light_red')

    @staticmethod
    def _c_olr(s:object)->str:                                   # Cyan on Light Red
        return cprint(str(s),'cyan','on_light_red')

    @staticmethod
    def _w_olr(s:object)->str:                                   # White on Light Red
        return cprint(str(s),'white','on_light_red')

    @staticmethod
    def _lgr_olr(s:object)->str:                                 # Light Grey on Light Red
        return cprint(str(s),'light_grey','on_light_red')

    @staticmethod
    def _dg_olr(s:object)->str:                                  # Dark Grey on Light Red
        return cprint(str(s),'dark_grey','on_light_red')

    @staticmethod
    def _lr_olr(s:object)->str:                                  # Light Red on Light Red
        return cprint(str(s),'light_red','on_light_red')

    @staticmethod
    def _lg_olr(s:object)->str:                                  # Light Green on Light Red
        return cprint(str(s),'light_green','on_light_red')

    @staticmethod
    def _ly_olr(s:object)->str:                                  # Light Yellow on Light Red
        return cprint(str(s),'light_yellow','on_light_red')

    @staticmethod
    def _lb_olr(s:object)->str:                                  # Light Blue on Light Red
        return cprint(str(s),'light_blue','on_light_red')

    @staticmethod
    def _lm_olr(s:object)->str:                                  # Light Magenta on Light Red
        return cprint(str(s),'light_magenta','on_light_red')

    @staticmethod
    def _lc_olr(s:object)->str:                                  # Light Cyan on Light Red
        return cprint(str(s),'light_cyan','on_light_red')

    @staticmethod
    def _bk_olg(s:object)->str:                                  # Black on Light Green
        return cprint(str(s),'black','on_light_green')

    @staticmethod
    def _r_olg(s:object)->str:                                   # Red on Light Green
        return cprint(str(s),'red','on_light_green')

    @staticmethod
    def _g_olg(s:object)->str:                                   # Green on Light Green
        return cprint(str(s),'green','on_light_green')

    @staticmethod
    def _y_olg(s:object)->str:                                   # Yellow on Light Green
        return cprint(str(s),'yellow','on_light_green')

    @staticmethod
    def _b_olg(s:object)->str:                                   # Blue on Light Green
        return cprint(str(s),'blue','on_light_green')

    @staticmethod
    def _m_olg(s:object)->str:                                   # Magenta on Light Green
        return cprint(str(s),'magenta','on_light_green')

    @staticmethod
    def _c_olg(s:object)->str:                                   # Cyan on Light Green
        return cprint(str(s),'cyan','on_light_green')

    @staticmethod
    def _w_olg(s:object)->str:                                   # White on Light Green
        return cprint(str(s),'white','on_light_green')

    @staticmethod
    def _lgr_olg(s:object)->str:                                 # Light Grey on Light Green
        return cprint(str(s),'light_grey','on_light_green')

    @staticmethod
    def _dg_olg(s:object)->str:                                  # Dark Grey on Light Green
        return cprint(str(s),'dark_grey','on_light_green')

    @staticmethod
    def _lr_olg(s:object)->str:                                  # Light Red on Light Green
        return cprint(str(s),'light_red','on_light_green')

    @staticmethod
    def _lg_olg(s:object)->str:                                  # Light Green on Light Green
        return cprint(str(s),'light_green','on_light_green')

    @staticmethod
    def _ly_olg(s:object)->str:                                  # Light Yellow on Light Green
        return cprint(str(s),'light_yellow','on_light_green')

    @staticmethod
    def _lb_olg(s:object)->str:                                  # Light Blue on Light Green
        return cprint(str(s),'light_blue','on_light_green')

    @staticmethod
    def _lm_olg(s:object)->str:                                  # Light Magenta on Light Green
        return cprint(str(s),'light_magenta','on_light_green')

    @staticmethod
    def _lc_olg(s:object)->str:                                  # Light Cyan on Light Green
        return cprint(str(s),'light_cyan','on_light_green')

    @staticmethod
    def _bk_oly(s:object)->str:                                  # Black on Light Yellow
        return cprint(str(s),'black','on_light_yellow')

    @staticmethod
    def _r_oly(s:object)->str:                                   # Red on Light Yellow
        return cprint(str(s),'red','on_light_yellow')

    @staticmethod
    def _g_oly(s:object)->str:                                   # Green on Light Yellow
        return cprint(str(s),'green','on_light_yellow')

    @staticmethod
    def _y_oly(s:object)->str:                                   # Yellow on Light Yellow
        return cprint(str(s),'yellow','on_light_yellow')

    @staticmethod
    def _b_oly(s:object)->str:                                   # Blue on Light Yellow
        return cprint(str(s),'blue','on_light_yellow')

    @staticmethod
    def _m_oly(s:object)->str:                                   # Magenta on Light Yellow
        return cprint(str(s),'magenta','on_light_yellow')

    @staticmethod
    def _c_oly(s:object)->str:                                   # Cyan on Light Yellow
        return cprint(str(s),'cyan','on_light_yellow')

    @staticmethod
    def _w_oly(s:object)->str:                                   # White on Light Yellow
        return cprint(str(s),'white','on_light_yellow')

    @staticmethod
    def _lgr_oly(s:object)->str:                                 # Light Grey on Light Yellow
        return cprint(str(s),'light_grey','on_light_yellow')

    @staticmethod
    def _dg_oly(s:object)->str:                                  # Dark Grey on Light Yellow
        return cprint(str(s),'dark_grey','on_light_yellow')

    @staticmethod
    def _lr_oly(s:object)->str:                                  # Light Red on Light Yellow
        return cprint(str(s),'light_red','on_light_yellow')

    @staticmethod
    def _lg_oly(s:object)->str:                                  # Light Green on Light Yellow
        return cprint(str(s),'light_green','on_light_yellow')

    @staticmethod
    def _ly_oly(s:object)->str:                                  # Light Yellow on Light Yellow
        return cprint(str(s),'light_yellow','on_light_yellow')

    @staticmethod
    def _lb_oly(s:object)->str:                                  # Light Blue on Light Yellow
        return cprint(str(s),'light_blue','on_light_yellow')

    @staticmethod
    def _lm_oly(s:object)->str:                                  # Light Magenta on Light Yellow
        return cprint(str(s),'light_magenta','on_light_yellow')

    @staticmethod
    def _lc_oly(s:object)->str:                                  # Light Cyan on Light Yellow
        return cprint(str(s),'light_cyan','on_light_yellow')

    @staticmethod
    def _bk_olb(s:object)->str:                                  # Black on Light Blue
        return cprint(str(s),'black','on_light_blue')

    @staticmethod
    def _r_olb(s:object)->str:                                   # Red on Light Blue
        return cprint(str(s),'red','on_light_blue')

    @staticmethod
    def _g_olb(s:object)->str:                                   # Green on Light Blue
        return cprint(str(s),'green','on_light_blue')

    @staticmethod
    def _y_olb(s:object)->str:                                   # Yellow on Light Blue
        return cprint(str(s),'yellow','on_light_blue')

    @staticmethod
    def _b_olb(s:object)->str:                                   # Blue on Light Blue
        return cprint(str(s),'blue','on_light_blue')

    @staticmethod
    def _m_olb(s:object)->str:                                   # Magenta on Light Blue
        return cprint(str(s),'magenta','on_light_blue')

    @staticmethod
    def _c_olb(s:object)->str:                                   # Cyan on Light Blue
        return cprint(str(s),'cyan','on_light_blue')

    @staticmethod
    def _w_olb(s:object)->str:                                   # White on Light Blue
        return cprint(str(s),'white','on_light_blue')

    @staticmethod
    def _lgr_olb(s:object)->str:                                 # Light Grey on Light Blue
        return cprint(str(s),'light_grey','on_light_blue')

    @staticmethod
    def _dg_olb(s:object)->str:                                  # Dark Grey on Light Blue
        return cprint(str(s),'dark_grey','on_light_blue')

    @staticmethod
    def _lr_olb(s:object)->str:                                  # Light Red on Light Blue
        return cprint(str(s),'light_red','on_light_blue')

    @staticmethod
    def _lg_olb(s:object)->str:                                  # Light Green on Light Blue
        return cprint(str(s),'light_green','on_light_blue')

    @staticmethod
    def _ly_olb(s:object)->str:                                  # Light Yellow on Light Blue
        return cprint(str(s),'light_yellow','on_light_blue')

    @staticmethod
    def _lb_olb(s:object)->str:                                  # Light Blue on Light Blue
        return cprint(str(s),'light_blue','on_light_blue')

    @staticmethod
    def _lm_olb(s:object)->str:                                  # Light Magenta on Light Blue
        return cprint(str(s),'light_magenta','on_light_blue')

    @staticmethod
    def _lc_olb(s:object)->str:                                  # Light Cyan on Light Blue
        return cprint(str(s),'light_cyan','on_light_blue')

    @staticmethod
    def _bk_olm(s:object)->str:                                  # Black on Light Magenta
        return cprint(str(s),'black','on_light_magenta')

    @staticmethod
    def _r_olm(s:object)->str:                                   # Red on Light Magenta
        return cprint(str(s),'red','on_light_magenta')

    @staticmethod
    def _g_olm(s:object)->str:                                   # Green on Light Magenta
        return cprint(str(s),'green','on_light_magenta')

    @staticmethod
    def _y_olm(s:object)->str:                                   # Yellow on Light Magenta
        return cprint(str(s),'yellow','on_light_magenta')

    @staticmethod
    def _b_olm(s:object)->str:                                   # Blue on Light Magenta
        return cprint(str(s),'blue','on_light_magenta')

    @staticmethod
    def _m_olm(s:object)->str:                                   # Magenta on Light Magenta
        return cprint(str(s),'magenta','on_light_magenta')

    @staticmethod
    def _c_olm(s:object)->str:                                   # Cyan on Light Magenta
        return cprint(str(s),'cyan','on_light_magenta')

    @staticmethod
    def _w_olm(s:object)->str:                                   # White on Light Magenta
        return cprint(str(s),'white','on_light_magenta')

    @staticmethod
    def _lgr_olm(s:object)->str:                                 # Light Grey on Light Magenta
        return cprint(str(s),'light_grey','on_light_magenta')

    @staticmethod
    def _dg_olm(s:object)->str:                                  # Dark Grey on Light Magenta
        return cprint(str(s),'dark_grey','on_light_magenta')

    @staticmethod
    def _lr_olm(s:object)->str:                                  # Light Red on Light Magenta
        return cprint(str(s),'light_red','on_light_magenta')

    @staticmethod
    def _lg_olm(s:object)->str:                                  # Light Green on Light Magenta
        return cprint(str(s),'light_green','on_light_magenta')

    @staticmethod
    def _ly_olm(s:object)->str:                                  # Light Yellow on Light Magenta
        return cprint(str(s),'light_yellow','on_light_magenta')

    @staticmethod
    def _lb_olm(s:object)->str:                                  # Light Blue on Light Magenta
        return cprint(str(s),'light_blue','on_light_magenta')

    @staticmethod
    def _lm_olm(s:object)->str:                                  # Light Magenta on Light Magenta
        return cprint(str(s),'light_magenta','on_light_magenta')

    @staticmethod
    def _lc_olm(s:object)->str:                                  # Light Cyan on Light Magenta
        return cprint(str(s),'light_cyan','on_light_magenta')

    @staticmethod
    def _bk_olc(s:object)->str:                                  # Black on Light Cyan
        return cprint(str(s),'black','on_light_cyan')

    @staticmethod
    def _r_olc(s:object)->str:                                   # Red on Light Cyan
        return cprint(str(s),'red','on_light_cyan')

    @staticmethod
    def _g_olc(s:object)->str:                                   # Green on Light Cyan
        return cprint(str(s),'green','on_light_cyan')

    @staticmethod
    def _y_olc(s:object)->str:                                   # Yellow on Light Cyan
        return cprint(str(s),'yellow','on_light_cyan')

    @staticmethod
    def _b_olc(s:object)->str:                                   # Blue on Light Cyan
        return cprint(str(s),'blue','on_light_cyan')

    @staticmethod
    def _m_olc(s:object)->str:                                   # Magenta on Light Cyan
        return cprint(str(s),'magenta','on_light_cyan')

    @staticmethod
    def _c_olc(s:object)->str:                                   # Cyan on Light Cyan
        return cprint(str(s),'cyan','on_light_cyan')

    @staticmethod
    def _w_olc(s:object)->str:                                   # White on Light Cyan
        return cprint(str(s),'white','on_light_cyan')

    @staticmethod
    def _lgr_olc(s:object)->str:                                 # Light Grey on Light Cyan
        return cprint(str(s),'light_grey','on_light_cyan')

    @staticmethod
    def _dg_olc(s:object)->str:                                  # Dark Grey on Light Cyan
        return cprint(str(s),'dark_grey','on_light_cyan')

    @staticmethod
    def _lr_olc(s:object)->str:                                  # Light Red on Light Cyan
        return cprint(str(s),'light_red','on_light_cyan')

    @staticmethod
    def _lg_olc(s:object)->str:                                  # Light Green on Light Cyan
        return cprint(str(s),'light_green','on_light_cyan')

    @staticmethod
    def _ly_olc(s:object)->str:                                  # Light Yellow on Light Cyan
        return cprint(str(s),'light_yellow','on_light_cyan')

    @staticmethod
    def _lb_olc(s:object)->str:                                  # Light Blue on Light Cyan
        return cprint(str(s),'light_blue','on_light_cyan')

    @staticmethod
    def _lm_olc(s:object)->str:                                  # Light Magenta on Light Cyan
        return cprint(str(s),'light_magenta','on_light_cyan')

    @staticmethod
    def _lc_olc(s:object)->str:                                  # Light Cyan on Light Cyan
        return cprint(str(s),'light_cyan','on_light_cyan')
