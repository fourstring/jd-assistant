#!/usr/bin/env python
# -*- coding:utf-8 -*-
from config import global_config
from jd_assistant import Assistant

TESTING = False  # 设为True测试下单功能是否正常

if global_config.getboolean('notification', 'enabled'):
    from notification import telegram_success_notify_callback

    notify = True
else:
    notify = False
if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """
    if not TESTING:
        sku_ids = [100006784140, 100006784144, 100010222606, 100006248177, 1835968, 1835967, 100005151507, 100005818743,
                   100010638508, 100009445348, 100009441994, 100009109410, 100006248247, 4642656, 100009130434, 7498167,
                   51137726169]
        skus = ','.join(f'{i}:1' for i in sku_ids)
        with Assistant() as asst:
            asst.login_by_QRcode()  # 扫码登陆
            asst.clear_cart()
            # asst.exec_reserve_seckill_by_time(sku_id="100009083498", buy_time="2019-11-10 22:42:30.000")
            asst.buy_item_in_stock(sku_ids=skus, area='18_1495_29449_30737', submit_retry=5, stock_interval=1,
                                   submit_interval=5,
                                   then_callbacks=[telegram_success_notify_callback] if notify else None)
    else:
        with Assistant() as asst:
            asst.login_by_QRcode()  # 扫码登陆
            asst.clear_cart()  # 清空购物车（可选）
            asst.add_item_to_cart(sku_ids='100008348584')  # 根据商品id添加购物车（可选）
            asst.submit_order()  # 直接提交订单
    # 执行预约抢购
    # 5个参数
    # sku_id: 商品id
    # buy_time: 下单时间，例如：'2019-11-10 22:41:30.000'
    # retry: 抢购重复执行次数，可选参数，默认4次
    # interval: 抢购执行间隔，可选参数，默认4秒
    # num: 购买数量，可选参数，默认1个
