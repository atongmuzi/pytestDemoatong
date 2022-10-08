import xmind  # 加载包
from xmind.core.const import TOPIC_DETACHED
from xmind.core.topic import TopicElement
from xmind.core.markerref import MarkerId


def design_sheet1(sheet1):
    # ***** 第一个画布 *****
    sheet1.setTitle("画布1")  # 设置画布名称

    # 获取画布的中心主题，默认创建画布时会新建一个空白中心主题
    root_topic1 = sheet1.getRootTopic()
    root_topic1.setTitle("根节点")  # 设置主题名称

    # 创建一个子主题，并设置其名称
    sub_topic1 = root_topic1.addSubTopic()
    sub_topic1.setTitle("节点1")

    sub_topic2 = root_topic1.addSubTopic()
    sub_topic2.setTitle("节点2")

    sub_topic3 = root_topic1.addSubTopic()
    sub_topic3.setTitle("节点3")
    # 除了新建子主题，还可以创建自由主题(注意:只有中心主题支持创建自由主题)
    detached_topic1 = root_topic1.addSubTopic(topics_type=TOPIC_DETACHED)
    detached_topic1.setTitle("主题")
    detached_topic1.setPosition(0, 30)


def gen_sheet2(workbook, sheet1):
    # ***** 设计第二个画布 *****
    sheet2 = workbook.createSheet()
    sheet2.setTitle("画布2")

    # 获取画布的中心主题
    root_topic2 = sheet2.getRootTopic()
    root_topic2.setTitle("根节点")

    # 使用另外一种方法创建子主题
    topic1 = TopicElement(ownerWorkbook=workbook)
    # 给子主题添加一个主题间超链接，通过指定目标主题ID即可，这里链接到第一个画布
    topic1.setTopicHyperlink(sheet1.getID())
    topic1.setTitle("跳转到画布1")

    topic2 = TopicElement(ownerWorkbook=workbook)
    topic2.setTitle("URL链接")
    # 给子主题添加一个URL超链接
    topic2.setURLHyperlink("https://www.baidu.com")
    topic3 = TopicElement(ownerWorkbook=workbook)
    # 给子主题添加一个备注（快捷键F4)
    topic3.setPlainNotes("这是做备注的啊")
    topic3.setTitle("节点 \n 备注")

    topic4 = TopicElement(ownerWorkbook=workbook)
    # 给子主题添加一个文件超链接
    topic4.setFileHyperlink("datou.png")
    topic4.setTitle("文件超链接")

    topic1_1 = TopicElement(ownerWorkbook=workbook)
    topic1_1.setTitle("子节点")
    # 给子主题添加一个标签（目前XMind软件仅支持添加一个，快捷键）
    topic1_1.addLabel("一个标签")

    topic1_1_1 = TopicElement(ownerWorkbook=workbook)
    topic1_1_1.setTitle("添加标记")
    # 给子主题添加两个图标
    topic1_1_1.addMarker(MarkerId.starBlue)
    topic1_1_1.addMarker(MarkerId.flagGreen)

    topic2_1 = TopicElement(ownerWorkbook=workbook)
    topic2_1.setTitle("添加评论")
    # 给子主题添加一个批注（评论）
    topic2_1.addComment("这是一个评论!")
    topic2_1.addComment(content="你好啊!", author='baby')

    # 将创建好的子主题添加到其父主题下
    root_topic2.addSubTopic(topic1)
    root_topic2.addSubTopic(topic2)
    root_topic2.addSubTopic(topic3)
    root_topic2.addSubTopic(topic4)
    topic1.addSubTopic(topic1_1)
    topic2.addSubTopic(topic2_1)
    topic1_1.addSubTopic(topic1_1_1)

    # 给中心主题下的每个子主题添加一个优先级图标
    topics = root_topic2.getSubTopics()
    for index, topic in enumerate(topics):
        topic.addMarker("priority-" + str(index + 1))

    # 添加一个主题与主题之间的联系
    sheet2.createRelationship(topic1.getID(), topic2.getID(), "关联")


# 1、如果指定的XMind文件存在，则加载，否则创建一个新的
workbook = xmind.load("my.xmind")
# 2、获取第一个画布（Sheet），默认新建一个XMind文件时，自动创建一个空白的画布
sheet1 = workbook.getPrimarySheet()
# 对第一个画布进行设计完善
design_sheet1(sheet1)
# 3、创建第二个画布
gen_sheet2(workbook, sheet1)
# 4、保存（如果指定path参数，另存为该文件名）
xmind.save(workbook, path='test.xmind')
