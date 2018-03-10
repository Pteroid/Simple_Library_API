# 簡易図書館API

簡易図書館APIはいつ誰がどの本を借りていつ返したかを管理するAPIサーバーを提供します．

Webアプリケーションフレームワークに[Falcon](https://falconframework.org/)を，データベースに[TinyDB](https://tinydb.readthedocs.io/en/latest/)を用いています．

## 使い方

エンドポイントにJSONをPOSTすることで，貸出記録に対してCRUDできます．

### 全ての貸出記録を取得

```
GET /books HTTP/1.1
```

```
HTTP1.1 200
Content-type: application/json

[
	{
		"borrower": "田中 太郎",
		"borrowed_date": "2017-01-12",
		"id": 1,
		"returned_date": "2017-01-24",
		"title": "松浦さよ姫伝説の基礎的研究 近・現代編"
	},
	{
		"borrower": "山田 花子",
		"borrowed_date": "2018-03-11",
		"id": 5,
		"title": "実践Python3",
		"returned_date": "2018-03-11"
	}
]
```

### 1つの貸出記録を追加

```
POST /books HTTP/1.1
Content-Type: application/json

{
	"borrower": "山田 花子",
	"title": "実践Python3"
}
```

```
HTTP/1.0 201
content-type: application/json

{
	"borrower": "山田 花子",
	"borrowed_date": "2018-03-11",
	"id": 6,
	"title": "実践Python3"
}
```

### 1つの貸出記録を返却済みにする

```
PUT /books/:book_id/returning
```

## 参考

-   [Qiita API v2 documentation](https://qiita.com/api/v2/docs)
-   [Falcon Documentation](https://falcon.readthedocs.io/en/stable/index.html)
-   [TinyDB Documentation](http://tinydb.readthedocs.io/en/latest/index.html)

