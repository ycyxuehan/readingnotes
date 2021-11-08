# PromQL

promQL的一些示例与解析。

#### `up{instance="localhost:9090", job="prometheus"}`

up 是一个指标名
instance 是一个标签，表示被抓取的目标地址
job 是一个标签，来自文件`prometheus.yml`的配置项`job_name`

#### `process_resident_memory_bytes`

gauge 类型， 服务当前使用的内存，单位字节
gauge类型表示当前绝对值很重要

#### `prometheus_tsdb_head_samples_appended_total`

counter类型，跟踪事件发生的数量

`rate(prometheus_tsdb_head_samples_appended_total[1m])`

计算一分钟内的平均采样数

rate是一个函数，这里用来计算counter每秒增长的速度

[1m] 表示取一分钟内的值

