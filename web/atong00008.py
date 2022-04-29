import jsonpath


data = {
    "store": {
        "book": [
            {
                "category": "新闻学",
                "author": "张三",
                "title": "图书标题1",
                "price": 8.95
            },
            {
                "category": "金融学",
                "author": "李四",
                "title": "图书标题2",
                "price": 12.00
            },
            {
                "category": "计算机",
                "author": "王五",
                "title": "图书标题3",
                "isbn": "0-553-21311-3",
                "price": 9.99
            },
            {
                "category": "医学",
                "author": "赵六",
                "title": "图书标题4",
                "price": 22.99
            }
        ],
        "phone": {
            "color": "red",
            "price": 1999.00,
            "author": "孙七"
        },
        "author": "周八",
        "price": 1.00
    },
    "expensive": 10,
    "author": "吴九"
}


res1 = jsonpath.jsonpath(data, "$.store.book[*].author")
print("所有book的author：{}".format(res1))

res2 = jsonpath.jsonpath(data, "$.store..price")
print("store的所有price：{}".format(res2))

res3 = jsonpath.jsonpath(data, "$..book[0,3]")
print("book的第1个元素、第4个元素：{}".format(res3))

res4 = jsonpath.jsonpath(data, "$.store.book[?(@.price < 10)]")
print("book中所有price小于10的元素：{}".format(res4))

