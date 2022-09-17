'''
Description: 
Version: 1.0
Author: Zhang AO
studentID: 518021910368
School: SJTU
Date: 2022-09-16 01:26:33
LastEditors: Seven
LastEditTime: 2022-09-17 20:15:58
'''
from flask import Flask,request
from flanker import flanker


#创建Flask的实例对象
app = Flask(__name__)

def packRes(res={}):
    res_dist={
        "practice_record":res.practice_record,
        "practice_accurate":res.getPracticeAccurate(),
        "ex_record":res.ex_record,
        "ex_accurate":res.getExAccurate(),
    }
    return res_dist

@app.route('/flanker',methods=['GET'])
def flanker():
    args=request.args
    admin=args['admin']
    participant=args['participant']
    session=args['session']
    res=flanker(admin=admin,participant=participant,session=session)
    return packRes(res=res)
    
    


if __name__ == '__main__':
    app.run(port=7777,debug=True)