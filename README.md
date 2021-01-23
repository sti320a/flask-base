## 概要
Flaskで開発するときに初期設定が面倒なので、基本的な準備を済ませた再利用のためのリポジトリです。

## 使い方
- 他人の場合: Forkして使ってください。
- 作者の場合: GitHub右上の＋ボタンから「Import repository」-> URL: https://github.com/sti320a/flask-base -> 「Repository Name」を入力 -> 「Begin Import」

## データベースの初期化

Flask-Migrateを使います。

初期化
> FLASK_APP=app.py flask db init

マイグレーションファイルの作成
> FLASK_APP=app.py flask db migrate

マイグレーションの実行
> FLASK_APP=app.py flask db upgrade

ダウングレード
> FLASK_APP=app.py flask db downgrade

