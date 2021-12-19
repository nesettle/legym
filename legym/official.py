__api__ = {
    "activities": {
        "url": "https://cpes.legym.cn/education/app/activity/getActivityList",
        "method": "post",
        "data": {"page": 1, "size": 10},
        "description": "Get outdoor activity list",
    },
    "limit": {
        "url": "https://cpes.legym.cn/running/app/getRunningLimit",
        "method": "post",
        "data": {"semesterId": None},
        "description": "Get upper limit of daily running mileage",
    },
    "login": {
        "url": "https://cpes.legym.cn/authorization/user/manage/login",
        "method": "post",
        "data": {"entrance": "1", "password": None, "userName": None},
        "description": "Log in Legym account",
    },
    "register": {
        "url": "https://cpes.legym.cn/education/app/activity/signUp",
        "method": "post",
        "data": {"activityId": None},
        "description": "Register certain activity",
    },
    "running": {
        "url": "https://cpes.legym.cn/running/app/uploadRunningDetails",
        "method": "post",
        "data": {
            "scoringType": 1,
            "semesterId": None,
            "signPoint": [],
            "startTime": None,
            "totalMileage": None,
            "totalPart": 0.0,
            "type": "自由跑",
            "uneffectiveReason": "",
            "avePace": None,
            "calorie": None,
            "effectiveMileage": None,
            "effectivePart": 1,
            "endTime": None,
            "gpsMileage": None,
            "limitationsGoalsSexInfoId": None,
            "paceNumber": None,
            "paceRange": None,
            "routineLine": [
                {"latitude": 30.756303201239845, "longitude": 103.93206457325871},
                {"latitude": 30.756346614671184, "longitude": 103.93206545656531},
                {"latitude": 30.756359404607583, "longitude": 103.93407893568614},
                {"latitude": 30.753229499261558, "longitude": 103.93407611144278},
            ],
        },
        "description": "Upload running data",
    },
    "semester": {
        "url": "https://cpes.legym.cn/education/semester/getCurrent",
        "method": "get",
        "data": {},
        "description": "Get current semester",
    },
    "sign": {
        "url": "https://cpes.legym.cn/education/activity/app/attainability/sign",
        "method": "put",
        "data": {
            "activityId": None,
            "times": "1",
            "pageType": "activity",
            "userId": None,
            "activityType": 0,
            "attainabilityType": 1,
        },
        "description": "Sign in certain activity",
    },
}
