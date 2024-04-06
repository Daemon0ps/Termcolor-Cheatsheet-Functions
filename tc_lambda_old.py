from dataclasses import dataclass
from termcolor import cprint

@dataclass(frozen=True)
class tc:
    # _bklf = lambda: cprint(chr(10), "black")
    # _bk = lambda x: cprint(x, "black",end="")
    # _r = lambda x: cprint(x, "red",end="")
    # _g = lambda x: cprint(x, "green",end="")
    # _y = lambda x: cprint(x, "yellow",end="")
    # _b = lambda x: cprint(x, "blue",end="")
    # _m = lambda x: cprint(x, "magenta",end="")
    # _c = lambda x: cprint(x, "cyan",end="")
    # _w = lambda x: cprint(x, "white",end="")
    # _lgr = lambda x: cprint(x, "light_grey",end="")
    # _dg = lambda x: cprint(x, "dark_grey",end="")
    # _lr = lambda x: cprint(x, "light_red",end="")
    # _lg = lambda x: cprint(x, "light_green",end="")
    # _ly = lambda x: cprint(x, "light_yellow",end="")
    # _lb = lambda x: cprint(x, "light_blue",end="")
    # _lm = lambda x: cprint(x, "light_magenta",end="")
    # _lc = lambda x: cprint(x, "light_cyan",end="")
    # _bk_obk = lambda x:cprint(x, "black", "on_black",end="")
    # _r_obk = lambda x:cprint(x, "red", "on_black",end="")
    # _g_obk = lambda x:cprint(x, "green", "on_black",end="")
    # _y_obk = lambda x:cprint(x, "yellow", "on_black",end="")
    # _b_obk = lambda x:cprint(x, "blue", "on_black",end="")
    # _m_obk = lambda x:cprint(x, "magenta", "on_black",end="")
    # _c_obk = lambda x:cprint(x, "cyan", "on_black",end="")
    # _w_obk = lambda x:cprint(x, "white", "on_black",end="")
    # _lgr_obk = lambda x:cprint(x, "light_grey", "on_black",end="")
    # _dg_obk = lambda x:cprint(x, "dark_grey", "on_black",end="")
    # _lr_obk = lambda x:cprint(x, "light_red", "on_black",end="")
    # _lg_obk = lambda x:cprint(x, "light_green", "on_black",end="")
    # _ly_obk = lambda x:cprint(x, "light_yellow", "on_black",end="")
    # _lb_obk = lambda x:cprint(x, "light_blue", "on_black",end="")
    # _lm_obk = lambda x:cprint(x, "light_magenta", "on_black",end="")
    # _lc_obk = lambda x:cprint(x, "light_cyan", "on_black",end="")
    # _bk_or = lambda x:cprint(x, "black", "on_red",end="")
    # _r_or = lambda x:cprint(x, "red", "on_red",end="")
    # _g_or = lambda x:cprint(x, "green", "on_red",end="")
    # _y_or = lambda x:cprint(x, "yellow", "on_red",end="")
    # _b_or = lambda x:cprint(x, "blue", "on_red",end="")
    # _m_or = lambda x:cprint(x, "magenta", "on_red",end="")
    # _c_or = lambda x:cprint(x, "cyan", "on_red",end="")
    # _w_or = lambda x:cprint(x, "white", "on_red",end="")
    # _lgr_or = lambda x:cprint(x, "light_grey", "on_red",end="")
    # _dg_or = lambda x:cprint(x, "dark_grey", "on_red",end="")
    # _lr_or = lambda x:cprint(x, "light_red", "on_red",end="")
    # _lg_or = lambda x:cprint(x, "light_green", "on_red",end="")
    # _ly_or = lambda x:cprint(x, "light_yellow", "on_red",end="")
    # _lb_or = lambda x:cprint(x, "light_blue", "on_red",end="")
    # _lm_or = lambda x:cprint(x, "light_magenta", "on_red",end="")
    # _lc_or = lambda x:cprint(x, "light_cyan", "on_red",end="")
    # _bk_og = lambda x:cprint(x, "black", "on_green",end="")
    # _r_og = lambda x:cprint(x, "red", "on_green",end="")
    # _g_og = lambda x:cprint(x, "green", "on_green",end="")
    # _y_og = lambda x:cprint(x, "yellow", "on_green",end="")
    # _b_og = lambda x:cprint(x, "blue", "on_green",end="")
    # _m_og = lambda x:cprint(x, "magenta", "on_green",end="")
    # _c_og = lambda x:cprint(x, "cyan", "on_green",end="")
    # _w_og = lambda x:cprint(x, "white", "on_green",end="")
    # _lgr_og = lambda x:cprint(x, "light_grey", "on_green",end="")
    # _dg_og = lambda x:cprint(x, "dark_grey", "on_green",end="")
    # _lr_og = lambda x:cprint(x, "light_red", "on_green",end="")
    # _lg_og = lambda x:cprint(x, "light_green", "on_green",end="")
    # _ly_og = lambda x:cprint(x, "light_yellow", "on_green",end="")
    # _lb_og = lambda x:cprint(x, "light_blue", "on_green",end="")
    # _lm_og = lambda x:cprint(x, "light_magenta", "on_green",end="")
    # _lc_og = lambda x:cprint(x, "light_cyan", "on_green",end="")
    # _bk_oy = lambda x:cprint(x, "black", "on_yellow",end="")
    # _r_oy = lambda x:cprint(x, "red", "on_yellow",end="")
    # _g_oy = lambda x:cprint(x, "green", "on_yellow",end="")
    # _y_oy = lambda x:cprint(x, "yellow", "on_yellow",end="")
    # _b_oy = lambda x:cprint(x, "blue", "on_yellow",end="")
    # _m_oy = lambda x:cprint(x, "magenta", "on_yellow",end="")
    # _c_oy = lambda x:cprint(x, "cyan", "on_yellow",end="")
    # _w_oy = lambda x:cprint(x, "white", "on_yellow",end="")
    # _lgr_oy = lambda x:cprint(x, "light_grey", "on_yellow",end="")
    # _dg_oy = lambda x:cprint(x, "dark_grey", "on_yellow",end="")
    # _lr_oy = lambda x:cprint(x, "light_red", "on_yellow",end="")
    # _lg_oy = lambda x:cprint(x, "light_green", "on_yellow",end="")
    # _ly_oy = lambda x:cprint(x, "light_yellow", "on_yellow",end="")
    # _lb_oy = lambda x:cprint(x, "light_blue", "on_yellow",end="")
    # _lm_oy = lambda x:cprint(x, "light_magenta", "on_yellow",end="")
    # _lc_oy = lambda x:cprint(x, "light_cyan", "on_yellow",end="")
    # _bk_ob = lambda x:cprint(x, "black", "on_blue",end="")
    # _r_ob = lambda x:cprint(x, "red", "on_blue",end="")
    # _g_ob = lambda x:cprint(x, "green", "on_blue",end="")
    # _y_ob = lambda x:cprint(x, "yellow", "on_blue",end="")
    # _b_ob = lambda x:cprint(x, "blue", "on_blue",end="")
    # _m_ob = lambda x:cprint(x, "magenta", "on_blue",end="")
    # _c_ob = lambda x:cprint(x, "cyan", "on_blue",end="")
    # _w_ob = lambda x:cprint(x, "white", "on_blue",end="")
    # _lgr_ob = lambda x:cprint(x, "light_grey", "on_blue",end="")
    # _dg_ob = lambda x:cprint(x, "dark_grey", "on_blue",end="")
    # _lr_ob = lambda x:cprint(x, "light_red", "on_blue",end="")
    # _lg_ob = lambda x:cprint(x, "light_green", "on_blue",end="")
    # _ly_ob = lambda x:cprint(x, "light_yellow", "on_blue",end="")
    # _lb_ob = lambda x:cprint(x, "light_blue", "on_blue",end="")
    # _lm_ob = lambda x:cprint(x, "light_magenta", "on_blue",end="")
    # _lc_ob = lambda x:cprint(x, "light_cyan", "on_blue",end="")
    # _bk_om = lambda x:cprint(x, "black", "on_magenta",end="")
    # _r_om = lambda x:cprint(x, "red", "on_magenta",end="")
    # _g_om = lambda x:cprint(x, "green", "on_magenta",end="")
    # _y_om = lambda x:cprint(x, "yellow", "on_magenta",end="")
    # _b_om = lambda x:cprint(x, "blue", "on_magenta",end="")
    # _m_om = lambda x:cprint(x, "magenta", "on_magenta",end="")
    # _c_om = lambda x:cprint(x, "cyan", "on_magenta",end="")
    # _w_om = lambda x:cprint(x, "white", "on_magenta",end="")
    # _lgr_om = lambda x:cprint(x, "light_grey", "on_magenta",end="")
    # _dg_om = lambda x:cprint(x, "dark_grey", "on_magenta",end="")
    # _lr_om = lambda x:cprint(x, "light_red", "on_magenta",end="")
    # _lg_om = lambda x:cprint(x, "light_green", "on_magenta",end="")
    # _ly_om = lambda x:cprint(x, "light_yellow", "on_magenta",end="")
    # _lb_om = lambda x:cprint(x, "light_blue", "on_magenta",end="")
    # _lm_om = lambda x:cprint(x, "light_magenta", "on_magenta",end="")
    # _lc_om = lambda x:cprint(x, "light_cyan", "on_magenta",end="")
    # _bk_oc = lambda x:cprint(x, "black", "on_cyan",end="")
    # _r_oc = lambda x:cprint(x, "red", "on_cyan",end="")
    # _g_oc = lambda x:cprint(x, "green", "on_cyan",end="")
    # _y_oc = lambda x:cprint(x, "yellow", "on_cyan",end="")
    # _b_oc = lambda x:cprint(x, "blue", "on_cyan",end="")
    # _m_oc = lambda x:cprint(x, "magenta", "on_cyan",end="")
    # _c_oc = lambda x:cprint(x, "cyan", "on_cyan",end="")
    # _w_oc = lambda x:cprint(x, "white", "on_cyan",end="")
    # _lgr_oc = lambda x:cprint(x, "light_grey", "on_cyan",end="")
    # _dg_oc = lambda x:cprint(x, "dark_grey", "on_cyan",end="")
    # _lr_oc = lambda x:cprint(x, "light_red", "on_cyan",end="")
    # _lg_oc = lambda x:cprint(x, "light_green", "on_cyan",end="")
    # _ly_oc = lambda x:cprint(x, "light_yellow", "on_cyan",end="")
    # _lb_oc = lambda x:cprint(x, "light_blue", "on_cyan",end="")
    # _lm_oc = lambda x:cprint(x, "light_magenta", "on_cyan",end="")
    # _lc_oc = lambda x:cprint(x, "light_cyan", "on_cyan",end="")
    # _bk_ow = lambda x:cprint(x, "black", "on_white",end="")
    # _r_ow = lambda x:cprint(x, "red", "on_white",end="")
    # _g_ow = lambda x:cprint(x, "green", "on_white",end="")
    # _y_ow = lambda x:cprint(x, "yellow", "on_white",end="")
    # _b_ow = lambda x:cprint(x, "blue", "on_white",end="")
    # _m_ow = lambda x:cprint(x, "magenta", "on_white",end="")
    # _c_ow = lambda x:cprint(x, "cyan", "on_white",end="")
    # _w_ow = lambda x:cprint(x, "white", "on_white",end="")
    # _lgr_ow = lambda x:cprint(x, "light_grey", "on_white",end="")
    # _dg_ow = lambda x:cprint(x, "dark_grey", "on_white",end="")
    # _lr_ow = lambda x:cprint(x, "light_red", "on_white",end="")
    # _lg_ow = lambda x:cprint(x, "light_green", "on_white",end="")
    # _ly_ow = lambda x:cprint(x, "light_yellow", "on_white",end="")
    # _lb_ow = lambda x:cprint(x, "light_blue", "on_white",end="")
    # _lm_ow = lambda x:cprint(x, "light_magenta", "on_white",end="")
    # _lc_ow = lambda x:cprint(x, "light_cyan", "on_white",end="")
    # _bk_olgr = lambda x:cprint(x, "black", "on_light_grey",end="")
    # _r_olgr = lambda x:cprint(x, "red", "on_light_grey",end="")
    # _g_olgr = lambda x:cprint(x, "green", "on_light_grey",end="")
    # _y_olgr = lambda x:cprint(x, "yellow", "on_light_grey",end="")
    # _b_olgr = lambda x:cprint(x, "blue", "on_light_grey",end="")
    # _m_olgr = lambda x:cprint(x, "magenta", "on_light_grey",end="")
    # _c_olgr = lambda x:cprint(x, "cyan", "on_light_grey",end="")
    # _w_olgr = lambda x:cprint(x, "white", "on_light_grey",end="")
    # _lgr_olgr = lambda x:cprint(x, "light_grey", "on_light_grey",end="")
    # _dg_olgr = lambda x:cprint(x, "dark_grey", "on_light_grey",end="")
    # _lr_olgr = lambda x:cprint(x, "light_red", "on_light_grey",end="")
    # _lg_olgr = lambda x:cprint(x, "light_green", "on_light_grey",end="")
    # _ly_olgr = lambda x:cprint(x, "light_yellow", "on_light_grey",end="")
    # _lb_olgr = lambda x:cprint(x, "light_blue", "on_light_grey",end="")
    # _lm_olgr = lambda x:cprint(x, "light_magenta", "on_light_grey",end="")
    # _lc_olgr = lambda x:cprint(x, "light_cyan", "on_light_grey",end="")
    # _bk_odg = lambda x:cprint(x, "black", "on_dark_grey",end="")
    # _r_odg = lambda x:cprint(x, "red", "on_dark_grey",end="")
    # _g_odg = lambda x:cprint(x, "green", "on_dark_grey",end="")
    # _y_odg = lambda x:cprint(x, "yellow", "on_dark_grey",end="")
    # _b_odg = lambda x:cprint(x, "blue", "on_dark_grey",end="")
    # _m_odg = lambda x:cprint(x, "magenta", "on_dark_grey",end="")
    # _c_odg = lambda x:cprint(x, "cyan", "on_dark_grey",end="")
    # _w_odg = lambda x:cprint(x, "white", "on_dark_grey",end="")
    # _lgr_odg = lambda x:cprint(x, "light_grey", "on_dark_grey",end="")
    # _dg_odg = lambda x:cprint(x, "dark_grey", "on_dark_grey",end="")
    # _lr_odg = lambda x:cprint(x, "light_red", "on_dark_grey",end="")
    # _lg_odg = lambda x:cprint(x, "light_green", "on_dark_grey",end="")
    # _ly_odg = lambda x:cprint(x, "light_yellow", "on_dark_grey",end="")
    # _lb_odg = lambda x:cprint(x, "light_blue", "on_dark_grey",end="")
    # _lm_odg = lambda x:cprint(x, "light_magenta", "on_dark_grey",end="")
    # _lc_odg = lambda x:cprint(x, "light_cyan", "on_dark_grey",end="")
    # _bk_olr = lambda x:cprint(x, "black", "on_light_red",end="")
    # _r_olr = lambda x:cprint(x, "red", "on_light_red",end="")
    # _g_olr = lambda x:cprint(x, "green", "on_light_red",end="")
    # _y_olr = lambda x:cprint(x, "yellow", "on_light_red",end="")
    # _b_olr = lambda x:cprint(x, "blue", "on_light_red",end="")
    # _m_olr = lambda x:cprint(x, "magenta", "on_light_red",end="")
    # _c_olr = lambda x:cprint(x, "cyan", "on_light_red",end="")
    # _w_olr = lambda x:cprint(x, "white", "on_light_red",end="")
    # _lgr_olr = lambda x:cprint(x, "light_grey", "on_light_red",end="")
    # _dg_olr = lambda x:cprint(x, "dark_grey", "on_light_red",end="")
    # _lr_olr = lambda x:cprint(x, "light_red", "on_light_red",end="")
    # _lg_olr = lambda x:cprint(x, "light_green", "on_light_red",end="")
    # _ly_olr = lambda x:cprint(x, "light_yellow", "on_light_red",end="")
    # _lb_olr = lambda x:cprint(x, "light_blue", "on_light_red",end="")
    # _lm_olr = lambda x:cprint(x, "light_magenta", "on_light_red",end="")
    # _lc_olr = lambda x:cprint(x, "light_cyan", "on_light_red",end="")
    # _bk_olg = lambda x:cprint(x, "black", "on_light_green",end="")
    # _r_olg = lambda x:cprint(x, "red", "on_light_green",end="")
    # _g_olg = lambda x:cprint(x, "green", "on_light_green",end="")
    # _y_olg = lambda x:cprint(x, "yellow", "on_light_green",end="")
    # _b_olg = lambda x:cprint(x, "blue", "on_light_green",end="")
    # _m_olg = lambda x:cprint(x, "magenta", "on_light_green",end="")
    # _c_olg = lambda x:cprint(x, "cyan", "on_light_green",end="")
    # _w_olg = lambda x:cprint(x, "white", "on_light_green",end="")
    # _lgr_olg = lambda x:cprint(x, "light_grey", "on_light_green",end="")
    # _dg_olg = lambda x:cprint(x, "dark_grey", "on_light_green",end="")
    # _lr_olg = lambda x:cprint(x, "light_red", "on_light_green",end="")
    # _lg_olg = lambda x:cprint(x, "light_green", "on_light_green",end="")
    # _ly_olg = lambda x:cprint(x, "light_yellow", "on_light_green",end="")
    # _lb_olg = lambda x:cprint(x, "light_blue", "on_light_green",end="")
    # _lm_olg = lambda x:cprint(x, "light_magenta", "on_light_green",end="")
    # _lc_olg = lambda x:cprint(x, "light_cyan", "on_light_green",end="")
    # _bk_oly = lambda x:cprint(x, "black", "on_light_yellow",end="")
    # _r_oly = lambda x:cprint(x, "red", "on_light_yellow",end="")
    # _g_oly = lambda x:cprint(x, "green", "on_light_yellow",end="")
    # _y_oly = lambda x:cprint(x, "yellow", "on_light_yellow",end="")
    # _b_oly = lambda x:cprint(x, "blue", "on_light_yellow",end="")
    # _m_oly = lambda x:cprint(x, "magenta", "on_light_yellow",end="")
    # _c_oly = lambda x:cprint(x, "cyan", "on_light_yellow",end="")
    # _w_oly = lambda x:cprint(x, "white", "on_light_yellow",end="")
    # _lgr_oly = lambda x:cprint(x, "light_grey", "on_light_yellow",end="")
    # _dg_oly = lambda x:cprint(x, "dark_grey", "on_light_yellow",end="")
    # _lr_oly = lambda x:cprint(x, "light_red", "on_light_yellow",end="")
    # _lg_oly = lambda x:cprint(x, "light_green", "on_light_yellow",end="")
    # _ly_oly = lambda x:cprint(x, "light_yellow", "on_light_yellow",end="")
    # _lb_oly = lambda x:cprint(x, "light_blue", "on_light_yellow",end="")
    # _lm_oly = lambda x:cprint(x, "light_magenta", "on_light_yellow",end="")
    # _lc_oly = lambda x:cprint(x, "light_cyan", "on_light_yellow",end="")
    # _bk_olb = lambda x:cprint(x, "black", "on_light_blue",end="")
    # _r_olb = lambda x:cprint(x, "red", "on_light_blue",end="")
    # _g_olb = lambda x:cprint(x, "green", "on_light_blue",end="")
    # _y_olb = lambda x:cprint(x, "yellow", "on_light_blue",end="")
    # _b_olb = lambda x:cprint(x, "blue", "on_light_blue",end="")
    # _m_olb = lambda x:cprint(x, "magenta", "on_light_blue",end="")
    # _c_olb = lambda x:cprint(x, "cyan", "on_light_blue",end="")
    # _w_olb = lambda x:cprint(x, "white", "on_light_blue",end="")
    # _lgr_olb = lambda x:cprint(x, "light_grey", "on_light_blue",end="")
    # _dg_olb = lambda x:cprint(x, "dark_grey", "on_light_blue",end="")
    # _lr_olb = lambda x:cprint(x, "light_red", "on_light_blue",end="")
    # _lg_olb = lambda x:cprint(x, "light_green", "on_light_blue",end="")
    # _ly_olb = lambda x:cprint(x, "light_yellow", "on_light_blue",end="")
    # _lb_olb = lambda x:cprint(x, "light_blue", "on_light_blue",end="")
    # _lm_olb = lambda x:cprint(x, "light_magenta", "on_light_blue",end="")
    # _lc_olb = lambda x:cprint(x, "light_cyan", "on_light_blue",end="")
    # _bk_olm = lambda x:cprint(x, "black", "on_light_magenta",end="")
    # _r_olm = lambda x:cprint(x, "red", "on_light_magenta",end="")
    # _g_olm = lambda x:cprint(x, "green", "on_light_magenta",end="")
    # _y_olm = lambda x:cprint(x, "yellow", "on_light_magenta",end="")
    # _b_olm = lambda x:cprint(x, "blue", "on_light_magenta",end="")
    # _m_olm = lambda x:cprint(x, "magenta", "on_light_magenta",end="")
    # _c_olm = lambda x:cprint(x, "cyan", "on_light_magenta",end="")
    # _w_olm = lambda x:cprint(x, "white", "on_light_magenta",end="")
    # _lgr_olm = lambda x:cprint(x, "light_grey", "on_light_magenta",end="")
    # _dg_olm = lambda x:cprint(x, "dark_grey", "on_light_magenta",end="")
    # _lr_olm = lambda x:cprint(x, "light_red", "on_light_magenta",end="")
    # _lg_olm = lambda x:cprint(x, "light_green", "on_light_magenta",end="")
    # _ly_olm = lambda x:cprint(x, "light_yellow", "on_light_magenta",end="")
    # _lb_olm = lambda x:cprint(x, "light_blue", "on_light_magenta",end="")
    # _lm_olm = lambda x:cprint(x, "light_magenta", "on_light_magenta",end="")
    # _lc_olm = lambda x:cprint(x, "light_cyan", "on_light_magenta",end="")
    # _bk_olc = lambda x:cprint(x, "black", "on_light_cyan",end="")
    # _r_olc = lambda x:cprint(x, "red", "on_light_cyan",end="")
    # _g_olc = lambda x:cprint(x, "green", "on_light_cyan",end="")
    # _y_olc = lambda x:cprint(x, "yellow", "on_light_cyan",end="")
    # _b_olc = lambda x:cprint(x, "blue", "on_light_cyan",end="")
    # _m_olc = lambda x:cprint(x, "magenta", "on_light_cyan",end="")
    # _c_olc = lambda x:cprint(x, "cyan", "on_light_cyan",end="")
    # _w_olc = lambda x:cprint(x, "white", "on_light_cyan",end="")
    # _lgr_olc = lambda x:cprint(x, "light_grey", "on_light_cyan",end="")
    # _dg_olc = lambda x:cprint(x, "dark_grey", "on_light_cyan",end="")
    # _lr_olc = lambda x:cprint(x, "light_red", "on_light_cyan",end="")
    # _lg_olc = lambda x:cprint(x, "light_green", "on_light_cyan",end="")
    # _ly_olc = lambda x:cprint(x, "light_yellow", "on_light_cyan",end="")
    # _lb_olc = lambda x:cprint(x, "light_blue", "on_light_cyan",end="")
    # _lm_olc = lambda x:cprint(x, "light_magenta", "on_light_cyan",end="")
    # _lc_olc = lambda x:cprint(x, "light_cyan", "on_light_cyan",end="")
    
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
    def _bk_obk(s:object)->str:                                  # Black on On Black
        return cprint(str(s),'black','on_black')

    @staticmethod
    def _r_obk(s:object)->str:                                   # Red on On Black
        return cprint(str(s),'red','on_black')

    @staticmethod
    def _g_obk(s:object)->str:                                   # Green on On Black
        return cprint(str(s),'green','on_black')

    @staticmethod
    def _y_obk(s:object)->str:                                   # Yellow on On Black
        return cprint(str(s),'yellow','on_black')

    @staticmethod
    def _b_obk(s:object)->str:                                   # Blue on On Black
        return cprint(str(s),'blue','on_black')

    @staticmethod
    def _m_obk(s:object)->str:                                   # Magenta on On Black
        return cprint(str(s),'magenta','on_black')

    @staticmethod
    def _c_obk(s:object)->str:                                   # Cyan on On Black
        return cprint(str(s),'cyan','on_black')

    @staticmethod
    def _w_obk(s:object)->str:                                   # White on On Black
        return cprint(str(s),'white','on_black')

    @staticmethod
    def _lgr_obk(s:object)->str:                                 # Light Grey on On Black
        return cprint(str(s),'light_grey','on_black')

    @staticmethod
    def _dg_obk(s:object)->str:                                  # Dark Grey on On Black
        return cprint(str(s),'dark_grey','on_black')

    @staticmethod
    def _lr_obk(s:object)->str:                                  # Light Red on On Black
        return cprint(str(s),'light_red','on_black')

    @staticmethod
    def _lg_obk(s:object)->str:                                  # Light Green on On Black
        return cprint(str(s),'light_green','on_black')

    @staticmethod
    def _ly_obk(s:object)->str:                                  # Light Yellow on On Black
        return cprint(str(s),'light_yellow','on_black')

    @staticmethod
    def _lb_obk(s:object)->str:                                  # Light Blue on On Black
        return cprint(str(s),'light_blue','on_black')

    @staticmethod
    def _lm_obk(s:object)->str:                                  # Light Magenta on On Black
        return cprint(str(s),'light_magenta','on_black')

    @staticmethod
    def _lc_obk(s:object)->str:                                  # Light Cyan on On Black
        return cprint(str(s),'light_cyan','on_black')

    @staticmethod
    def _bk_or(s:object)->str:                                   # Black on On Red
        return cprint(str(s),'black','on_red')

    @staticmethod
    def _r_or(s:object)->str:                                    # Red on On Red
        return cprint(str(s),'red','on_red')

    @staticmethod
    def _g_or(s:object)->str:                                    # Green on On Red
        return cprint(str(s),'green','on_red')

    @staticmethod
    def _y_or(s:object)->str:                                    # Yellow on On Red
        return cprint(str(s),'yellow','on_red')

    @staticmethod
    def _b_or(s:object)->str:                                    # Blue on On Red
        return cprint(str(s),'blue','on_red')

    @staticmethod
    def _m_or(s:object)->str:                                    # Magenta on On Red
        return cprint(str(s),'magenta','on_red')

    @staticmethod
    def _c_or(s:object)->str:                                    # Cyan on On Red
        return cprint(str(s),'cyan','on_red')

    @staticmethod
    def _w_or(s:object)->str:                                    # White on On Red
        return cprint(str(s),'white','on_red')

    @staticmethod
    def _lgr_or(s:object)->str:                                  # Light Grey on On Red
        return cprint(str(s),'light_grey','on_red')

    @staticmethod
    def _dg_or(s:object)->str:                                   # Dark Grey on On Red
        return cprint(str(s),'dark_grey','on_red')

    @staticmethod
    def _lr_or(s:object)->str:                                   # Light Red on On Red
        return cprint(str(s),'light_red','on_red')

    @staticmethod
    def _lg_or(s:object)->str:                                   # Light Green on On Red
        return cprint(str(s),'light_green','on_red')

    @staticmethod
    def _ly_or(s:object)->str:                                   # Light Yellow on On Red
        return cprint(str(s),'light_yellow','on_red')

    @staticmethod
    def _lb_or(s:object)->str:                                   # Light Blue on On Red
        return cprint(str(s),'light_blue','on_red')

    @staticmethod
    def _lm_or(s:object)->str:                                   # Light Magenta on On Red
        return cprint(str(s),'light_magenta','on_red')

    @staticmethod
    def _lc_or(s:object)->str:                                   # Light Cyan on On Red
        return cprint(str(s),'light_cyan','on_red')

    @staticmethod
    def _bk_og(s:object)->str:                                   # Black on On Green
        return cprint(str(s),'black','on_green')

    @staticmethod
    def _r_og(s:object)->str:                                    # Red on On Green
        return cprint(str(s),'red','on_green')

    @staticmethod
    def _g_og(s:object)->str:                                    # Green on On Green
        return cprint(str(s),'green','on_green')

    @staticmethod
    def _y_og(s:object)->str:                                    # Yellow on On Green
        return cprint(str(s),'yellow','on_green')

    @staticmethod
    def _b_og(s:object)->str:                                    # Blue on On Green
        return cprint(str(s),'blue','on_green')

    @staticmethod
    def _m_og(s:object)->str:                                    # Magenta on On Green
        return cprint(str(s),'magenta','on_green')

    @staticmethod
    def _c_og(s:object)->str:                                    # Cyan on On Green
        return cprint(str(s),'cyan','on_green')

    @staticmethod
    def _w_og(s:object)->str:                                    # White on On Green
        return cprint(str(s),'white','on_green')

    @staticmethod
    def _lgr_og(s:object)->str:                                  # Light Grey on On Green
        return cprint(str(s),'light_grey','on_green')

    @staticmethod
    def _dg_og(s:object)->str:                                   # Dark Grey on On Green
        return cprint(str(s),'dark_grey','on_green')

    @staticmethod
    def _lr_og(s:object)->str:                                   # Light Red on On Green
        return cprint(str(s),'light_red','on_green')

    @staticmethod
    def _lg_og(s:object)->str:                                   # Light Green on On Green
        return cprint(str(s),'light_green','on_green')

    @staticmethod
    def _ly_og(s:object)->str:                                   # Light Yellow on On Green
        return cprint(str(s),'light_yellow','on_green')

    @staticmethod
    def _lb_og(s:object)->str:                                   # Light Blue on On Green
        return cprint(str(s),'light_blue','on_green')

    @staticmethod
    def _lm_og(s:object)->str:                                   # Light Magenta on On Green
        return cprint(str(s),'light_magenta','on_green')

    @staticmethod
    def _lc_og(s:object)->str:                                   # Light Cyan on On Green
        return cprint(str(s),'light_cyan','on_green')

    @staticmethod
    def _bk_oy(s:object)->str:                                   # Black on On Yellow
        return cprint(str(s),'black','on_yellow')

    @staticmethod
    def _r_oy(s:object)->str:                                    # Red on On Yellow
        return cprint(str(s),'red','on_yellow')

    @staticmethod
    def _g_oy(s:object)->str:                                    # Green on On Yellow
        return cprint(str(s),'green','on_yellow')

    @staticmethod
    def _y_oy(s:object)->str:                                    # Yellow on On Yellow
        return cprint(str(s),'yellow','on_yellow')

    @staticmethod
    def _b_oy(s:object)->str:                                    # Blue on On Yellow
        return cprint(str(s),'blue','on_yellow')

    @staticmethod
    def _m_oy(s:object)->str:                                    # Magenta on On Yellow
        return cprint(str(s),'magenta','on_yellow')

    @staticmethod
    def _c_oy(s:object)->str:                                    # Cyan on On Yellow
        return cprint(str(s),'cyan','on_yellow')

    @staticmethod
    def _w_oy(s:object)->str:                                    # White on On Yellow
        return cprint(str(s),'white','on_yellow')

    @staticmethod
    def _lgr_oy(s:object)->str:                                  # Light Grey on On Yellow
        return cprint(str(s),'light_grey','on_yellow')

    @staticmethod
    def _dg_oy(s:object)->str:                                   # Dark Grey on On Yellow
        return cprint(str(s),'dark_grey','on_yellow')

    @staticmethod
    def _lr_oy(s:object)->str:                                   # Light Red on On Yellow
        return cprint(str(s),'light_red','on_yellow')

    @staticmethod
    def _lg_oy(s:object)->str:                                   # Light Green on On Yellow
        return cprint(str(s),'light_green','on_yellow')

    @staticmethod
    def _ly_oy(s:object)->str:                                   # Light Yellow on On Yellow
        return cprint(str(s),'light_yellow','on_yellow')

    @staticmethod
    def _lb_oy(s:object)->str:                                   # Light Blue on On Yellow
        return cprint(str(s),'light_blue','on_yellow')

    @staticmethod
    def _lm_oy(s:object)->str:                                   # Light Magenta on On Yellow
        return cprint(str(s),'light_magenta','on_yellow')

    @staticmethod
    def _lc_oy(s:object)->str:                                   # Light Cyan on On Yellow
        return cprint(str(s),'light_cyan','on_yellow')

    @staticmethod
    def _bk_ob(s:object)->str:                                   # Black on On Blue
        return cprint(str(s),'black','on_blue')

    @staticmethod
    def _r_ob(s:object)->str:                                    # Red on On Blue
        return cprint(str(s),'red','on_blue')

    @staticmethod
    def _g_ob(s:object)->str:                                    # Green on On Blue
        return cprint(str(s),'green','on_blue')

    @staticmethod
    def _y_ob(s:object)->str:                                    # Yellow on On Blue
        return cprint(str(s),'yellow','on_blue')

    @staticmethod
    def _b_ob(s:object)->str:                                    # Blue on On Blue
        return cprint(str(s),'blue','on_blue')

    @staticmethod
    def _m_ob(s:object)->str:                                    # Magenta on On Blue
        return cprint(str(s),'magenta','on_blue')

    @staticmethod
    def _c_ob(s:object)->str:                                    # Cyan on On Blue
        return cprint(str(s),'cyan','on_blue')

    @staticmethod
    def _w_ob(s:object)->str:                                    # White on On Blue
        return cprint(str(s),'white','on_blue')

    @staticmethod
    def _lgr_ob(s:object)->str:                                  # Light Grey on On Blue
        return cprint(str(s),'light_grey','on_blue')

    @staticmethod
    def _dg_ob(s:object)->str:                                   # Dark Grey on On Blue
        return cprint(str(s),'dark_grey','on_blue')

    @staticmethod
    def _lr_ob(s:object)->str:                                   # Light Red on On Blue
        return cprint(str(s),'light_red','on_blue')

    @staticmethod
    def _lg_ob(s:object)->str:                                   # Light Green on On Blue
        return cprint(str(s),'light_green','on_blue')

    @staticmethod
    def _ly_ob(s:object)->str:                                   # Light Yellow on On Blue
        return cprint(str(s),'light_yellow','on_blue')

    @staticmethod
    def _lb_ob(s:object)->str:                                   # Light Blue on On Blue
        return cprint(str(s),'light_blue','on_blue')

    @staticmethod
    def _lm_ob(s:object)->str:                                   # Light Magenta on On Blue
        return cprint(str(s),'light_magenta','on_blue')

    @staticmethod
    def _lc_ob(s:object)->str:                                   # Light Cyan on On Blue
        return cprint(str(s),'light_cyan','on_blue')

    @staticmethod
    def _bk_om(s:object)->str:                                   # Black on On Magenta
        return cprint(str(s),'black','on_magenta')

    @staticmethod
    def _r_om(s:object)->str:                                    # Red on On Magenta
        return cprint(str(s),'red','on_magenta')

    @staticmethod
    def _g_om(s:object)->str:                                    # Green on On Magenta
        return cprint(str(s),'green','on_magenta')

    @staticmethod
    def _y_om(s:object)->str:                                    # Yellow on On Magenta
        return cprint(str(s),'yellow','on_magenta')

    @staticmethod
    def _b_om(s:object)->str:                                    # Blue on On Magenta
        return cprint(str(s),'blue','on_magenta')

    @staticmethod
    def _m_om(s:object)->str:                                    # Magenta on On Magenta
        return cprint(str(s),'magenta','on_magenta')

    @staticmethod
    def _c_om(s:object)->str:                                    # Cyan on On Magenta
        return cprint(str(s),'cyan','on_magenta')

    @staticmethod
    def _w_om(s:object)->str:                                    # White on On Magenta
        return cprint(str(s),'white','on_magenta')

    @staticmethod
    def _lgr_om(s:object)->str:                                  # Light Grey on On Magenta
        return cprint(str(s),'light_grey','on_magenta')

    @staticmethod
    def _dg_om(s:object)->str:                                   # Dark Grey on On Magenta
        return cprint(str(s),'dark_grey','on_magenta')

    @staticmethod
    def _lr_om(s:object)->str:                                   # Light Red on On Magenta
        return cprint(str(s),'light_red','on_magenta')

    @staticmethod
    def _lg_om(s:object)->str:                                   # Light Green on On Magenta
        return cprint(str(s),'light_green','on_magenta')

    @staticmethod
    def _ly_om(s:object)->str:                                   # Light Yellow on On Magenta
        return cprint(str(s),'light_yellow','on_magenta')

    @staticmethod
    def _lb_om(s:object)->str:                                   # Light Blue on On Magenta
        return cprint(str(s),'light_blue','on_magenta')

    @staticmethod
    def _lm_om(s:object)->str:                                   # Light Magenta on On Magenta
        return cprint(str(s),'light_magenta','on_magenta')

    @staticmethod
    def _lc_om(s:object)->str:                                   # Light Cyan on On Magenta
        return cprint(str(s),'light_cyan','on_magenta')

    @staticmethod
    def _bk_oc(s:object)->str:                                   # Black on On Cyan
        return cprint(str(s),'black','on_cyan')

    @staticmethod
    def _r_oc(s:object)->str:                                    # Red on On Cyan
        return cprint(str(s),'red','on_cyan')

    @staticmethod
    def _g_oc(s:object)->str:                                    # Green on On Cyan
        return cprint(str(s),'green','on_cyan')

    @staticmethod
    def _y_oc(s:object)->str:                                    # Yellow on On Cyan
        return cprint(str(s),'yellow','on_cyan')

    @staticmethod
    def _b_oc(s:object)->str:                                    # Blue on On Cyan
        return cprint(str(s),'blue','on_cyan')

    @staticmethod
    def _m_oc(s:object)->str:                                    # Magenta on On Cyan
        return cprint(str(s),'magenta','on_cyan')

    @staticmethod
    def _c_oc(s:object)->str:                                    # Cyan on On Cyan
        return cprint(str(s),'cyan','on_cyan')

    @staticmethod
    def _w_oc(s:object)->str:                                    # White on On Cyan
        return cprint(str(s),'white','on_cyan')

    @staticmethod
    def _lgr_oc(s:object)->str:                                  # Light Grey on On Cyan
        return cprint(str(s),'light_grey','on_cyan')

    @staticmethod
    def _dg_oc(s:object)->str:                                   # Dark Grey on On Cyan
        return cprint(str(s),'dark_grey','on_cyan')

    @staticmethod
    def _lr_oc(s:object)->str:                                   # Light Red on On Cyan
        return cprint(str(s),'light_red','on_cyan')

    @staticmethod
    def _lg_oc(s:object)->str:                                   # Light Green on On Cyan
        return cprint(str(s),'light_green','on_cyan')

    @staticmethod
    def _ly_oc(s:object)->str:                                   # Light Yellow on On Cyan
        return cprint(str(s),'light_yellow','on_cyan')

    @staticmethod
    def _lb_oc(s:object)->str:                                   # Light Blue on On Cyan
        return cprint(str(s),'light_blue','on_cyan')

    @staticmethod
    def _lm_oc(s:object)->str:                                   # Light Magenta on On Cyan
        return cprint(str(s),'light_magenta','on_cyan')

    @staticmethod
    def _lc_oc(s:object)->str:                                   # Light Cyan on On Cyan
        return cprint(str(s),'light_cyan','on_cyan')

    @staticmethod
    def _bk_ow(s:object)->str:                                   # Black on On White
        return cprint(str(s),'black','on_white')

    @staticmethod
    def _r_ow(s:object)->str:                                    # Red on On White
        return cprint(str(s),'red','on_white')

    @staticmethod
    def _g_ow(s:object)->str:                                    # Green on On White
        return cprint(str(s),'green','on_white')

    @staticmethod
    def _y_ow(s:object)->str:                                    # Yellow on On White
        return cprint(str(s),'yellow','on_white')

    @staticmethod
    def _b_ow(s:object)->str:                                    # Blue on On White
        return cprint(str(s),'blue','on_white')

    @staticmethod
    def _m_ow(s:object)->str:                                    # Magenta on On White
        return cprint(str(s),'magenta','on_white')

    @staticmethod
    def _c_ow(s:object)->str:                                    # Cyan on On White
        return cprint(str(s),'cyan','on_white')

    @staticmethod
    def _w_ow(s:object)->str:                                    # White on On White
        return cprint(str(s),'white','on_white')

    @staticmethod
    def _lgr_ow(s:object)->str:                                  # Light Grey on On White
        return cprint(str(s),'light_grey','on_white')

    @staticmethod
    def _dg_ow(s:object)->str:                                   # Dark Grey on On White
        return cprint(str(s),'dark_grey','on_white')

    @staticmethod
    def _lr_ow(s:object)->str:                                   # Light Red on On White
        return cprint(str(s),'light_red','on_white')

    @staticmethod
    def _lg_ow(s:object)->str:                                   # Light Green on On White
        return cprint(str(s),'light_green','on_white')

    @staticmethod
    def _ly_ow(s:object)->str:                                   # Light Yellow on On White
        return cprint(str(s),'light_yellow','on_white')

    @staticmethod
    def _lb_ow(s:object)->str:                                   # Light Blue on On White
        return cprint(str(s),'light_blue','on_white')

    @staticmethod
    def _lm_ow(s:object)->str:                                   # Light Magenta on On White
        return cprint(str(s),'light_magenta','on_white')

    @staticmethod
    def _lc_ow(s:object)->str:                                   # Light Cyan on On White
        return cprint(str(s),'light_cyan','on_white')

    @staticmethod
    def _bk_olgr(s:object)->str:                                 # Black on On Light Grey
        return cprint(str(s),'black','on_light_grey')

    @staticmethod
    def _r_olgr(s:object)->str:                                  # Red on On Light Grey
        return cprint(str(s),'red','on_light_grey')

    @staticmethod
    def _g_olgr(s:object)->str:                                  # Green on On Light Grey
        return cprint(str(s),'green','on_light_grey')

    @staticmethod
    def _y_olgr(s:object)->str:                                  # Yellow on On Light Grey
        return cprint(str(s),'yellow','on_light_grey')

    @staticmethod
    def _b_olgr(s:object)->str:                                  # Blue on On Light Grey
        return cprint(str(s),'blue','on_light_grey')

    @staticmethod
    def _m_olgr(s:object)->str:                                  # Magenta on On Light Grey
        return cprint(str(s),'magenta','on_light_grey')

    @staticmethod
    def _c_olgr(s:object)->str:                                  # Cyan on On Light Grey
        return cprint(str(s),'cyan','on_light_grey')

    @staticmethod
    def _w_olgr(s:object)->str:                                  # White on On Light Grey
        return cprint(str(s),'white','on_light_grey')

    @staticmethod
    def _lgr_olgr(s:object)->str:                                # Light Grey on On Light Grey
        return cprint(str(s),'light_grey','on_light_grey')

    @staticmethod
    def _dg_olgr(s:object)->str:                                 # Dark Grey on On Light Grey
        return cprint(str(s),'dark_grey','on_light_grey')

    @staticmethod
    def _lr_olgr(s:object)->str:                                 # Light Red on On Light Grey
        return cprint(str(s),'light_red','on_light_grey')

    @staticmethod
    def _lg_olgr(s:object)->str:                                 # Light Green on On Light Grey
        return cprint(str(s),'light_green','on_light_grey')

    @staticmethod
    def _ly_olgr(s:object)->str:                                 # Light Yellow on On Light Grey
        return cprint(str(s),'light_yellow','on_light_grey')

    @staticmethod
    def _lb_olgr(s:object)->str:                                 # Light Blue on On Light Grey
        return cprint(str(s),'light_blue','on_light_grey')

    @staticmethod
    def _lm_olgr(s:object)->str:                                 # Light Magenta on On Light Grey
        return cprint(str(s),'light_magenta','on_light_grey')

    @staticmethod
    def _lc_olgr(s:object)->str:                                 # Light Cyan on On Light Grey
        return cprint(str(s),'light_cyan','on_light_grey')

    @staticmethod
    def _bk_odg(s:object)->str:                                  # Black on On Dark Grey
        return cprint(str(s),'black','on_dark_grey')

    @staticmethod
    def _r_odg(s:object)->str:                                   # Red on On Dark Grey
        return cprint(str(s),'red','on_dark_grey')

    @staticmethod
    def _g_odg(s:object)->str:                                   # Green on On Dark Grey
        return cprint(str(s),'green','on_dark_grey')

    @staticmethod
    def _y_odg(s:object)->str:                                   # Yellow on On Dark Grey
        return cprint(str(s),'yellow','on_dark_grey')

    @staticmethod
    def _b_odg(s:object)->str:                                   # Blue on On Dark Grey
        return cprint(str(s),'blue','on_dark_grey')

    @staticmethod
    def _m_odg(s:object)->str:                                   # Magenta on On Dark Grey
        return cprint(str(s),'magenta','on_dark_grey')

    @staticmethod
    def _c_odg(s:object)->str:                                   # Cyan on On Dark Grey
        return cprint(str(s),'cyan','on_dark_grey')

    @staticmethod
    def _w_odg(s:object)->str:                                   # White on On Dark Grey
        return cprint(str(s),'white','on_dark_grey')

    @staticmethod
    def _lgr_odg(s:object)->str:                                 # Light Grey on On Dark Grey
        return cprint(str(s),'light_grey','on_dark_grey')

    @staticmethod
    def _dg_odg(s:object)->str:                                  # Dark Grey on On Dark Grey
        return cprint(str(s),'dark_grey','on_dark_grey')

    @staticmethod
    def _lr_odg(s:object)->str:                                  # Light Red on On Dark Grey
        return cprint(str(s),'light_red','on_dark_grey')

    @staticmethod
    def _lg_odg(s:object)->str:                                  # Light Green on On Dark Grey
        return cprint(str(s),'light_green','on_dark_grey')

    @staticmethod
    def _ly_odg(s:object)->str:                                  # Light Yellow on On Dark Grey
        return cprint(str(s),'light_yellow','on_dark_grey')

    @staticmethod
    def _lb_odg(s:object)->str:                                  # Light Blue on On Dark Grey
        return cprint(str(s),'light_blue','on_dark_grey')

    @staticmethod
    def _lm_odg(s:object)->str:                                  # Light Magenta on On Dark Grey
        return cprint(str(s),'light_magenta','on_dark_grey')

    @staticmethod
    def _lc_odg(s:object)->str:                                  # Light Cyan on On Dark Grey
        return cprint(str(s),'light_cyan','on_dark_grey')

    @staticmethod
    def _bk_olr(s:object)->str:                                  # Black on On Light Red
        return cprint(str(s),'black','on_light_red')

    @staticmethod
    def _r_olr(s:object)->str:                                   # Red on On Light Red
        return cprint(str(s),'red','on_light_red')

    @staticmethod
    def _g_olr(s:object)->str:                                   # Green on On Light Red
        return cprint(str(s),'green','on_light_red')

    @staticmethod
    def _y_olr(s:object)->str:                                   # Yellow on On Light Red
        return cprint(str(s),'yellow','on_light_red')

    @staticmethod
    def _b_olr(s:object)->str:                                   # Blue on On Light Red
        return cprint(str(s),'blue','on_light_red')

    @staticmethod
    def _m_olr(s:object)->str:                                   # Magenta on On Light Red
        return cprint(str(s),'magenta','on_light_red')

    @staticmethod
    def _c_olr(s:object)->str:                                   # Cyan on On Light Red
        return cprint(str(s),'cyan','on_light_red')

    @staticmethod
    def _w_olr(s:object)->str:                                   # White on On Light Red
        return cprint(str(s),'white','on_light_red')

    @staticmethod
    def _lgr_olr(s:object)->str:                                 # Light Grey on On Light Red
        return cprint(str(s),'light_grey','on_light_red')

    @staticmethod
    def _dg_olr(s:object)->str:                                  # Dark Grey on On Light Red
        return cprint(str(s),'dark_grey','on_light_red')

    @staticmethod
    def _lr_olr(s:object)->str:                                  # Light Red on On Light Red
        return cprint(str(s),'light_red','on_light_red')

    @staticmethod
    def _lg_olr(s:object)->str:                                  # Light Green on On Light Red
        return cprint(str(s),'light_green','on_light_red')

    @staticmethod
    def _ly_olr(s:object)->str:                                  # Light Yellow on On Light Red
        return cprint(str(s),'light_yellow','on_light_red')

    @staticmethod
    def _lb_olr(s:object)->str:                                  # Light Blue on On Light Red
        return cprint(str(s),'light_blue','on_light_red')

    @staticmethod
    def _lm_olr(s:object)->str:                                  # Light Magenta on On Light Red
        return cprint(str(s),'light_magenta','on_light_red')

    @staticmethod
    def _lc_olr(s:object)->str:                                  # Light Cyan on On Light Red
        return cprint(str(s),'light_cyan','on_light_red')

    @staticmethod
    def _bk_olg(s:object)->str:                                  # Black on On Light Green
        return cprint(str(s),'black','on_light_green')

    @staticmethod
    def _r_olg(s:object)->str:                                   # Red on On Light Green
        return cprint(str(s),'red','on_light_green')

    @staticmethod
    def _g_olg(s:object)->str:                                   # Green on On Light Green
        return cprint(str(s),'green','on_light_green')

    @staticmethod
    def _y_olg(s:object)->str:                                   # Yellow on On Light Green
        return cprint(str(s),'yellow','on_light_green')

    @staticmethod
    def _b_olg(s:object)->str:                                   # Blue on On Light Green
        return cprint(str(s),'blue','on_light_green')

    @staticmethod
    def _m_olg(s:object)->str:                                   # Magenta on On Light Green
        return cprint(str(s),'magenta','on_light_green')

    @staticmethod
    def _c_olg(s:object)->str:                                   # Cyan on On Light Green
        return cprint(str(s),'cyan','on_light_green')

    @staticmethod
    def _w_olg(s:object)->str:                                   # White on On Light Green
        return cprint(str(s),'white','on_light_green')

    @staticmethod
    def _lgr_olg(s:object)->str:                                 # Light Grey on On Light Green
        return cprint(str(s),'light_grey','on_light_green')

    @staticmethod
    def _dg_olg(s:object)->str:                                  # Dark Grey on On Light Green
        return cprint(str(s),'dark_grey','on_light_green')

    @staticmethod
    def _lr_olg(s:object)->str:                                  # Light Red on On Light Green
        return cprint(str(s),'light_red','on_light_green')

    @staticmethod
    def _lg_olg(s:object)->str:                                  # Light Green on On Light Green
        return cprint(str(s),'light_green','on_light_green')

    @staticmethod
    def _ly_olg(s:object)->str:                                  # Light Yellow on On Light Green
        return cprint(str(s),'light_yellow','on_light_green')

    @staticmethod
    def _lb_olg(s:object)->str:                                  # Light Blue on On Light Green
        return cprint(str(s),'light_blue','on_light_green')

    @staticmethod
    def _lm_olg(s:object)->str:                                  # Light Magenta on On Light Green
        return cprint(str(s),'light_magenta','on_light_green')

    @staticmethod
    def _lc_olg(s:object)->str:                                  # Light Cyan on On Light Green
        return cprint(str(s),'light_cyan','on_light_green')

    @staticmethod
    def _bk_oly(s:object)->str:                                  # Black on On Light Yellow
        return cprint(str(s),'black','on_light_yellow')

    @staticmethod
    def _r_oly(s:object)->str:                                   # Red on On Light Yellow
        return cprint(str(s),'red','on_light_yellow')

    @staticmethod
    def _g_oly(s:object)->str:                                   # Green on On Light Yellow
        return cprint(str(s),'green','on_light_yellow')

    @staticmethod
    def _y_oly(s:object)->str:                                   # Yellow on On Light Yellow
        return cprint(str(s),'yellow','on_light_yellow')

    @staticmethod
    def _b_oly(s:object)->str:                                   # Blue on On Light Yellow
        return cprint(str(s),'blue','on_light_yellow')

    @staticmethod
    def _m_oly(s:object)->str:                                   # Magenta on On Light Yellow
        return cprint(str(s),'magenta','on_light_yellow')

    @staticmethod
    def _c_oly(s:object)->str:                                   # Cyan on On Light Yellow
        return cprint(str(s),'cyan','on_light_yellow')

    @staticmethod
    def _w_oly(s:object)->str:                                   # White on On Light Yellow
        return cprint(str(s),'white','on_light_yellow')

    @staticmethod
    def _lgr_oly(s:object)->str:                                 # Light Grey on On Light Yellow
        return cprint(str(s),'light_grey','on_light_yellow')

    @staticmethod
    def _dg_oly(s:object)->str:                                  # Dark Grey on On Light Yellow
        return cprint(str(s),'dark_grey','on_light_yellow')

    @staticmethod
    def _lr_oly(s:object)->str:                                  # Light Red on On Light Yellow
        return cprint(str(s),'light_red','on_light_yellow')

    @staticmethod
    def _lg_oly(s:object)->str:                                  # Light Green on On Light Yellow
        return cprint(str(s),'light_green','on_light_yellow')

    @staticmethod
    def _ly_oly(s:object)->str:                                  # Light Yellow on On Light Yellow
        return cprint(str(s),'light_yellow','on_light_yellow')

    @staticmethod
    def _lb_oly(s:object)->str:                                  # Light Blue on On Light Yellow
        return cprint(str(s),'light_blue','on_light_yellow')

    @staticmethod
    def _lm_oly(s:object)->str:                                  # Light Magenta on On Light Yellow
        return cprint(str(s),'light_magenta','on_light_yellow')

    @staticmethod
    def _lc_oly(s:object)->str:                                  # Light Cyan on On Light Yellow
        return cprint(str(s),'light_cyan','on_light_yellow')

    @staticmethod
    def _bk_olb(s:object)->str:                                  # Black on On Light Blue
        return cprint(str(s),'black','on_light_blue')

    @staticmethod
    def _r_olb(s:object)->str:                                   # Red on On Light Blue
        return cprint(str(s),'red','on_light_blue')

    @staticmethod
    def _g_olb(s:object)->str:                                   # Green on On Light Blue
        return cprint(str(s),'green','on_light_blue')

    @staticmethod
    def _y_olb(s:object)->str:                                   # Yellow on On Light Blue
        return cprint(str(s),'yellow','on_light_blue')

    @staticmethod
    def _b_olb(s:object)->str:                                   # Blue on On Light Blue
        return cprint(str(s),'blue','on_light_blue')

    @staticmethod
    def _m_olb(s:object)->str:                                   # Magenta on On Light Blue
        return cprint(str(s),'magenta','on_light_blue')

    @staticmethod
    def _c_olb(s:object)->str:                                   # Cyan on On Light Blue
        return cprint(str(s),'cyan','on_light_blue')

    @staticmethod
    def _w_olb(s:object)->str:                                   # White on On Light Blue
        return cprint(str(s),'white','on_light_blue')

    @staticmethod
    def _lgr_olb(s:object)->str:                                 # Light Grey on On Light Blue
        return cprint(str(s),'light_grey','on_light_blue')

    @staticmethod
    def _dg_olb(s:object)->str:                                  # Dark Grey on On Light Blue
        return cprint(str(s),'dark_grey','on_light_blue')

    @staticmethod
    def _lr_olb(s:object)->str:                                  # Light Red on On Light Blue
        return cprint(str(s),'light_red','on_light_blue')

    @staticmethod
    def _lg_olb(s:object)->str:                                  # Light Green on On Light Blue
        return cprint(str(s),'light_green','on_light_blue')

    @staticmethod
    def _ly_olb(s:object)->str:                                  # Light Yellow on On Light Blue
        return cprint(str(s),'light_yellow','on_light_blue')

    @staticmethod
    def _lb_olb(s:object)->str:                                  # Light Blue on On Light Blue
        return cprint(str(s),'light_blue','on_light_blue')

    @staticmethod
    def _lm_olb(s:object)->str:                                  # Light Magenta on On Light Blue
        return cprint(str(s),'light_magenta','on_light_blue')

    @staticmethod
    def _lc_olb(s:object)->str:                                  # Light Cyan on On Light Blue
        return cprint(str(s),'light_cyan','on_light_blue')

    @staticmethod
    def _bk_olm(s:object)->str:                                  # Black on On Light Magenta
        return cprint(str(s),'black','on_light_magenta')

    @staticmethod
    def _r_olm(s:object)->str:                                   # Red on On Light Magenta
        return cprint(str(s),'red','on_light_magenta')

    @staticmethod
    def _g_olm(s:object)->str:                                   # Green on On Light Magenta
        return cprint(str(s),'green','on_light_magenta')

    @staticmethod
    def _y_olm(s:object)->str:                                   # Yellow on On Light Magenta
        return cprint(str(s),'yellow','on_light_magenta')

    @staticmethod
    def _b_olm(s:object)->str:                                   # Blue on On Light Magenta
        return cprint(str(s),'blue','on_light_magenta')

    @staticmethod
    def _m_olm(s:object)->str:                                   # Magenta on On Light Magenta
        return cprint(str(s),'magenta','on_light_magenta')

    @staticmethod
    def _c_olm(s:object)->str:                                   # Cyan on On Light Magenta
        return cprint(str(s),'cyan','on_light_magenta')

    @staticmethod
    def _w_olm(s:object)->str:                                   # White on On Light Magenta
        return cprint(str(s),'white','on_light_magenta')

    @staticmethod
    def _lgr_olm(s:object)->str:                                 # Light Grey on On Light Magenta
        return cprint(str(s),'light_grey','on_light_magenta')

    @staticmethod
    def _dg_olm(s:object)->str:                                  # Dark Grey on On Light Magenta
        return cprint(str(s),'dark_grey','on_light_magenta')

    @staticmethod
    def _lr_olm(s:object)->str:                                  # Light Red on On Light Magenta
        return cprint(str(s),'light_red','on_light_magenta')

    @staticmethod
    def _lg_olm(s:object)->str:                                  # Light Green on On Light Magenta
        return cprint(str(s),'light_green','on_light_magenta')

    @staticmethod
    def _ly_olm(s:object)->str:                                  # Light Yellow on On Light Magenta
        return cprint(str(s),'light_yellow','on_light_magenta')

    @staticmethod
    def _lb_olm(s:object)->str:                                  # Light Blue on On Light Magenta
        return cprint(str(s),'light_blue','on_light_magenta')

    @staticmethod
    def _lm_olm(s:object)->str:                                  # Light Magenta on On Light Magenta
        return cprint(str(s),'light_magenta','on_light_magenta')

    @staticmethod
    def _lc_olm(s:object)->str:                                  # Light Cyan on On Light Magenta
        return cprint(str(s),'light_cyan','on_light_magenta')

    @staticmethod
    def _bk_olc(s:object)->str:                                  # Black on On Light Cyan
        return cprint(str(s),'black','on_light_cyan')

    @staticmethod
    def _r_olc(s:object)->str:                                   # Red on On Light Cyan
        return cprint(str(s),'red','on_light_cyan')

    @staticmethod
    def _g_olc(s:object)->str:                                   # Green on On Light Cyan
        return cprint(str(s),'green','on_light_cyan')

    @staticmethod
    def _y_olc(s:object)->str:                                   # Yellow on On Light Cyan
        return cprint(str(s),'yellow','on_light_cyan')

    @staticmethod
    def _b_olc(s:object)->str:                                   # Blue on On Light Cyan
        return cprint(str(s),'blue','on_light_cyan')

    @staticmethod
    def _m_olc(s:object)->str:                                   # Magenta on On Light Cyan
        return cprint(str(s),'magenta','on_light_cyan')

    @staticmethod
    def _c_olc(s:object)->str:                                   # Cyan on On Light Cyan
        return cprint(str(s),'cyan','on_light_cyan')

    @staticmethod
    def _w_olc(s:object)->str:                                   # White on On Light Cyan
        return cprint(str(s),'white','on_light_cyan')

    @staticmethod
    def _lgr_olc(s:object)->str:                                 # Light Grey on On Light Cyan
        return cprint(str(s),'light_grey','on_light_cyan')

    @staticmethod
    def _dg_olc(s:object)->str:                                  # Dark Grey on On Light Cyan
        return cprint(str(s),'dark_grey','on_light_cyan')

    @staticmethod
    def _lr_olc(s:object)->str:                                  # Light Red on On Light Cyan
        return cprint(str(s),'light_red','on_light_cyan')

    @staticmethod
    def _lg_olc(s:object)->str:                                  # Light Green on On Light Cyan
        return cprint(str(s),'light_green','on_light_cyan')

    @staticmethod
    def _ly_olc(s:object)->str:                                  # Light Yellow on On Light Cyan
        return cprint(str(s),'light_yellow','on_light_cyan')

    @staticmethod
    def _lb_olc(s:object)->str:                                  # Light Blue on On Light Cyan
        return cprint(str(s),'light_blue','on_light_cyan')

    @staticmethod
    def _lm_olc(s:object)->str:                                  # Light Magenta on On Light Cyan
        return cprint(str(s),'light_magenta','on_light_cyan')

    @staticmethod
    def _lc_olc(s:object)->str:                                  # Light Cyan on On Light Cyan
        return cprint(str(s),'light_cyan','on_light_cyan')



    def __post_init__(self):
        self._bklf = tc._bklf
        self._bk = tc._bk
        self._r = tc._r
        self._g = tc._g
        self._y = tc._y
        self._b = tc._b
        self._m = tc._m
        self._c = tc._c
        self._w = tc._w
        self._lgr = tc._lgr
        self._dg = tc._dg
        self._lr = tc._lr
        self._lg = tc._lg
        self._ly = tc._ly
        self._lb = tc._lb
        self._lm = tc._lm
        self._lc = tc._lc
        self._bk_obk = tc._bk_obk
        self._r_obk = tc._r_obk
        self._g_obk = tc._g_obk
        self._y_obk = tc._y_obk
        self._b_obk = tc._b_obk
        self._m_obk = tc._m_obk
        self._c_obk = tc._c_obk
        self._w_obk = tc._w_obk
        self._lgr_obk = tc._lgr_obk
        self._dg_obk = tc._dg_obk
        self._lr_obk = tc._lr_obk
        self._lg_obk = tc._lg_obk
        self._ly_obk = tc._ly_obk
        self._lb_obk = tc._lb_obk
        self._lm_obk = tc._lm_obk
        self._lc_obk = tc._lc_obk
        self._bk_or = tc._bk_or
        self._r_or = tc._r_or
        self._g_or = tc._g_or
        self._y_or = tc._y_or
        self._b_or = tc._b_or
        self._m_or = tc._m_or
        self._c_or = tc._c_or
        self._w_or = tc._w_or
        self._lgr_or = tc._lgr_or
        self._dg_or = tc._dg_or
        self._lr_or = tc._lr_or
        self._lg_or = tc._lg_or
        self._ly_or = tc._ly_or
        self._lb_or = tc._lb_or
        self._lm_or = tc._lm_or
        self._lc_or = tc._lc_or
        self._bk_og = tc._bk_og
        self._r_og = tc._r_og
        self._g_og = tc._g_og
        self._y_og = tc._y_og
        self._b_og = tc._b_og
        self._m_og = tc._m_og
        self._c_og = tc._c_og
        self._w_og = tc._w_og
        self._lgr_og = tc._lgr_og
        self._dg_og = tc._dg_og
        self._lr_og = tc._lr_og
        self._lg_og = tc._lg_og
        self._ly_og = tc._ly_og
        self._lb_og = tc._lb_og
        self._lm_og = tc._lm_og
        self._lc_og = tc._lc_og
        self._bk_oy = tc._bk_oy
        self._r_oy = tc._r_oy
        self._g_oy = tc._g_oy
        self._y_oy = tc._y_oy
        self._b_oy = tc._b_oy
        self._m_oy = tc._m_oy
        self._c_oy = tc._c_oy
        self._w_oy = tc._w_oy
        self._lgr_oy = tc._lgr_oy
        self._dg_oy = tc._dg_oy
        self._lr_oy = tc._lr_oy
        self._lg_oy = tc._lg_oy
        self._ly_oy = tc._ly_oy
        self._lb_oy = tc._lb_oy
        self._lm_oy = tc._lm_oy
        self._lc_oy = tc._lc_oy
        self._bk_ob = tc._bk_ob
        self._r_ob = tc._r_ob
        self._g_ob = tc._g_ob
        self._y_ob = tc._y_ob
        self._b_ob = tc._b_ob
        self._m_ob = tc._m_ob
        self._c_ob = tc._c_ob
        self._w_ob = tc._w_ob
        self._lgr_ob = tc._lgr_ob
        self._dg_ob = tc._dg_ob
        self._lr_ob = tc._lr_ob
        self._lg_ob = tc._lg_ob
        self._ly_ob = tc._ly_ob
        self._lb_ob = tc._lb_ob
        self._lm_ob = tc._lm_ob
        self._lc_ob = tc._lc_ob
        self._bk_om = tc._bk_om
        self._r_om = tc._r_om
        self._g_om = tc._g_om
        self._y_om = tc._y_om
        self._b_om = tc._b_om
        self._m_om = tc._m_om
        self._c_om = tc._c_om
        self._w_om = tc._w_om
        self._lgr_om = tc._lgr_om
        self._dg_om = tc._dg_om
        self._lr_om = tc._lr_om
        self._lg_om = tc._lg_om
        self._ly_om = tc._ly_om
        self._lb_om = tc._lb_om
        self._lm_om = tc._lm_om
        self._lc_om = tc._lc_om
        self._bk_oc = tc._bk_oc
        self._r_oc = tc._r_oc
        self._g_oc = tc._g_oc
        self._y_oc = tc._y_oc
        self._b_oc = tc._b_oc
        self._m_oc = tc._m_oc
        self._c_oc = tc._c_oc
        self._w_oc = tc._w_oc
        self._lgr_oc = tc._lgr_oc
        self._dg_oc = tc._dg_oc
        self._lr_oc = tc._lr_oc
        self._lg_oc = tc._lg_oc
        self._ly_oc = tc._ly_oc
        self._lb_oc = tc._lb_oc
        self._lm_oc = tc._lm_oc
        self._lc_oc = tc._lc_oc
        self._bk_ow = tc._bk_ow
        self._r_ow = tc._r_ow
        self._g_ow = tc._g_ow
        self._y_ow = tc._y_ow
        self._b_ow = tc._b_ow
        self._m_ow = tc._m_ow
        self._c_ow = tc._c_ow
        self._w_ow = tc._w_ow
        self._lgr_ow = tc._lgr_ow
        self._dg_ow = tc._dg_ow
        self._lr_ow = tc._lr_ow
        self._lg_ow = tc._lg_ow
        self._ly_ow = tc._ly_ow
        self._lb_ow = tc._lb_ow
        self._lm_ow = tc._lm_ow
        self._lc_ow = tc._lc_ow
        self._bk_olgr = tc._bk_olgr
        self._r_olgr = tc._r_olgr
        self._g_olgr = tc._g_olgr
        self._y_olgr = tc._y_olgr
        self._b_olgr = tc._b_olgr
        self._m_olgr = tc._m_olgr
        self._c_olgr = tc._c_olgr
        self._w_olgr = tc._w_olgr
        self._lgr_olgr = tc._lgr_olgr
        self._dg_olgr = tc._dg_olgr
        self._lr_olgr = tc._lr_olgr
        self._lg_olgr = tc._lg_olgr
        self._ly_olgr = tc._ly_olgr
        self._lb_olgr = tc._lb_olgr
        self._lm_olgr = tc._lm_olgr
        self._lc_olgr = tc._lc_olgr
        self._bk_odg = tc._bk_odg
        self._r_odg = tc._r_odg
        self._g_odg = tc._g_odg
        self._y_odg = tc._y_odg
        self._b_odg = tc._b_odg
        self._m_odg = tc._m_odg
        self._c_odg = tc._c_odg
        self._w_odg = tc._w_odg
        self._lgr_odg = tc._lgr_odg
        self._dg_odg = tc._dg_odg
        self._lr_odg = tc._lr_odg
        self._lg_odg = tc._lg_odg
        self._ly_odg = tc._ly_odg
        self._lb_odg = tc._lb_odg
        self._lm_odg = tc._lm_odg
        self._lc_odg = tc._lc_odg
        self._bk_olr = tc._bk_olr
        self._r_olr = tc._r_olr
        self._g_olr = tc._g_olr
        self._y_olr = tc._y_olr
        self._b_olr = tc._b_olr
        self._m_olr = tc._m_olr
        self._c_olr = tc._c_olr
        self._w_olr = tc._w_olr
        self._lgr_olr = tc._lgr_olr
        self._dg_olr = tc._dg_olr
        self._lr_olr = tc._lr_olr
        self._lg_olr = tc._lg_olr
        self._ly_olr = tc._ly_olr
        self._lb_olr = tc._lb_olr
        self._lm_olr = tc._lm_olr
        self._lc_olr = tc._lc_olr
        self._bk_olg = tc._bk_olg
        self._r_olg = tc._r_olg
        self._g_olg = tc._g_olg
        self._y_olg = tc._y_olg
        self._b_olg = tc._b_olg
        self._m_olg = tc._m_olg
        self._c_olg = tc._c_olg
        self._w_olg = tc._w_olg
        self._lgr_olg = tc._lgr_olg
        self._dg_olg = tc._dg_olg
        self._lr_olg = tc._lr_olg
        self._lg_olg = tc._lg_olg
        self._ly_olg = tc._ly_olg
        self._lb_olg = tc._lb_olg
        self._lm_olg = tc._lm_olg
        self._lc_olg = tc._lc_olg
        self._bk_oly = tc._bk_oly
        self._r_oly = tc._r_oly
        self._g_oly = tc._g_oly
        self._y_oly = tc._y_oly
        self._b_oly = tc._b_oly
        self._m_oly = tc._m_oly
        self._c_oly = tc._c_oly
        self._w_oly = tc._w_oly
        self._lgr_oly = tc._lgr_oly
        self._dg_oly = tc._dg_oly
        self._lr_oly = tc._lr_oly
        self._lg_oly = tc._lg_oly
        self._ly_oly = tc._ly_oly
        self._lb_oly = tc._lb_oly
        self._lm_oly = tc._lm_oly
        self._lc_oly = tc._lc_oly
        self._bk_olb = tc._bk_olb
        self._r_olb = tc._r_olb
        self._g_olb = tc._g_olb
        self._y_olb = tc._y_olb
        self._b_olb = tc._b_olb
        self._m_olb = tc._m_olb
        self._c_olb = tc._c_olb
        self._w_olb = tc._w_olb
        self._lgr_olb = tc._lgr_olb
        self._dg_olb = tc._dg_olb
        self._lr_olb = tc._lr_olb
        self._lg_olb = tc._lg_olb
        self._ly_olb = tc._ly_olb
        self._lb_olb = tc._lb_olb
        self._lm_olb = tc._lm_olb
        self._lc_olb = tc._lc_olb
        self._bk_olm = tc._bk_olm
        self._r_olm = tc._r_olm
        self._g_olm = tc._g_olm
        self._y_olm = tc._y_olm
        self._b_olm = tc._b_olm
        self._m_olm = tc._m_olm
        self._c_olm = tc._c_olm
        self._w_olm = tc._w_olm
        self._lgr_olm = tc._lgr_olm
        self._dg_olm = tc._dg_olm
        self._lr_olm = tc._lr_olm
        self._lg_olm = tc._lg_olm
        self._ly_olm = tc._ly_olm
        self._lb_olm = tc._lb_olm
        self._lm_olm = tc._lm_olm
        self._lc_olm = tc._lc_olm
        self._bk_olc = tc._bk_olc
        self._r_olc = tc._r_olc
        self._g_olc = tc._g_olc
        self._y_olc = tc._y_olc
        self._b_olc = tc._b_olc
        self._m_olc = tc._m_olc
        self._c_olc = tc._c_olc
        self._w_olc = tc._w_olc
        self._lgr_olc = tc._lgr_olc
        self._dg_olc = tc._dg_olc
        self._lr_olc = tc._lr_olc
        self._lg_olc = tc._lg_olc
        self._ly_olc = tc._ly_olc
        self._lb_olc = tc._lb_olc
        self._lm_olc = tc._lm_olc
        self._lc_olc = tc._lc_olc
        super().__setattr__("attr_name", self)
