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
### 必要なもの
* pipを使えるようにしておく
* macの場合，slycotをインストールする前に，brew install gcc しておく
* pipでjupyter, control, sympy, ipywidgets, slycot をインストール



### windows環境でインストール(anacondaを使う場合)

1. [anaconda](https://www.anaconda.com/download/)をインストール(python3.6でテスト)
2. 必要なpythonライブラリをインストール
3. pip でslycotをインストールしようとすると，エラーになるので[インストールバイナリ](http://www.lfd.uci.edu/~gohlke/pythonlibs/#slycot)をダウンロード
4. whlファイルを保存した場所に移動して，`pip install <ファイル名>`

## 設定
ipywidgetを有効化するために，一回だけ下記のコマンドを実行する必要がある．

    jupyter nbextension enable --py widgetsnbextension

## 実行
`jupyter notebook` を端末で実行すると，ブラウザが開く．

notebookは*.ipynbの拡張子のファイルなので，これを開いたら，
`Run Cell All` で実行できる．
