#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant
from notification import telegram_success_notify_callback

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """
    sku_ids = [100006784140, 100006784144, 100010222606, 100006248177, 1835968, 1835967, 100005151507, 100005818743,
               100010638508, 100009445348, 100009441994, 100009109410]
    skus = ','.join(f'{i}:1' for i in sku_ids)
    with Assistant() as asst:
        asst.login_by_QRcode()  # 扫码登陆
        asst.clear_cart()
        # asst.exec_reserve_seckill_by_time(sku_id="100009083498", buy_time="2019-11-10 22:42:30.000")
        asst.buy_item_in_stock(sku_ids=skus, area='18_1495_29449_30737', submit_retry=2, stock_interval=2,
                               then_callbacks=[telegram_success_notify_callback])
    # 执行预约抢购
    # 5个参数
    # sku_id: 商品id
    # buy_time: 下单时间，例如：'2019-11-10 22:41:30.000'
    # retry: 抢购重复执行次数，可选参数，默认4次
    # interval: 抢购执行间隔，可选参数，默认4秒
    # num: 购买数量，可选参数，默认1个
