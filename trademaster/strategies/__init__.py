from trademaster.utils.registry import Registry

STRATEGIES = Registry('strategy')

# Register strategies here if needed

# 注册一些示例策略
@STRATEGIES.register_module
class SimpleStrategy:
    def __init__(self, initial_balance):
        self.balance = initial_balance