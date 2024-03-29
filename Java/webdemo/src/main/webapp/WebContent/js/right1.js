/**
 * 
 */
/**
 * 
 */
  // 基于准备好的dom，初始化echarts实例
      var myChartright1 = echarts.init(document.getElementById('right1'),"dark");

      // 指定图表的配置项和数据
      var optionright1 = {
        title: {
          text: 'ECharts 入门示例'
        },
        tooltip: {},
        legend: {
          data: ['销量']
        },
        xAxis: {
          data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子','帽子']
        },
        yAxis: {},
        series: [
          {
            name: '销量',
            type: 'bar',
            data: [5, 20, 36, 10, 10, 20,100]
          }
        ]
      };

      // 使用刚指定的配置项和数据显示图表。
      myChartright1.setOption(optionright1);