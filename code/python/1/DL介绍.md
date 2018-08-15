Tensorflow 介绍
----------

+ 数据流图
 >+ 线和节点
+ 特点：
 >+ 灵活性
 >+ 可移植性
 >+ 多语言支持
 >+ 异步执行
+ 基本概念
 >- 图(Graph)是一个计算的流程
 >- 张量（Tensor）数据源
 >- 操作（op） 图中的节点就是op
 >- 会话（Session） 属于是控制
 >- 变量（Variable） 运行过程会改变，用于维护状态
 
+ 对比
> Tensorflow 和其他框架对比

| 库名称 | Caffe| MXNet | Tensorflow |
|---|---|---|---|
| 开发语言|c++ cuda |c++ cuda |c++ cuda python|
|支持接口| c++ python matlab| python R Julia |c++ python|
|安装难度| 难| 比较难|简单|
|示例数量|多|比较多|少|
|支持模型|CNN |CNN RNN  |CNN RNN|
|上手难度|比较难|简单|难|

+ 应用
>+ 语音识别

