#!/usr/bin/python3.6

import websocket
import json
from six import print_


def do_nothing(event): pass


def print_event(event): print_(event)


def to_candle_subscribe_json(figi, interval):
    return '''{ "event": "candle:subscribe", "figi": "%s", "interval": "%s" }''' % (figi, interval)


def to_orderbook_subscribe_json(figi, depth):
    return '''{ "event": "orderbook:subscribe", "figi": "%s", "depth": %s }''' % (figi, depth)


def to_instrument_info_subscribe_json(figi):
    return '''{ "event": "instrument_info:subscribe", "figi": "%s" }''' % (figi)


def callback_decider(event_string,
                     on_candle_event,
                     on_orderbook_event,
                     on_instrument_info_event):
    event_json = json.loads(event_string)
    event_type = event_json['event']
    event_payload = event_json['payload']

    if event_type == 'candle':
        on_candle_event(event_payload)
    elif event_type == 'orderbook':
        on_orderbook_event(event_payload)
    elif event_type == 'instrument_info':
        on_instrument_info_event(event_payload)
    else:
        raise Exception("unknown event type - %s" % event_type)


def subscribe_to(ws, candle_subs=(), orderbook_subs=(), instrument_info_subs=()):
    subscribtions_list = []

    subscribtions_list.extend(map(lambda x: to_candle_subscribe_json(x['figi'], x['interval']), candle_subs))

    subscribtions_list.extend(map(lambda x: to_orderbook_subscribe_json(x['figi'], x['depth']), orderbook_subs))

    subscribtions_list.extend(map(lambda x: to_instrument_info_subscribe_json(x['figi']), instrument_info_subs))

    for sub in subscribtions_list:
        print_("sending: %s" % sub)
        ws.send(sub)


def run_stream_consumer(token,
                        candle_subs=(),
                        orderbook_subs=(),
                        instrument_info_subs=(),
                        on_candle_event=do_nothing,
                        on_orderbook_event=do_nothing,
                        on_instrument_info_event=do_nothing):
    """
    | subscriptions example:
    |    candle_subs = [{'figi': 'BBG000B9XRY4', 'interval': '1min'}, {'figi': 'BBG009S39JX6', 'interval': '1min'}]
    |    orderbook_subs = [{'figi': 'BBG000B9XRY4', 'depth': 3}, {'figi': 'BBG009S39JX6', 'depth': 3}]
    |    instrument_info_subs = [{'figi': 'BBG000B9XRY4'}, {'figi': 'BBG009S39JX6'}]
    |
    | callback example:
    |    lambda x: print(x)
    """

    url = 'wss://api-invest.tinkoff.ru/openapi/md/v1/md-openapi/ws'

    ws = websocket.WebSocketApp(
        url=url,
        header=["Authorization: Bearer %s" % token],
        on_open=lambda ws: subscribe_to(ws, candle_subs, orderbook_subs, instrument_info_subs),
        on_message=lambda ws, msg: callback_decider(msg, on_candle_event, on_orderbook_event, on_instrument_info_event),
        on_error=lambda ws, err: print_(err)
    )

    try:
        ws.run_forever()
    except KeyboardInterrupt:
        ws.close()
        raise
