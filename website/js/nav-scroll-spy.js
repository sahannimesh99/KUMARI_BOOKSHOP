((root, factory, undefined) => {
		if (typeof define === 'function' && define.amd) {
				//AMD
				define(['jquery'], factory);
		} else if (typeof exports === 'object') {
				//CommonJS
				const $ = requie('jquery');
				module.exports = factory($);
		} else {
				//都不是，浏览器全局定义
				root.navScrollSpy = factory(root.jQuery);
		}
})(window, ($) => {
		const pluginName = 'jqNavScrollSpy';
		const defaults = {
				navItems: '.nav-item', //导航元素
				scrollContainer: 'html,body', //滚动的容器
				spyItems: '.spy-item', //监视的元素
				easing: 'swing', //动效
				speed: 550 //速度
		}
		class jqNavScrollSpy {
				constructor(element, configs) {
						this._element = element;
						this.$win = $(window);
						this.defaults = $.extend({}, defaults, configs);
						this.init();
				}
				//初始化
				init() {
						this.$navItems = $(this.defaults.navItems);
						this.$spyItems = $(this.defaults.spyItems);
						this.$scrollContainer = $(this.defaults.scrollContainer);
						this.fixTop = $(this.$spyItems[0]).offset().top;  //修正初始化的时候元素距离顶部的距离不等于滚动的距离的变量，也就是减去第一个元素距离顶部的高度
						this.spyItemsData = this.getSpyItemsData();
						this.spyScroll();
						this.clickSwitch();
				}
				//监听滚动事件
				spyScroll() {
						this.$win.on('scroll', this.throttle(this.scrollCallBack,100,200));
				}
				//滚动监听的回调函数
				scrollCallBack(){
					let spyIndex = this.getVisibleElIndex();
					this.changeNav(this.$navItems[spyIndex]);
				}
				//存储监视滚动元素的中心位置数组
				getSpyItemsData(){
					let spyItemsData = [];
					this.$spyItems.each((index)=>{
						spyItemsData[index] = (this.getOffsetTop(index)+this.getOffsetTop(index)+$(this.$spyItems[index]).height())/2
					});
					return spyItemsData;
				}
				//获得当前滚动到视图区的元素的索引
				getVisibleElIndex(){
					let spyIndex;
					const scrollTop = parseInt(this.$win.scrollTop());
					$.each(this.spyItemsData,(index)=>{
						if(this.spyItemsData[0] >= scrollTop){
							spyIndex = 0;
							return true
						}else if(this.spyItemsData[index] <= scrollTop && scrollTop <= this.spyItemsData[index+1]){
							spyIndex = index+1;
							return true
						}
					});
					return spyIndex;
				}
				//节流函数
				throttle(func, wait, mustRun) {
						let timeout,
								context = this,
								startTime = new Date();
						return function() {
								let args = arguments,
										curTime = new Date();
								clearTimeout(timeout);
								// 如果达到了规定的触发时间间隔，触发 handler
								if (curTime - startTime >= mustRun) {
										func.apply(context, args);
										startTime = curTime;
										// 没达到触发间隔，重新设定定时器
								} else {
										timeout = setTimeout(func.bind(context), wait);
								}
						};
				}
				//点击切换
				clickSwitch() {
						const _this = this;
						this.$navItems.on("click", function() {
								_this.changeNav(this);
								const navIndex = $(this).index();
								_this.$win.off("scroll");
								_this.scrollIntoView(navIndex);
						});
				}
				//改变导航active
				changeNav(currentNav) {
						this.$navItems.removeClass("active");
						$(currentNav).addClass("active");
				}
				//滚动到可视区
				scrollIntoView(navIndex) {
						const offsetTop = parseInt(this.getOffsetTop(navIndex));
						if (!this.$scrollContainer.is(":animated")) {
								this.$scrollContainer.stop().animate({ 'scrollTop': offsetTop }, this.defaults.speed, this.defaults.easing, () => {
										//动画结束后重新注册滚动监听事件
										this.spyScroll();
								});
						}
				}
				//获取滚动元素距离顶部的距离
				getOffsetTop(index) {
						return parseInt($(this.$spyItems[index]).offset().top) - parseInt(this.fixTop);
				}
		}
		$.fn.jqNavScrollSpy = function(configs) {
				return this.each(function() {
						if (!$.data(this, "plugin_" + pluginName)) {
								$.data(this, "plugin_" + pluginName, new jqNavScrollSpy(this, configs));
						}else{
							$.data(this, "plugin_" + pluginName, null);
							$.data(this, "plugin_" + pluginName, new jqNavScrollSpy(this, configs));
						}
				});
		}
});
