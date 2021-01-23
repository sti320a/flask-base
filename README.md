## データベースの初期化

初期化
> FLASK_APP=app.py flask db init

マイグレーションファイルの作成
> FLASK_APP=app.py flask db migrate

マイグレーションの実行
> FLASK_APP=app.py flask db upgrade

ダウングレード
> FLASK_APP=app.py flask db downgrade

