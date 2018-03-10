# APIリファレンス

## Books

全ての貸出記録を表します．

- title
  - 本のタイトル
  - Example: `"松浦さよ姫伝説の基礎的研究 近・現代編"`
  - Type: string
- borrower
  - 借りた人
  - Example: `"田中 太郎"`
  - Type: string
- borrowed_date
  - 借りた日
  - オプション
  - Example: `"2018-03-16"`
  - Type: string
  - Format: `%Y-%m-%d`

### GET /books

全ての貸出記録を取得します．

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

### POST /books

1つの貸出記録を登録します．

-   title
    -   本のタイトル
    -   Example: `"松浦さよ姫伝説の基礎的研究 近・現代編"`
    -   Type: string
-   borrower
    -   借りた人
    -   Example: `"田中 太郎"`
    -   Type: string
-   borrowed_date
    -   借りた日（オプション）
    -   Example: `"2018-03-16"`
    -   Type: string
    -   Format: `%Y-%m-%d`

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

## Book

１つの貸出記録を表します．

## Returning

1つの貸出記録に対して，本を返却することを表します．

### PUT /books/:book_id/returning
本を返却します．

```
PUT /books/:book_id/returning HTTP/1.1
```

```
HTTP/1.0 204
```

