# mock-enemaru-api
## 初期設定
```
python -m venv .venv
.venv\Scripts\activate
pip install -r .\requirements.txt
```
## 起動
```
.venv\Scripts\activate # まだ仮想環境に入っていない場合に実行
uvicorn main:app --reload --port 3000
```
http://localhost:3000/ でアクセスできる