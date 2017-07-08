# control_notebook
micromouse simulation using jupyter and python-control

## 依存環境
* python 2.7/ 3.4
    * jupyter
    * control
    * slycot
    * sympy
    * matplotlib
    

## インストール
### すでにPythonが入ってる場合，
* pipを使えるようにしておく
* macの場合，slycotをインストールする前に，brew install gcc しておく
* pipでjupyter, control, sympy, ipywidget, slycot をインストール

### Pythonをまだインストールしてない場合

anacondaをインストールすると，pythonの他にjupyterやpipいったツールが一緒に入ってくれるので，おすすめです．


## 設定
ipywidgetを有効化するために，一回だけ下記のコマンドを実行する必要がある．

jupyter nbextension enable --py widgetsnbextension

## 実行
jupyter notebook を端末で実行すると，ブラウザが開く．

notebookは*.ipynbの拡張子のファイルなので，これを開いたら，
Run Cell All で実行できる．
