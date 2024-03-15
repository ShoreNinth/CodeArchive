/**
 * 
 */
// 基于准备好的dom，初始化echarts实例
      var myChartleft1 = echarts.init(document.getElementById("left1"),"dark");
      optionleft1 = {
    		  xAxis: {
    		    type: 'category',
    		    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    		  },
    		  yAxis: {
    		    type: 'value'
    		  },
    		  series: [
    		    {
    		      data: [820, 932, 901, 934, 1290, 1330, 1320],
    		      type: 'line',
    		      smooth: true
    		    }
    		  ]
    		};
      // 使用刚指定的配置项和数据显示图表。
      myChartleft1.setOption(optionleft1);