# -*- coding=utf-8 -*-
import  time,os
 
#数据部分
title = []
for x in range(1,13):
    title[x-1] = "diff_ang(0)_|Etheta|(%s)"%x

series_name = [["path(8.5.step)_TM", "air_TM"],]

data_path = []
data_air = []

xaxis_name = ["theta", ]
xaxis_data = []
yaxis_name = ["E-filed(dB)", ]
 
class Template_mixin(object):
    """html报告"""
    HTML_TMPL = r"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>diff_ang(0)</title>
            <script src="https://cdn.bootcss.com/echarts/4.3.0-rc.2/echarts.min.js"></script>
            <script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.min.js"></script>
        </head>
        <body>
            %(div)s
            <script type="text/javascript">
                %(scripts)s
            </script>
        </body>
        </html>"""
    DIV = r"""
        <div id="%(id)s" style="width:800px;height:400px;"></div>
    """
    SCRIPTS = r"""
        var myChart_%(id)s = echarts.init(document.getElementById("%(id)s"), 'dark', {renderer: 'canvas'});
        var option_%(id)s = {
            "title": [
                {
                    "text": "diff_ang(0)_|Etheta|(16)",
                    "left": "center",
                    "top": "auto",
                    "textStyle": {
                        "fontSize": 18
                    },
                    "subtextStyle": {
                        "fontSize": 12
                    }
                }
            ],
            "toolbox": {
                "show": true,
                "orient": "vertical",
                "left": "95%",
                "top": "center",
                "feature": {
                    "saveAsImage": {
                        "show": true,
                        "title": "save as image"
                    },
                    "restore": {
                        "show": true,
                        "title": "restore"
                    },
                    "dataView": {
                        "show": true,
                        "title": "data view"
                    }
                }
            },
            "series_id": 6117306,
            "tooltip": {
                "trigger": "item",
                "triggerOn": "mousemove|click",
                "axisPointer": {
                    "type": "line"
                },
                "textStyle": {
                    "fontSize": 14
                },
                "backgroundColor": "rgba(50,50,50,0.7)",
                "borderColor": "#333",
                "borderWidth": 0
            },
        }
    """
    
 
if __name__ == '__main__':
    table_tr0 = ''
    table_tr1=""
    table_tr2=""

    numfail = 1
    numsucc = 9
    html = Template_mixin()
    
    #总表数据
    table_td = html.TABLE_TMPL_TOTAL % dict(version=VERSION_DICT['version'],radio=VERSION_DICT['radio'],runstarttime=VERSION_DICT['runstarttime'],runstoptime = VERSION_DICT['runstoptime'])
    table_tr0 += table_td

    #详情数据
    table_td_module=html.TABLE_TMPL_MODULE % dict(name="",module=case1["name"],casetotal=case1["total"],passtotal=case1["passnum"],status=case1["status"],)
    table_tr1 += table_td_module

    #表头总数
    total_str = '共 %s，通过 %s，失败 %s' % (numfail + numsucc, numsucc, numfail)
   
    #case数据
    table_td_case=html.TABLE_TMPL_CASE % dict(name="",module=case2["name"],casetotal=case2["total"],passtotal=case2["passnum"],status=case2["status"],)
    table_tr2 += table_td_case

    output=html.HTML_TMPL % dict(value = total_str,table_tr = table_tr0,table_tr2=table_tr1,table_tr3=table_tr2)

    # 生成html报告
    filename='{date}_TestReport.html'.format(date=time.strftime('%Y%m%d%H%M%S'))
 
    #获取report的路径
    dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report")
    print(dir)
    filename=os.path.join(dir,filename)
    print(filename)

    if not os.path.exists(dir):
        os.makedirs(dir)
 
    with open(filename, 'wb') as f:
        f.write(output.encode('utf8'))
