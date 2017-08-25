# -*- coding: utf-8 -*- 
from control import *
import numpy as np

class MouseConfig:
    def __init__(self):
        self.R = 5.0; # 抵抗 [ohm]
        self.KE = 7.1504e-04; # 逆起電力定数[V/(rad/s)]
        self.KT = 6.5e-04; # トルク定数[Nm/I]
        self.Vbat = 4.0; # モータドライバの電源電圧[V]

        # 機体パラメータ
        self.Ng = 3.0;          # ギアの減速比(モーター：ホイール=1:n), スライドバーで設定
        self.r = 7.5e-03;    # タイヤ半径[m]
        self.m = 75e-03;     # 機体重量[kg], スライドバーで設定
        self.w = 30e-03;     # 機体の中心から右端までの距離(横幅/2) [m]
        self.h = 45e-03;     # 機体の中心から先端までの距離(縦幅/2) [m]
        self.J = 1/3*(self.w**2+self.h**2)*self.m; # 機体の慣性モーメント(形状を長方形に近似)


class MouseDynamics:
    """
    Body and Motor Model (Transrational)
    -
    Input: 
        * duty :Duty ratio of the voltage input to the motor
    Output:
        * x: Position
        * v: Speed (Forward +)
        * phi: motor rotation [in radian]
        
    """
    
    def __init__(self, config=-1):  # コンストラクタ
        if config == -1:
            # 回路定数 (MK06-4.5の場合)
            self.R = 5.0; # ohm
            self.KE = 7.1504e-04; # 逆起電力定数[V/(rad/s)]
            self.KT = 6.5e-04; # トルク定数[Nm/I]
            self.Vbat = 4.0; # モータドライバの電源電圧[V]

            # 機体パラメータ
            self.Ng = 3.0;          # ギアの減速比(モーター：ホイール=1:n), スライドバーで設定
            self.r = 7.5e-03;    # タイヤ半径[m]
            self.m = 75e-03;     # 機体重量[kg], スライドバーで設定
            self.w = 30e-03;     # 機体の中心から右端までの距離(横幅/2) [m]
            self.h = 45e-03;     # 機体の中心から先端までの距離(縦幅/2) [m]
            self.J = 1/3*(self.w**2+self.h**2)*self.m; # 機体の慣性モーメント(形状を長方形に近似)
        else:
            self.R = config.R; # ohm
            self.KE = config.KE; # 逆起電力定数[V/(rad/s)]
            self.KT = config.KT; # トルク定数[Nm/I]
            self.Vbat = config.Vbat; # モータドライバの電源電圧[V]
            self.Ng = config.Ng;          # ギアの減速比(モーター：ホイール=1:n), スライドバーで設定
            self.r = config.r;     # タイヤ半径[m]
            self.m = config.m;     # 機体重量[kg], スライドバーで設定
            self.w = config.w;     # 機体の中心から右端までの距離(横幅/2) [m]
            self.h = config.h;     # 機体の中心から先端までの距離(縦幅/2) [m]
            self.J = config.J;     # 機体の慣性モーメント(形状を長方形に近似)        

        self._ismodified = False # モデル再計算フラグ
        # state space model
        a = -(self.KT*self.KE*self.Ng**2)/(self.R*self.m*self.r**2)
        b = (2*self.Vbat) * (self.KT*self.Ng)/(self.m*self.r*self.R) # Vm = (2*motor_duty*Vbat)*u と置いた
        c = 1/(self.Ng*self.r)
        A = np.array([ [0,1,0], [0,a,0], [0,c,0]]) 
        B = np.array([[0], [b], [0]])
        C = np.array([[1,0,0],[0,1,0],[0,0,1]])
        D = np.array([[0],[0],[0]])
        self.sys = StateSpace(A, B, C, D)
        
    def set_config(config):
        self.R = config.R; # ohm
        self.KE = config.KE; # 逆起電力定数[V/(rad/s)]
        self.KT = config.KT; # トルク定数[Nm/I]
        self.Vbat = config.Vbat; # モータドライバの電源電圧[V]
        self.Ng = config.Ng;          # ギアの減速比(モーター：ホイール=1:n), スライドバーで設定
        self.r = config.r;     # タイヤ半径[m]
        self.m = config.m;     # 機体重量[kg], スライドバーで設定
        self.w = config.w;     # 機体の中心から右端までの距離(横幅/2) [m]
        self.h = config.h;     # 機体の中心から先端までの距離(縦幅/2) [m]
        self.J = config.J;     # 機体の慣性モーメント(形状を長方形に近似)        
        self._ismodified = True
        
    @property
    def ss(self):
        if self._ismodified: # パラメータに変更があればモデルを再計算
            # state space model
            a = -(self.KT*self.KE*self.Ng**2)/(self.R*self.m*self.r**2)
            b = (2*self.Vbat) * (self.KT*self.Ng)/(self.m*self.r*self.R) # Vm = (2*Vbat)*u と置いた
            c = 1/(self.Ng*self.r)
            A = np.array([ [0,1,0], [0,a,0], [0,c,0]]) 
            B = np.array([[0], [b], [0]])
            C = np.array([[1,0,0],[0,1,0],[0,0,1]])
            D = np.array([[0],[0],[0]])
            self.sys = StateSpace(A, B, C, D)
            self._ismodified = False

        return self.sys

    
if __name__ == "__main__": 
    # インスタンスの生成
    config = MouseConfig()

    config.R = 5.0; # 抵抗 [ohm]
    config.KE = 7.1504e-04; # 逆起電力定数[V/(rad/s)]
    config.KT = 6.5e-04; # トルク定数[Nm/I]
    config.Vbat = 4.0; # モータドライバの電源電圧[V]
    config.Ng = 3.0;          # ギアの減速比(モーター：ホイール=1:n), スライドバーで設定
    config.r = 7.5e-03;    # タイヤ半径[m]
    config.m = 50e-03;     # 機体重量[kg], スライドバーで設定
    config.w = 30e-03;     # 機体の中心から右端までの距離(横幅/2) [m]
    config.h = 45e-03;     # 機体の中心から先端までの距離(縦幅/2) [m]
    config.J = 1/3*(config.w**2+config.h**2)*config.m; # 機体の慣性モーメント(形状を長方形に近似)
    mouse = MouseDynamics(config)

    print(mouse.ss)