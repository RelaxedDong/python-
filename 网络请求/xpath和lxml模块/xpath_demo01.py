#encoding:utf-8

# xpath:语法
'''选取节点：
XPath 使用路径表达式来选取 XML 文档中的节点或者节点集。这些路径表达式和我们在常规的电脑文件系统中看到的表达式非常相似。

表达式	描述	示例	结果
nodename	选取此节点的所有子节点	bookstore	选取bookstore下所有的子节点
/	如果是在最前面，代表从根节点选取。否则选择某节点下的某个节点	/bookstore	选取根元素下所有的bookstore节点
//	从全局节点中选择节点，随便在哪个位置	//book	从全局节点中找到所有的book节点
@	选取某个节点的属性	//book[@price]	选择所有拥有price属性的book节点
.	当前节点	./a	选取当前节点下的a标签
谓语：
谓语用来查找某个特定的节点或者包含某个指定的值的节点，被嵌在方括号中。
在下面的表格中，我们列出了带有谓语的一些路径表达式，以及表达式的结果：

路径表达式	描述
/bookstore/book[1]	选取bookstore下的第一个子元素
/bookstore/book[last()]	选取bookstore下的倒数第二个book元素。
bookstore/book[position()<3]	选取bookstore下前面两个子元素。
//book[@price]	选取拥有price属性的book元素
//book[@price=10]	选取所有属性price等于10的book元素
'''

'''
通配符
*表示通配符。

通配符	描述	示例	结果
*	匹配任意节点	/bookstore/*	选取bookstore下的所有子元素。
@*	匹配节点中的任何属性	//book[@*]	选取所有带有属性的book元素。'''















