<!--
 * @Description: 
 * @Version: 1.0
 * @Author: Zhang AO
 * @studentID: 518021910368
 * @School: SJTU
 * @Date: 2022-04-29 01:02:56
 * @LastEditors: Seven
 * @LastEditTime: 2022-06-12 02:20:16
-->
 - trialList[]参数中的值需要重新定义
 - 创建returnValue
 - returnValue.practice_record.append(ex_resp.corr)
 - delete logging
 - 
 - core.quit()注释掉 => return returnValue
 - --------------------------------------------
    # Store info about the experiment session
    expInfo = {}
    expInfo['admin']=admin
    expInfo['participant']=participant
    expInfo['session']=session
    expName="flanker"
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    print(expInfo['date'])
    
    returnValue=flankerResponse([],[],)

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data/XXX/%s/%s/%s/%s' % (admin,participant,group,session)

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        savePickle=False, saveWideText=True,
        originPath='./',
        dataFileName=filename)

----------------------------------------------
 - savePickle=False

 - 反应时是.rt

 - 删除    
    thisExp.saveAsPickle(filename)
    logging.flush()


- fullscr=False 


- two back 结果显示问题

-----------------------------------
Flanker：flanker_practice_resp.corr                                           

心理旋转：key_resp_2.corr

more-odd shifting：odd_practice_resp.corr
posner：this_resp.corr
stop signal：stop_resp.corr
stroop：key_resp.corr
go no go：key_stim_2.corr

ANT和2 back统计的是反应的按键 这个后面我在研究一下


_thisDir="."