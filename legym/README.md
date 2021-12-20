# Legym API

## Creating LegymUser object

`LegymUser` is the basic operating unit of legym module, i.e. everything this module can do is based on this type of object. It represents a user who is using Legym App.

There are two ways to create a `LegymUser` instance:

Via API:

```Python
>>> import legym

>>> mrcai = legym.login('username', 'password')

>>> mrcai
<Legym User Yuwang Cai>
```

Via creating instance:

```Python
>>> import legym

>>> mrcai = legym.LegymUser('username', 'password')

>>> mrcai
<Legym User Yuwang Cai>
```

Both of these will return a `LegymUser` instance, which has a list of methods to call.

## View user info

Once we create a `LegymUser` instance, we can view his basic information.

Legym now supports 4 types of user info:

1. Real name:

```Python
>>> mrcai.real_name
'Yuwang Cai'
```

2. Nick name on Legym App:

```Python
>>> mrcai.nick_name
'MrCai'
```

3. School name:

```Python
>>> mrcai.school
'电子科技大学'
```

4. Organization name:

```Python
>>> mrcai.organization
'信息与通信工程学院'
```

## Get activity list

Method `get_activities()` can issue a request to Legym official API, and return current activities, which are exactly those the user can see on his Legym App.

```Python
>>> mrcai.get_activities()
<Legym Activity id='xxxxxx' name='xxxx' state='blocked'>
<Legym Activity id='xxxxxx' name='xxxx' state='available'>
<Legym Activity id='xxxxxx' name='xxxx' state='registered'>
<Legym Activity id='xxxxxx' name='xxxx' state='signed'>
...
```

For more details about `LegymActivities` object, read doc [here](https://www.bilibili.com/video/BV1ER4y1E7qn). (not written yet, coming soon 🥰)

## Register activity

Method `register()` can register an activity for user.

> This method currently only supports specifying activity by name. In later versions we will add more APIs like `register_by_id()`, `register_by_code()`, etc.

```Python
>>> mrcai.register('清水河校区综训馆')
('清水河校区综训馆', True, '报名成功')
>>> mrcai.register()
('清水河校区体育馆', True, '报名成功')
>>> mrcai.register('一个不存在的活动')
------------------------------------------
LegymException Trackback (most recent call last)
...
LegymException: 活动当前不可报名：一个不存在的活动
```

In the first example shown above, the user attempts to register activity "清水河校区综训馆". On success, method returns a tuple of 3 elements, the meaning of which can be looked up in docstring of `register()`, or hovers in IDEs like Visual Studio Code or Pycharm.

In the second example shown above, the user does not specify activity name: this is also allowed, in which case we will register the first available activity for him.

In the third example shown above, the user specifies an incorrect activity name. This will cause the program to throw a `LegymException`. Developers can catch and decide how to tackle it in their own codes.

> Actually I think returning a tuple like ('', False, '不存在该活动') might be a better solution. We will consider adding it in later versions.

## Sign in activity

Method `sign()` can sign in each activity registered by the user.

```Python
>>> mrcai.sign()
(('清水河校区综训馆', True, '成功'), ('清水河校区体育场', True, '成功'))
```

In last chapter the user registered two activities, and now he signs in both activities at a time.

`LegymException` will be caught inside this method, so don't worry about tackling this exception in your own code.

## Upload running data

Method `running()` can upload running data for the user.

```Python
>>> mrcai.running("0.1")
(0.1, True)
>>> mrcai.running(1.5)
(1.5, True)
>>> mrcai.running()
(3.5, True)
```

As is shown in the first and second example, you can specify the running distance either with `str` or `float`.

> `int` is also a reasonable type, as you would assume. Even your self-defined object can be passed in, as long as it can be converted to `float` type with Python built-in method `float()`.

Distance parameter is optional, as is shown in the third example, in which case the upper limit of effective mileage will be uploaded.

> This upper limit is relevant with current semester, not necessarily 3.5 km.
