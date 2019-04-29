## 接口返回值

-----

### status
- 第一个数字表示功能模块
- 第二个数字表示具体功能
- 第三个数字表示返回结果

### 0-权限不足
- 只有一个数字，表示因为token错误引起的权限错误

### 1-用户模块
> 1-注册功能
>>- 1：提交过程中数据丢失
>>- 2：注册成功
>>- 3：用户已经存在
>>- 4: 未知错误

> 2-登录功能
>>- 1：提交过程中数据丢失
>>- 2：登陆成功
>>- 3：用户名或者密码错误

### 2-书架模块
> 1-添加书籍
>>- 1：提交过程中数据丢失
>>- 2：添加成功

> 2-移除书籍
>>- 1：提交过程中数据丢失
>>- 2：删除成功
>>- 3：未找到该书，客户端书籍提交错误或数据库错误

> 3-获取用户书籍列表
>>- 1：保留
>>- 2：成功返回用户书架数据

### 3-书签模块
> 1-添加书签
>>- 1：提交过程中数据丢失
>>- 2：添加成功
>>- 3：数据错误，未找到该书籍

> 2-删除书签
>>- 1：提交过程中数据丢失
>>- 2：成功删除书签
>>- 3：数据错误，未找到该书签

> 3-获取用户下所有书签
>>- 1：保留
>>- 2：成功返回用户书签列表

### 4-评论模块
> 1-添加评论
>>- 1：提交过程中数据丢失
>>- 2：添加成功
>>- 3：数据错误，未找到该书籍

> 2-删除评论
>>- 1：提交过程中数据丢失
>>- 2：成功删除评论
>>- 3：数据错误，未找到该评论

> 3-获取用户评论
>>- 1：保留
>>- 2：成功获取用户评论列表

> 4-获取书籍评论
>>- 1：提交过程中数据丢失
>>- 2：成功获取书籍评论列表
>>- 3：数据错误，未找到书籍