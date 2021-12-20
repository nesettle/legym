# Legym Activities

`LegymActivities` acts as a manager of activities on Legym App.

- [Legym Activities](#legym-activities)
  - [1. Create LegymActivities object](#1-create-legymactivities-object)
  - [2. Search with given rules](#2-search-with-given-rules)

## 1. Create LegymActivities object

Instances of this class cannot be created manually, unless you captured packets of Legym App, find key `items`, and manually pass it in.

But you can get an instance after you create a `LegymUser` object, and call method `get_activities()`. (see doc [here](https://github.com/MrCaiDev/legym/blob/master/legym/README.md/#3-get-activity-list))

```Python
>>> import legym

>>> mrcai = legym.login('username', 'password')

>>> activities = mrcai.get_activities()

>>> activities
<Legym Activity id='xxxxxx' name='xxxx' state='blocked'>
<Legym Activity id='xxxxxx' name='xxxx' state='available'>
<Legym Activity id='xxxxxx' name='xxxx' state='registered'>
<Legym Activity id='xxxxxx' name='xxxx' state='signed'>
...
```

## 2. Search with given rules

Method `search()` is the only accessible API of `LegymActivities` instances. You can specify your own rules to filter activities. In this document we will take activities below as example:

|                ID                | Code  |           Name           |   State    |
| :------------------------------: | :---: | :----------------------: | :--------: |
| 8a9781c97d75b704017d7a727d1a1d8b | 1d8b  | 第三空间清水河校区综训馆 |  blocked   |
| 8a9781c97d75b704017d7a727d1f1dc6 | 1dc6  |  第三空间海南校区运动场  | available  |
| 20ee7c461ac244feaffc5c3dfa5ab297 | b297  |     嘉年华-特殊学院      | available  |
| 6e523f88883544878a777100220c3a8f | 3a8f  |  第三空间-周四-海南校区  | registered |
| 8a9781c97d75b704017d7a727d1a1d8a | 1d8a  | 第三空间清水河校区综训馆 |   signed   |

As you can see, code is just the last four characters of ID. Here are some examples of searching:

```Python
>>> activities.search(id='8a9781c97d75b704017d7a727d1a1d8a')
[<Legym Activity id='8a9781c97d75b704017d7a727d1a1d8a' name='第三空间清水河校区综训馆' state='signed'>]
>>> activities.search(name='综训馆')
[<Legym Activity id='8a9781c97d75b704017d7a727d1a1d8b' name='第三空间清水河校区综训馆' state='blocked'>, <Legym Activity id='8a9781c97d75b704017d7a727d1a1d8a' name='第三空间清水河校区综训馆' state='signed'>]
>>> activities.search(name='综训馆', state=legym.activity.ActivityState.signed)
[<Legym Activity id='8a9781c97d75b704017d7a727d1a1d8a' name='第三空间清水河校区综训馆' state='signed'>]
```

For the first example, we attempts to search for activity whose ID equals "8a9781c97d75b704017d7a727d1a1d8a". The result will be returned as a list, even if it has only one element.

For the second example, we attempts to search for activity whose name contains "综训馆". Yes, we are ok with abbreviation, as long as it is a substring of full name.

For the third example, we specifies both name and state at the same time, indicating you can apply several rules to personalize your searching.