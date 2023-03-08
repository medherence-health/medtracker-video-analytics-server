#!/usr/bin/env bash
ACTION_NET_MODEL="https://github.com/OlafenwaMoses/Action-Net/releases/download/v1/action_net_ex-060_acc-0.745313.h5"
ACTION_NET_MODEL_CLASSES="https://raw.githubusercontent.com/OlafenwaMoses/Action-Net/master/model_class.json"
#
wget -r --tries=5 $ACTION_NET_MODEL -O "models/action_net_ex-060_acc-0.745313.h5"
wget -r --tries=5 $ACTION_NET_MODEL_CLASSES -O "models/model_class.json"