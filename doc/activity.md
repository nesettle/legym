# Legym Activity

`LegymActivity` is the minimum operating unit for activity on Legym app.

- [Legym Activity](#legym-activity)
  - [1. Create LegymActivity object](#1-create-legymactivity-object)
  - [2. View activity info](#2-view-activity-info)

## 1. Create LegymActivity object

Like `LegymActivities`, it is bothering to manually create an instance of `LegymActivity`. And there is no direct API to get a `LegymActivity` instance, which is different from `LegymActivities`.

While it cannot be initialized, you can still get its instance(s) from `LegymActivities().search()`, which will return a list of instances of `LegymActivity`.

```Python
>>> import legym

>>> mrcai = legym.login('username', 'password')

>>> mrcai.get_activities()[0]
<Legym Activity id='xxxxxx' name='xxxx' state='blocked'>
```

## 2. View activity info

`LegymActivity` provides no API to call, but we set 4 read-only properties.

1. ID:

```Python
>>> activity.id
'8a9781c97d75b704017d7a727d1a1d8a'
```

2. Code

```Python
>>> activity.code
'1d8a'
```

3. Name

```Python
>>> activity.name
'第三空间清水河校区综训馆'
```

4. State

```Python
>>> activity.state
legym.activity.ActivityState.signed
```